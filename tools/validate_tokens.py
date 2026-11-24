#!/usr/bin/env python3
"""Valida o JSON de design tokens: sintaxe, tags, confiança, cores HEX e referências {a.b.c}."""
import json
import re
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "DESIGN_TOKENS_TEMPLATE.json"
try:
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
except Exception as exc:
    sys.exit(f"JSON INVÁLIDO em {path}: {exc}")

meta = data.get("meta", {})
tags = set(meta.get("allowedTags", ["OBSERVADO", "ESTIMADO", "HIPOTESE", "DESCONHECIDA", "INFERIDA", "COMPROVADA"]))
confs = set(meta.get("allowedConfidence", ["ALTA", "MEDIA", "BAIXA"]))
errors, warns = [], []
hex_re = re.compile(r"^#(?:[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6}|[0-9A-Fa-f]{8})$")
ref_re = re.compile(r"^\{([^{}]+)\}$")


def lookup(path_str):
    cur = data
    for part in path_str.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            return None
    return cur


def walk(node, trail):
    if isinstance(node, dict):
        if "tag" in node and node["tag"] not in tags:
            errors.append(f"{trail}: tag '{node['tag']}' fora de {sorted(tags)}")
        if "confidence" in node and node["confidence"] not in confs:
            errors.append(f"{trail}: confidence '{node['confidence']}' fora de {sorted(confs)}")
        for k, v in node.items():
            walk(v, f"{trail}.{k}" if trail else k)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, f"{trail}[{i}]")
    elif isinstance(node, str):
        m = ref_re.match(node)
        if m and lookup(m.group(1)) is None:
            errors.append(f"{trail}: referência {node} não resolve")
        if node.startswith("#") and not hex_re.match(node):
            errors.append(f"{trail}: HEX inválido '{node}'")


walk(data, "")
for section in ("color", "typography", "spacing"):
    if section not in data:
        warns.append(f"seção '{section}' ausente")
print(f"Arquivo: {path}")
for w in warns:
    print("AVISO:", w)
for e in errors:
    print("ERRO:", e)
print("RESULTADO:", "OK" if not errors else f"{len(errors)} erro(s)")
sys.exit(1 if errors else 0)
