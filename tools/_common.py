"""Funções compartilhadas pelos scripts de tools/. Requer Pillow e numpy."""
import json
import sys

try:
    from PIL import Image
    import numpy as np
except ImportError:
    sys.exit("Faltam dependências: pip install pillow numpy")

COMMON_VIEWPORTS = [
    (360, 800), (375, 667), (375, 812), (390, 844), (393, 852), (412, 915),
    (768, 1024), (820, 1180), (1024, 768), (1280, 720), (1366, 768),
    (1440, 900), (1536, 864), (1920, 1080),
]


def load(path, mode="RGB"):
    try:
        return Image.open(path).convert(mode)
    except Exception as exc:  # arquivo ausente, formato inválido
        sys.exit(f"Não foi possível abrir '{path}': {exc}")


def parse_region(text):
    """'x,y,w,h' -> (x, y, w, h) inteiros."""
    try:
        x, y, w, h = [int(float(v)) for v in text.split(",")]
    except ValueError:
        sys.exit(f"Região inválida '{text}'. Use x,y,w,h (ex.: 0,0,1440,80)")
    return x, y, w, h


def parse_named_region(text):
    """'nome=x,y,w,h' -> (nome, (x,y,w,h))."""
    if "=" not in text:
        sys.exit(f"Use nome=x,y,w,h (recebido '{text}')")
    name, rest = text.split("=", 1)
    return name.strip(), parse_region(rest)


def hex_of(rgb):
    return "#{:02X}{:02X}{:02X}".format(*[int(v) for v in rgb[:3]])


def clamp_box(box, size):
    x, y, w, h = box
    W, H = size
    x0, y0 = max(0, x), max(0, y)
    x1, y1 = min(W, x + w), min(H, y + h)
    return x0, y0, x1, y1


def dump_json(obj, path=None):
    text = json.dumps(obj, ensure_ascii=False, indent=2)
    if path:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
    return text
