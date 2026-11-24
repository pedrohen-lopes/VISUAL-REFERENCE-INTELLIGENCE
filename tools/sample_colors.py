#!/usr/bin/env python3
"""Lê cores: pontos, regiões (mediana) e paleta dominante. Cores de JPEG são ESTIMADAS."""
import argparse
import numpy as np
from _common import load, parse_region, hex_of, clamp_box, dump_json

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("image")
ap.add_argument("--point", action="append", default=[], help="x,y (mediana de janela 5x5)")
ap.add_argument("--region", action="append", default=[], help="x,y,w,h (mediana da região)")
ap.add_argument("--palette", type=int, default=0, help="N cores dominantes da imagem")
ap.add_argument("--json", action="store_true")
args = ap.parse_args()

img = load(args.image)
arr = np.asarray(img)
H, W = arr.shape[:2]
out = {"points": [], "regions": [], "palette": []}

for p in args.point:
    x, y = [int(v) for v in p.split(",")]
    x0, y0, x1, y1 = clamp_box((x - 2, y - 2, 5, 5), (W, H))
    win = arr[y0:y1, x0:x1].reshape(-1, 3)
    med = np.median(win, axis=0)
    std = float(win.std(axis=0).max())
    out["points"].append({"point": [x, y], "hex": hex_of(med), "rgb": [int(v) for v in med],
                          "variacao": round(std, 1),
                          "aviso": "alta variação: borda, gradiente ou ruído; reamostre no centro de uma área chapada" if std > 12 else ""})

for r in args.region:
    box = parse_region(r)
    x0, y0, x1, y1 = clamp_box(box, (W, H))
    if x1 <= x0 or y1 <= y0:
        raise SystemExit(f"Região fora da imagem: {r}")
    win = arr[y0:y1, x0:x1].reshape(-1, 3)
    med = np.median(win, axis=0)
    std = float(win.std(axis=0).max())
    out["regions"].append({"region": list(box), "hex": hex_of(med), "rgb": [int(v) for v in med],
                           "variacao": round(std, 1),
                           "tipo": "chapada" if std < 6 else "gradiente/textura/conteúdo misto"})

if args.palette:
    small = img.copy()
    small.thumbnail((400, 400))
    q = small.quantize(colors=args.palette, method=2)
    pal = q.getpalette()[: args.palette * 3]
    counts = sorted(q.getcolors(), reverse=True)
    total = sum(c for c, _ in counts)
    for c, idx in counts:
        rgb = pal[idx * 3: idx * 3 + 3]
        out["palette"].append({"hex": hex_of(rgb), "percentual": round(100 * c / total, 1)})

if args.json:
    print(dump_json(out))
else:
    for p in out["points"]:
        print(f"ponto {p['point']}: {p['hex']} rgb{tuple(p['rgb'])} variação={p['variacao']} {p['aviso']}")
    for r in out["regions"]:
        print(f"região {r['region']}: {r['hex']} rgb{tuple(r['rgb'])} variação={r['variacao']} ({r['tipo']})")
    for c in out["palette"]:
        print(f"paleta: {c['hex']}  {c['percentual']}%")
print("# Tag: [ESTIMADO] (confiança ALTA só para áreas chapadas em PNG; JPEG = MÉDIA/BAIXA)")
