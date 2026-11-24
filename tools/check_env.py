#!/usr/bin/env python3
"""Verifica quais ferramentas estão disponíveis. Rode ANTES de usar os demais scripts."""
import importlib
import shutil
import subprocess


def module(name, label=None):
    try:
        mod = importlib.import_module(name)
        return f"OK  {label or name} {getattr(mod, '__version__', '')}".strip()
    except Exception:
        return f"--  {label or name}: não instalado"


def binary(name, args):
    path = shutil.which(name)
    if not path:
        return f"--  {name}: não encontrado"
    try:
        out = subprocess.run([path] + args, capture_output=True, text=True, timeout=15)
        first = (out.stdout or out.stderr).splitlines()[0] if (out.stdout or out.stderr) else ""
        return f"OK  {name}: {first}"
    except Exception as exc:
        return f"??  {name}: {exc}"


print("== Python ==")
for m, l in [("PIL", "Pillow (obrigatório)"), ("numpy", "numpy (obrigatório)"),
             ("skimage", "scikit-image (SSIM, opcional)"), ("cv2", "opencv (opcional)"),
             ("pytesseract", "pytesseract (OCR, opcional)"),
             ("playwright", "playwright (screenshots, opcional)")]:
    print(module(m, l))
print("== Binários ==")
print(binary("tesseract", ["--version"]))
print(binary("ffmpeg", ["-version"]))
print(binary("git", ["--version"]))
print("\nUse apenas o que aparece como OK. Itens ausentes reduzem o que pode ser validado: declare isso no relatório.")
