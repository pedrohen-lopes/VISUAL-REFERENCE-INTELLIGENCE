#!/usr/bin/env python3
"""Cria a estrutura de entrega para o Claude Code em uma pasta de projeto.
Copia CLAUDE.md, .claude/commands/, tools/ essenciais e os modelos de spec/.
Não sobrescreve sem --force. Se houver imagem em references/, gera regions.json com viewport detectado."""
import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parent.parent
HANDOFF = KIT / "claude-code-handoff"

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("--target", required=True, help="pasta do projeto de destino")
ap.add_argument("--force", action="store_true", help="sobrescrever arquivos existentes")
args = ap.parse_args()

if not HANDOFF.exists():
    sys.exit(f"Pasta {HANDOFF} não encontrada. Rode este script a partir do kit completo.")
target = Path(args.target).resolve()
target.mkdir(parents=True, exist_ok=True)
log = []


def put(src, dst):
    if dst.exists() and not args.force:
        log.append(f"mantido (já existe): {dst.relative_to(target)}")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    log.append(f"criado: {dst.relative_to(target)}")


def write(dst, text):
    if dst.exists() and not args.force:
        log.append(f"mantido (já existe): {dst.relative_to(target)}")
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8")
    log.append(f"criado: {dst.relative_to(target)}")


# 1. Core files
put(HANDOFF / "CLAUDE.md", target / "CLAUDE.md")
for f in sorted((HANDOFF / ".claude" / "commands").glob("*.md")):
    put(f, target / ".claude" / "commands" / f.name)

# 2. Essential tools only (not __pycache__, not test scripts)
essential_tools = {
    "check_env.py", "image_info.py", "sample_colors.py", "crop_regions.py",
    "grid_overlay.py", "image_diff.py", "image_report.py", "ocr_text.py",
    "screenshot.py", "validate_tokens.py", "extract_frames.py", "requirements.txt"
}
for f in sorted((KIT / "tools").iterdir()):
    if f.is_file() and f.name in essential_tools:
        put(f, target / "tools" / f.name)

# 3. Spec templates
mapping = {
    "TECHNICAL_SPECIFICATION_TEMPLATE.md": "specification.md",
    "DESIGN_TOKENS_TEMPLATE.json": "tokens.json",
    "COMPONENT_INVENTORY_TEMPLATE.md": "components.md",
    "ACCEPTANCE_CRITERIA_TEMPLATE.md": "acceptance.md",
}
for src, name in mapping.items():
    put(KIT / "templates" / src, target / "spec" / name)

# 4. requirements.md (matriz REQ)
write(target / "spec" / "requirements.md",
      "# Matriz de requisitos\n\n| REQ | Requisito | Origem (REF/VIDEO) | Tag | Confiança | Critério | Status |\n|---|---|---|---|---|---|---|\n")

# 5. regions.json — tenta detectar viewport da primeira imagem em references/
regions_json = target / "spec" / "regions.json"
refs_dir = target / "references"
refs_dir.mkdir(parents=True, exist_ok=True)
img_exts = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
first_ref = next((p for p in refs_dir.iterdir() if p.suffix.lower() in img_exts), None)

if first_ref:
    # Tenta rodar image_info.py para obter viewport
    try:
        r = subprocess.run(
            [sys.executable, str(target / "tools" / "image_info.py"), str(first_ref)],
            capture_output=True, text=True, timeout=10
        )
        viewport = None
        for line in r.stdout.splitlines():
            # Procura padrões: "@1x -> viewport 1440px" ou "1440 x 900"
            import re
            m = re.search(r"viewport\s+(\d+)px", line, re.IGNORECASE)
            if m:
                w = int(m.group(1))
                # Tenta achar altura na mesma linha ou na resolução
                m2 = re.search(r"(\d+)\s*[x×]\s*(\d+)", line)
                if m2:
                    h = int(m2.group(2))
                else:
                    # Usa proporção da imagem
                    from PIL import Image
                    with Image.open(first_ref) as im:
                        iw, ih = im.size
                    h = int(w * ih / iw)
                viewport = (w, h)
                break
        if not viewport:
            # Fallback: resolução da imagem
            from PIL import Image
            with Image.open(first_ref) as im:
                viewport = im.size
        if viewport:
            w, h = viewport
            regions = {
                "A_header": [0, 0, w, min(120, h // 6)],
                "B_main": [0, min(120, h // 6), w, h - min(120, h // 6) - min(80, h // 12)],
                "C_footer": [0, h - min(80, h // 12), w, min(80, h // 12)],
            }
        else:
            regions = {"A_exemplo": [0, 0, 100, 100]}
    except Exception:
        regions = {"A_exemplo": [0, 0, 100, 100]}
else:
    regions = {"A_exemplo": [0, 0, 100, 100]}

write(regions_json, json.dumps(regions, ensure_ascii=False, indent=2))

# 6. Diretórios de trabalho
for d in ("references", "assets", "reports"):
    write(target / d / ".gitkeep", "")

print("\n".join(log))
print(f"\nPronto em {target}.")
if first_ref:
    print(f"  → regions.json gerado com viewport detectado de {first_ref.name}")
else:
    print("  → Coloque as imagens em references/ e rode novamente para regions.json automático.")
print("  → Próximo: abra o Claude Code nesta pasta e use /analisar")