#!/usr/bin/env python3
"""Informações da imagem e candidatos de escala/viewport. Saída = [ESTIMADO]."""
import argparse
from _common import load, COMMON_VIEWPORTS

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("image")
args = ap.parse_args()

img = load(args.image)
W, H = img.size
print(f"Arquivo: {args.image}\nResolução: {W} x {H} px | proporção {W / H:.4f}")
print("Candidatos de escala (largura / escala ≈ largura de viewport comum):")
found = False
for scale in (1, 2, 3):
    for vw, vh in COMMON_VIEWPORTS:
        if abs(W / scale - vw) <= 1:
            found = True
            exp_h = vh * scale
            note = "altura compatível" if abs(H - exp_h) <= 2 else f"altura difere (esperado {exp_h}; pode ser captura parcial/rolagem)"
            print(f"  @{scale}x -> viewport {vw}px de largura ({note})")
if not found:
    print("  Nenhum viewport comum bate. Provável imagem redimensionada/recortada: declare a escala como PREMISSA e calibre com uma âncora conhecida.")
print("Lembrete: confirme com uma âncora (barra de status, ícone 24px, input 40-48px) antes de tratar como fato.")
