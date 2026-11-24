#!/usr/bin/env python3
"""Cria a estrutura de entrega para o Claude Code em uma pasta de projeto.
Copia CLAUDE.md, .claude/commands/, tools/ e os modelos de spec/. Não sobrescreve sem --force."""
import argparse
import shutil
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


put(HANDOFF / "CLAUDE.md", target / "CLAUDE.md")
for f in sorted((HANDOFF / ".claude" / "commands").glob("*.md")):
    put(f, target / ".claude" / "commands" / f.name)
for f in sorted((KIT / "tools").iterdir()):
    if f.is_file() and f.suffix in {".py", ".txt", ".md"}:
        put(f, target / "tools" / f.name)
mapping = {
    "TECHNICAL_SPECIFICATION_TEMPLATE.md": "specification.md",
    "DESIGN_TOKENS_TEMPLATE.json": "tokens.json",
    "COMPONENT_INVENTORY_TEMPLATE.md": "components.md",
    "ACCEPTANCE_CRITERIA_TEMPLATE.md": "acceptance.md",
}
for src, name in mapping.items():
    put(KIT / "templates" / src, target / "spec" / name)
write(target / "spec" / "requirements.md",
      "# Matriz de requisitos\n\n| REQ | Requisito | Origem (REF/VIDEO) | Tag | Confiança | Critério | Status |\n|---|---|---|---|---|---|---|\n")
write(target / "spec" / "regions.json", '{\n  "A_exemplo": [0, 0, 100, 100]\n}\n')
for d in ("references", "assets", "reports"):
    write(target / d / ".gitkeep", "")
print("\n".join(log))
print(f"\nPronto em {target}. Próximo: coloque as imagens em references/ e abra o Claude Code nesta pasta.")
