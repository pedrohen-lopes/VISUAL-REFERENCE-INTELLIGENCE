#!/usr/bin/env python3
"""Converte uma imagem em um relatório de TEXTO (Markdown) para quem não consegue ver imagens
(ex.: Claude Code sem visão): metadados, paleta, faixas horizontais, mapa de cores por célula e OCR.
Tudo é [ESTIMADO]; não substitui a análise visual."""
import argparse
import os
import shutil
import subprocess
import sys
import numpy as np
from _common import load, hex_of, COMMON_VIEWPORTS

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("image")
ap.add_argument("--cols", type=int, default=12)
ap.add_argument("--rows", type=int, default=8)
ap.add_argument("--palette", type=int, default=8)
ap.add_argument("--no-ocr", action="store_true")
ap.add_argument("--out", default="")
args = ap.parse_args()

img = load(args.image)
arr = np.asarray(img).astype(int)
H, W = arr.shape[:2]
L = [f"# Relatório textual — {os.path.basename(args.image)}", "",
     "> Gerado automaticamente. Todos os valores são [ESTIMADO]. Não há análise visual aqui.", "",
     "## Metadados", f"- Resolução: {W} x {H} px (proporção {W / H:.3f})"]
cands = [f"@{s}x ≈ viewport {vw}px" for s in (1, 2, 3) for vw, _ in COMMON_VIEWPORTS if abs(W / s - vw) <= 1]
L.append("- Escala/viewport candidatos: " + (", ".join(cands) if cands else "nenhum viewport comum (declare premissa)"))

small = img.copy()
small.thumbnail((400, 400))
q = small.quantize(colors=args.palette, method=2)
pal = q.getpalette()[: args.palette * 3]
cols = sorted(q.getcolors(), reverse=True)
tot = sum(c for c, _ in cols)
L += ["", "## Paleta dominante", "| HEX | % da imagem |", "|---|---|"]
for c, i in cols:
    L.append(f"| {hex_of(pal[i * 3:i * 3 + 3])} | {100 * c / tot:.1f}% |")

# faixas horizontais: agrupa linhas consecutivas de cor média parecida
rowmean = arr.mean(axis=1)
bands, start = [], 0
for y in range(1, H):
    if np.abs(rowmean[y] - rowmean[y - 1]).max() > 18:
        bands.append((start, y))
        start = y
bands.append((start, H))
bands = [(a, b) for a, b in bands if b - a >= 4]
L += ["", "## Faixas horizontais (mudanças fortes de cor média por linha)", "| y inicial | y final | altura | cor média |", "|---|---|---|---|"]
for a, b in bands[:40]:
    L.append(f"| {a} | {b} | {b - a} | {hex_of(arr[a:b].reshape(-1, 3).mean(axis=0))} |")
if len(bands) > 40:
    L.append(f"| ... | | | (+{len(bands) - 40} faixas omitidas) |")

L += ["", f"## Mapa de cores por célula ({args.cols} x {args.rows}, mediana por célula)", "| y\\x | " + " | ".join(str(int(c * W / args.cols)) for c in range(args.cols)) + " |",
      "|---|" + "---|" * args.cols]
for r in range(args.rows):
    y0, y1 = int(r * H / args.rows), int((r + 1) * H / args.rows)
    row = []
    for c in range(args.cols):
        x0, x1 = int(c * W / args.cols), int((c + 1) * W / args.cols)
        row.append(hex_of(np.median(arr[y0:y1, x0:x1].reshape(-1, 3), axis=0)))
    L.append(f"| {y0} | " + " | ".join(row) + " |")

L += ["", "## Texto (OCR)"]
if args.no_ocr:
    L.append("OCR desativado.")
elif not shutil.which("tesseract"):
    L.append("OCR indisponível (tesseract não encontrado). Texto NÃO extraído: peça a transcrição ao usuário.")
else:
    here = os.path.dirname(os.path.abspath(__file__))
    proc = subprocess.run([sys.executable, os.path.join(here, "ocr_text.py"), args.image], capture_output=True, text=True)
    L.append("```\n" + (proc.stdout.strip() or "(nenhum texto detectado)") + "\n```")
    if proc.stderr.strip():
        L.append("Avisos: " + proc.stderr.strip().splitlines()[0])
text = "\n".join(L)
if args.out:
    with open(args.out, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"Relatório salvo em {args.out}")
else:
    print(text)
