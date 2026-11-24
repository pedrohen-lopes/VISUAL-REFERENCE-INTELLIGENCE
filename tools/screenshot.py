#!/usr/bin/env python3
"""Captura screenshot com Playwright (verifica disponibilidade antes)."""
import argparse
import os
import sys

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("target", nargs="?", help="URL ou caminho de arquivo .html")
ap.add_argument("--viewport", default="1440x900", help="LARGURAxALTURA em CSS px")
ap.add_argument("--scale", type=float, default=1.0, help="deviceScaleFactor")
ap.add_argument("--full-page", action="store_true")
ap.add_argument("--wait", type=int, default=500, help="ms de espera após carregar")
ap.add_argument("--freeze-animations", action="store_true", help="desliga animações/transições para comparar estado estático")
ap.add_argument("--out", default="screenshot.png")
ap.add_argument("--check", action="store_true", help="só verifica se Playwright/Chromium funcionam")
args = ap.parse_args()

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("Playwright não instalado: pip install playwright && playwright install chromium")

if not args.check and not args.target:
    sys.exit("Informe a URL/arquivo ou use --check")
try:
    w, h = [int(v) for v in args.viewport.lower().split("x")]
except ValueError:
    sys.exit("Use --viewport 1440x900")

url = args.target
if url and "://" not in url:
    url = "file://" + os.path.abspath(url)

with sync_playwright() as p:
    try:
        browser = p.chromium.launch()
    except Exception as exc:
        sys.exit(f"Chromium indisponível ({exc}). Rode: playwright install chromium")
    if args.check:
        print(f"Playwright OK, Chromium {browser.version}")
        browser.close()
        sys.exit(0)
    ctx = browser.new_context(viewport={"width": w, "height": h}, device_scale_factor=args.scale)
    page = ctx.new_page()
    page.goto(url, wait_until="networkidle")
    if args.freeze_animations:
        page.add_style_tag(content="*,*::before,*::after{animation:none!important;transition:none!important;caret-color:transparent!important}")
    page.wait_for_timeout(args.wait)
    page.screenshot(path=args.out, full_page=args.full_page)
    browser.close()
print(f"Screenshot salvo em {args.out} (viewport {w}x{h} @{args.scale}x => {int(w * args.scale)}x{int(h * args.scale)} px; "
      f"{'página inteira' if args.full_page else 'apenas o viewport'}).")
