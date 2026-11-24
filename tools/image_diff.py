#!/usr/bin/env python3
"""Compara referência x resultado: % de pixels divergentes, SSIM (se houver), por região, e gera imagens."""
import argparse
import json
import os
import numpy as np
from PIL import Image, ImageDraw
from _common import load, parse_named_region, clamp_box, dump_json

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("reference")
ap.add_argument("result")
ap.add_argument("--tolerance", type=int, default=8, help="tolerância por canal (0-255)")
ap.add_argument("--region", action="append", default=[], help="nome=x,y,w,h (comparação por região)")
ap.add_argument("--regions-file", help="JSON {nome: [x,y,w,h]}")
ap.add_argument("--out", default="diff_out")
args = ap.parse_args()

ref, res = load(args.reference), load(args.result)
notes = []
if ref.size != res.size:
    notes.append(f"Tamanhos diferentes: referência {ref.size}, resultado {res.size}. Resultado redimensionado só para comparar; "
                 "isso INVALIDA medidas de posição/tamanho. Capture na mesma resolução/escala.")
    res = res.resize(ref.size, Image.LANCZOS)
a, b = np.asarray(ref).astype(int), np.asarray(res).astype(int)
delta = np.abs(a - b).max(axis=2)
mask = delta > args.tolerance
pct = 100 * mask.mean()
os.makedirs(args.out, exist_ok=True)

heat = np.zeros_like(a, dtype=np.uint8)
heat[..., 0] = np.clip(delta * 4, 0, 255)
heat[..., 1] = (a.mean(axis=2) * 0.25).astype(np.uint8)
heat[..., 2] = (a.mean(axis=2) * 0.25).astype(np.uint8)
Image.fromarray(heat).save(os.path.join(args.out, "diff_heatmap.png"))
Image.blend(ref, res, 0.5).save(os.path.join(args.out, "overlay.png"))
sbs = Image.new("RGB", (ref.width * 2 + 10, ref.height), (255, 0, 255))
sbs.paste(ref, (0, 0))
sbs.paste(res, (ref.width + 10, 0))
sbs.save(os.path.join(args.out, "side_by_side.png"))

report = {"tolerancia_canal": args.tolerance, "pixels_divergentes_pct": round(float(pct), 3),
          "maior_delta": int(delta.max()), "avisos": notes}
try:
    from skimage.metrics import structural_similarity as ssim
    report["ssim"] = round(float(ssim(np.asarray(ref.convert("L")), np.asarray(res.convert("L")))), 4)
except Exception:
    report["ssim"] = "indisponível (instale scikit-image)"

regions = dict(parse_named_region(r) for r in args.region)
if args.regions_file:
    with open(args.regions_file, encoding="utf-8") as fh:
        regions.update({k: tuple(v) for k, v in json.load(fh).items()})
rep_regions = []
marked = ref.copy()
draw = ImageDraw.Draw(marked)
for name, box in regions.items():
    x0, y0, x1, y1 = clamp_box(box, ref.size)
    if x1 <= x0 or y1 <= y0:
        continue
    sub = mask[y0:y1, x0:x1]
    p = 100 * sub.mean()
    ys, xs = np.nonzero(sub)
    bbox = [int(xs.min()) + x0, int(ys.min()) + y0, int(xs.max() - xs.min()) + 1, int(ys.max() - ys.min()) + 1] if len(xs) else None
    rep_regions.append({"regiao": name, "box": [x0, y0, x1 - x0, y1 - y0], "divergente_pct": round(float(p), 3),
                        "caixa_da_divergencia": bbox,
                        "sugestao_de_atencao": "investigar (provável Alta/Crítica)" if p > 15 else
                        "investigar (provável Média)" if p > 3 else "ok/Baixa (confirme visualmente)" if p > 0.2 else "sem divergência relevante"})
    draw.rectangle([x0, y0, x1 - 1, y1 - 1], outline=(255, 0, 80), width=2)
    draw.text((x0 + 4, y0 + 4), name, fill=(255, 0, 80))
if regions:
    marked.save(os.path.join(args.out, "regions_marked.png"))
report["regioes"] = rep_regions
report["observacao"] = ("A sugestão de atenção é apenas um indicador numérico. A gravidade (Crítica/Alta/Média/Baixa) "
                        "deve ser decidida por inspeção das imagens, conforme instructions/STANDARDS.md.")
dump_json(report, os.path.join(args.out, "report.json"))
print(dump_json(report))
