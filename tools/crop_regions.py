#!/usr/bin/env python3
"""Recorta regiões em PNG (sem recompressão), com ampliação opcional para inspeção."""
import argparse
import json
import os
from _common import load, parse_named_region, clamp_box

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("image")
ap.add_argument("--region", action="append", default=[], help="nome=x,y,w,h")
ap.add_argument("--regions-file", help="JSON {nome: [x,y,w,h]}")
ap.add_argument("--upscale", type=int, default=1, help="fator inteiro (vizinho mais próximo)")
ap.add_argument("--out", default="crops")
args = ap.parse_args()

img = load(args.image)
regions = dict(parse_named_region(r) for r in args.region)
if args.regions_file:
    with open(args.regions_file, encoding="utf-8") as fh:
        regions.update({k: tuple(v) for k, v in json.load(fh).items()})
if not regions:
    raise SystemExit("Informe --region nome=x,y,w,h ou --regions-file")
os.makedirs(args.out, exist_ok=True)
from PIL import Image
for name, box in regions.items():
    x0, y0, x1, y1 = clamp_box(box, img.size)
    if x1 <= x0 or y1 <= y0:
        print(f"[pulado] {name}: fora da imagem")
        continue
    crop = img.crop((x0, y0, x1, y1))
    if args.upscale > 1:
        crop = crop.resize((crop.width * args.upscale, crop.height * args.upscale), Image.NEAREST)
    path = os.path.join(args.out, f"{name}.png")
    crop.save(path)
    print(f"{path}  ({x1 - x0}x{y1 - y0} px, origem x={x0} y={y0})")
