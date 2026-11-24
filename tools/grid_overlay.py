#!/usr/bin/env python3
"""Desenha uma grade com coordenadas sobre a imagem para facilitar medições visuais."""
import argparse
from PIL import ImageDraw, ImageFont
from _common import load

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("image")
ap.add_argument("--step", type=int, default=100, help="espaçamento da grade em px")
ap.add_argument("--out", default="grid_overlay.png")
args = ap.parse_args()

img = load(args.image).convert("RGBA")
layer = ImageDraw.Draw(img, "RGBA")
try:
    font = ImageFont.truetype("DejaVuSans.ttf", 14)
except Exception:
    font = ImageFont.load_default()
W, H = img.size
for x in range(0, W, args.step):
    layer.line([(x, 0), (x, H)], fill=(255, 0, 80, 120), width=1)
    layer.text((x + 3, 3), str(x), fill=(255, 0, 80, 255), font=font)
for y in range(0, H, args.step):
    layer.line([(0, y), (W, y)], fill=(0, 120, 255, 120), width=1)
    layer.text((3, y + 3), str(y), fill=(0, 120, 255, 255), font=font)
img.convert("RGB").save(args.out)
print(f"Grade salva em {args.out} (passo {args.step}px). Coordenadas em px da imagem original.")
