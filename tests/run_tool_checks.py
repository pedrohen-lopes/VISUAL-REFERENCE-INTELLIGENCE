#!/usr/bin/env python3
"""Autoteste dos scripts de tools/ contra as imagens sintéticas e o gabarito. Uso: python3 run_tool_checks.py"""
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(os.path.dirname(HERE), "tools")
S = os.path.join(HERE, "samples")
truth = json.load(open(os.path.join(S, "ground_truth.json"), encoding="utf-8"))
results = []


def run(script, *args):
    return subprocess.run([sys.executable, os.path.join(TOOLS, script), *args], capture_output=True, text=True)


def check(name, cond, detail=""):
    results.append(("PASS" if cond else "FAIL", name, detail))


def skip(name, why):
    results.append(("SKIP", name, why))


tmp = tempfile.mkdtemp()
land = os.path.join(S, "landing_ref.png")

r = run("image_info.py", os.path.join(S, "dashboard_ref.png"))
check("image_info detecta viewport 1920 @1x", "@1x -> viewport 1920px" in r.stdout, r.stdout[-120:])

r = run("sample_colors.py", land, "--region", "810,150,100,100", "--json")
try:
    got = json.loads(r.stdout.split("\n# Tag")[0])["regions"][0]["hex"]
except Exception:
    got = "?"
check("sample_colors lê a cor da imagem do hero", got == truth["landing_ref.png"]["cores"]["imagem_hero"], got)

regs = os.path.join(tmp, "regions.json")
json.dump(truth["landing_ref.png"]["regioes"], open(regs, "w"))
out = os.path.join(tmp, "diff")
r = run("image_diff.py", land, os.path.join(S, "landing_result.png"), "--regions-file", regs, "--out", out)
rep = json.load(open(os.path.join(out, "report.json"), encoding="utf-8"))
by = {x["regiao"]: x for x in rep["regioes"]}
check("image_diff localiza a diferença na região B_hero", by["B_hero"]["divergente_pct"] > 0)
check("image_diff não acusa regiões sem diferença", all(by[k]["divergente_pct"] == 0 for k in ("A_header", "C_cards", "D_footer")))
check("image_diff gera heatmap, overlay e lado a lado", all(os.path.exists(os.path.join(out, f)) for f in ("diff_heatmap.png", "overlay.png", "side_by_side.png")))

r = run("validate_tokens.py", os.path.join(os.path.dirname(HERE), "templates", "DESIGN_TOKENS_TEMPLATE.json"))
check("validate_tokens aprova o template", r.returncode == 0, r.stdout[-80:])
bad = os.path.join(tmp, "bad.json")
json.dump({"meta": {}, "color": {"semantic": {"x": {"value": "#ZZZ123", "tag": "TALVEZ", "confidence": "ALTA"}}}, "typography": {}, "spacing": {}}, open(bad, "w"))
r = run("validate_tokens.py", bad)
check("validate_tokens reprova tag e HEX inválidos", r.returncode == 1 and "HEX inválido" in r.stdout and "tag" in r.stdout)

r = run("crop_regions.py", land, "--region", "botao=96,420,240,64", "--out", os.path.join(tmp, "crops"))
check("crop_regions recorta 240x64", "240x64" in r.stdout, r.stdout.strip())

if shutil.which("tesseract"):
    r = run("ocr_text.py", land, "--region", "96,400,300,100")
    check("ocr_text lê 'Reservar' no botão", "reservar" in r.stdout.lower(), r.stdout.strip()[:80])
else:
    skip("ocr_text", "tesseract ausente")

r = run("screenshot.py", "--check")
if "OK" in r.stdout:
    page = os.path.join(tmp, "t.html")
    open(page, "w").write("<html><body style='margin:0;background:#123456'></body></html>")
    shot = os.path.join(tmp, "s.png")
    r2 = run("screenshot.py", page, "--viewport", "390x844", "--scale", "2", "--out", shot)
    check("screenshot gera 780x1688", r2.returncode == 0 and os.path.exists(shot), r2.stderr[-80:])
else:
    skip("screenshot", "Playwright/Chromium indisponível")

for st, name, d in results:
    print(f"[{st}] {name}" + (f"  ({d})" if st == "FAIL" and d else (f"  - {d}" if st == "SKIP" else "")))
fails = [x for x in results if x[0] == "FAIL"]
print(f"\n{len(results) - len(fails)} ok/ignorados, {len(fails)} falha(s).")
shutil.rmtree(tmp, ignore_errors=True)
sys.exit(1 if fails else 0)
