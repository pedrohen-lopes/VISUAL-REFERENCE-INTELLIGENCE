#!/usr/bin/env python3
"""OCR com Tesseract: texto, caixa e confiança por linha. Baixa confiança => [INCERTO]."""
import argparse
import shutil
import sys
from _common import load, parse_region, clamp_box, dump_json

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("image")
ap.add_argument("--region", help="x,y,w,h (OCR só nessa região)")
ap.add_argument("--lang", default="por+eng")
ap.add_argument("--upscale", type=int, default=2, help="amplia antes do OCR (melhora texto pequeno)")
ap.add_argument("--json", action="store_true")
args = ap.parse_args()

try:
    import pytesseract
except ImportError:
    sys.exit("pytesseract não instalado: pip install pytesseract (e instale o binário tesseract)")
if not shutil.which("tesseract"):
    sys.exit("Binário 'tesseract' não encontrado. Instale (sudo apt install tesseract-ocr tesseract-ocr-por / pkg install tesseract).")

img = load(args.image)
ox = oy = 0
if args.region:
    x0, y0, x1, y1 = clamp_box(parse_region(args.region), img.size)
    img = img.crop((x0, y0, x1, y1))
    ox, oy = x0, y0
lang = args.lang
try:
    available = set(pytesseract.get_languages())
    wanted = [l for l in lang.split("+") if l in available]
    if not wanted:
        sys.exit(f"Nenhum idioma de '{lang}' instalado (disponíveis: {sorted(available)}).")
    if len(wanted) < len(lang.split("+")):
        print(f"AVISO: idioma(s) ausente(s); usando {'+'.join(wanted)}. Acentos podem falhar sem 'por'.", file=sys.stderr)
    lang = "+".join(wanted)
except SystemExit:
    raise
except Exception:
    pass
k = max(1, args.upscale)
big = img.resize((img.width * k, img.height * k))
data = pytesseract.image_to_data(big, lang=lang, output_type=pytesseract.Output.DICT)
lines = {}
for i, txt in enumerate(data["text"]):
    if not txt.strip() or float(data["conf"][i]) < 0:
        continue
    key = (data["block_num"][i], data["par_num"][i], data["line_num"][i])
    d = lines.setdefault(key, {"words": [], "conf": [], "x0": 10**9, "y0": 10**9, "x1": 0, "y1": 0})
    d["words"].append(txt)
    d["conf"].append(float(data["conf"][i]))
    d["x0"] = min(d["x0"], data["left"][i])
    d["y0"] = min(d["y0"], data["top"][i])
    d["x1"] = max(d["x1"], data["left"][i] + data["width"][i])
    d["y1"] = max(d["y1"], data["top"][i] + data["height"][i])
out = []
for key in sorted(lines):
    d = lines[key]
    conf = sum(d["conf"]) / len(d["conf"])
    text = " ".join(d["words"])
    out.append({"texto": text if conf >= 80 else f'[INCERTO: "{text}"]', "confianca_ocr": round(conf, 1),
                "tag": "OBSERVADO" if conf >= 80 else "ESTIMADO",
                "caixa": [ox + d["x0"] // k, oy + d["y0"] // k, (d["x1"] - d["x0"]) // k, (d["y1"] - d["y0"]) // k]})
if args.json:
    print(dump_json(out))
else:
    for o in out:
        print(f"{o['caixa']} conf={o['confianca_ocr']:>5} {o['texto']}")
print("# OCR é auxiliar: confirme visualmente o texto literal (capitalização, acentos, símbolos).", file=sys.stderr)
