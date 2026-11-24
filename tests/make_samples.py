#!/usr/bin/env python3
"""Gera imagens de referência SINTÉTICAS com gabarito exato (ground truth) para testar o projeto e os scripts.
Uso: python3 make_samples.py   (cria samples/*.png e samples/*.json). Requer Pillow."""
import json
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "samples")
os.makedirs(OUT, exist_ok=True)


def font(size, bold=False):
    names = ["DejaVuSans-Bold.ttf", "DejaVuSans.ttf"] if bold else ["DejaVuSans.ttf"]
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except Exception:
            pass
    return ImageFont.load_default()


def centered(d, box, text, f, fill):
    x, y, w, h = box
    l, t, r, b = d.textbbox((0, 0), text, font=f)
    d.text((x + (w - (r - l)) / 2 - l, y + (h - (b - t)) / 2 - t), text, font=f, fill=fill)


def landing(variant="ref"):
    mod = variant == "result"
    img = Image.new("RGB", (1440, 900), "#FFF8F0")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 1439, 79], fill="#FFFFFF")
    d.line([(0, 79), (1439, 79)], fill="#E8DCCB", width=1)
    d.text((48, 24), "Aurora Café", font=font(28, True), fill="#3B2A20")
    for i, t in enumerate(["Cardápio", "Horários", "Sobre", "Contato"]):
        d.text((880 + i * 130, 28), t, font=font(18), fill="#5A463A")
    d.rectangle([0, 80, 1439, 639], fill="#F3E3CF")
    d.text((96, 220), "Café que acorda a cidade" if not mod else "Café que acorda a Cidade", font=font(54, True), fill="#3B2A20")
    d.text((96, 330), "Grãos selecionados, torra artesanal e pão quente todas as manhãs.", font=font(22), fill="#6B5547")
    by = 420 + (6 if mod else 0)
    d.rounded_rectangle([96, by, 335, by + 63], radius=32, fill="#2E7D32" if not mod else "#388E3C")
    centered(d, (96, by, 240, 64), "Reservar mesa", font(22, True), "#FFFFFF")
    d.rounded_rectangle([800, 140, 1343, 619], radius=24, fill="#C9A27A")
    d.line([(800, 140), (1343, 619)], fill="#B58B62", width=2)
    d.line([(1343, 140), (800, 619)], fill="#B58B62", width=2)
    for i, t in enumerate(["Espresso", "Pão de queijo", "Bolo do dia"]):
        x = 96 + i * 424
        d.rounded_rectangle([x, 660, x + 399, 799], radius=16, fill="#FFFFFF", outline="#E8DCCB", width=1)
        d.text((x + 24, 690), t, font=font(24, True), fill="#3B2A20")
        d.text((x + 24, 738), "Feito na hora", font=font(16), fill="#6B5547")
    d.rectangle([0, 820, 1439, 899], fill="#3B2A20")
    d.text((96, 850), "© 2026 Aurora Café", font=font(18), fill="#F3E3CF")
    return img


def dashboard():
    img = Image.new("RGB", (1920, 1080), "#F3F4F6")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 239, 1079], fill="#111827")
    d.text((32, 28), "DashPro", font=font(26, True), fill="#FFFFFF")
    for i, t in enumerate(["Visão geral", "Vendas", "Clientes", "Relatórios", "Ajustes"]):
        y = 120 + i * 56
        if i == 0:
            d.rounded_rectangle([16, y - 8, 223, y + 36], radius=8, fill="#1F2937")
        d.text((40, y), t, font=font(18), fill="#E5E7EB" if i == 0 else "#9CA3AF")
    d.rectangle([240, 0, 1919, 71], fill="#FFFFFF")
    d.line([(240, 71), (1919, 71)], fill="#E5E7EB", width=1)
    d.text((280, 22), "Visão geral", font=font(24, True), fill="#111827")
    kpis = [("Receita", "R$ 128.400"), ("Pedidos", "1.284"), ("Clientes", "342"), ("Conversão", "3,8%")]
    for i, (a, b) in enumerate(kpis):
        x = 280 + i * 408
        d.rounded_rectangle([x, 112, x + 375, 231], radius=12, fill="#FFFFFF")
        d.text((x + 24, 136), a, font=font(16), fill="#6B7280")
        d.text((x + 24, 170), b, font=font(32, True), fill="#111827")
    d.rounded_rectangle([280, 264, 1259, 683], radius=12, fill="#FFFFFF")
    d.text((304, 284), "Receita mensal", font=font(18, True), fill="#111827")
    line_vals = [40, 55, 48, 70, 65, 90, 85, 110, 100, 130, 125, 150]
    pts = [(320 + i * 82, 650 - v * 2) for i, v in enumerate(line_vals)]
    d.line(pts, fill="#2563EB", width=3)
    for p in pts:
        d.ellipse([p[0] - 5, p[1] - 5, p[0] + 5, p[1] + 5], fill="#2563EB")
    d.rounded_rectangle([1292, 264, 1879, 683], radius=12, fill="#FFFFFF")
    d.text((1316, 284), "Pedidos por canal", font=font(18, True), fill="#111827")
    bar_vals = [320, 210, 150, 90]
    for i, v in enumerate(bar_vals):
        x = 1340 + i * 130
        d.rectangle([x, 650 - v, x + 80, 650], fill="#10B981")
    d.rounded_rectangle([280, 716, 1879, 1035], radius=12, fill="#FFFFFF")
    for j, t in enumerate(["Pedido", "Cliente", "Valor", "Status"]):
        d.text((304 + j * 380, 736), t, font=font(16, True), fill="#6B7280")
    d.line([(280, 772), (1879, 772)], fill="#E5E7EB", width=1)
    rows = [("#1042", "Ana Souza", "R$ 320,00", "Pago"), ("#1041", "Bruno Lima", "R$ 89,90", "Pendente"),
            ("#1040", "Carla Dias", "R$ 540,00", "Pago"), ("#1039", "Diego Rocha", "R$ 75,00", "Cancelado")]
    for i, r in enumerate(rows):
        for j, t in enumerate(r):
            d.text((304 + j * 380, 792 + i * 56), t, font=font(16), fill="#111827")
        d.line([(280, 836 + i * 56), (1879, 836 + i * 56)], fill="#F3F4F6", width=1)
    return img


landing("ref").save(os.path.join(OUT, "landing_ref.png"))
landing("result").save(os.path.join(OUT, "landing_result.png"))
dashboard().save(os.path.join(OUT, "dashboard_ref.png"))

truth = {
    "landing_ref.png": {
        "viewport_css_px": [1440, 900], "escala": 1,
        "regioes": {"A_header": [0, 0, 1440, 80], "B_hero": [0, 80, 1440, 560], "C_cards": [0, 640, 1440, 180], "D_footer": [0, 820, 1440, 80]},
        "cores": {"fundo_pagina": "#FFF8F0", "header": "#FFFFFF", "hero": "#F3E3CF", "botao": "#2E7D32", "footer": "#3B2A20", "imagem_hero": "#C9A27A"},
        "elementos": {"botao_reservar": {"box": [96, 420, 240, 64], "raio": 32, "texto": "Reservar mesa"},
                      "imagem_hero": {"box": [800, 140, 544, 480], "raio": 24},
                      "cards": [[96, 660, 400, 140], [520, 660, 400, 140], [944, 660, 400, 140]]},
        "textos": ["Aurora Café", "Cardápio", "Horários", "Sobre", "Contato", "Café que acorda a cidade",
                   "Grãos selecionados, torra artesanal e pão quente todas as manhãs.", "Reservar mesa",
                   "Espresso", "Pão de queijo", "Bolo do dia", "Feito na hora", "© 2026 Aurora Café"],
        "animacoes": "DESCONHECIDAS (imagem estática)",
        "estados_sem_evidencia": ["hover do botão", "menu mobile", "header fixo"],
    },
    "landing_result.png": {
        "diferencas_inseridas": ["botão deslocado 6 px para baixo (y 426)", "cor do botão #388E3C em vez de #2E7D32", "título com 'C' maiúsculo em 'Cidade' (capitalização alterada)"],
        "regiao_esperada_do_erro": "B_hero",
    },
    "dashboard_ref.png": {
        "viewport_css_px": [1920, 1080], "escala": 1,
        "regioes": {"A_sidebar": [0, 0, 240, 1080], "B_topbar": [240, 0, 1680, 72], "C_kpis": [280, 112, 1600, 120],
                    "D_grafico_linha": [280, 264, 980, 420], "E_grafico_barras": [1292, 264, 588, 420], "F_tabela": [280, 716, 1600, 320]},
        "cores": {"sidebar": "#111827", "fundo": "#F3F4F6", "card": "#FFFFFF", "linha_grafico": "#2563EB", "barras": "#10B981"},
        "dados_reais_grafico_linha": [40, 55, 48, 70, 65, 90, 85, 110, 100, 130, 125, 150],
        "dados_reais_barras": [320, 210, 150, 90],
        "nota_dados": "Na imagem os valores só podem ser ESTIMADOS pela altura; o gabarito existe para medir o erro da estimativa.",
        "textos": ["DashPro", "Visão geral", "Vendas", "Clientes", "Relatórios", "Ajustes", "Receita", "R$ 128.400", "Pedidos", "1.284",
                   "Clientes", "342", "Conversão", "3,8%", "Receita mensal", "Pedidos por canal", "Pedido", "Cliente", "Valor", "Status"],
        "animacoes": "DESCONHECIDAS (imagem estática)",
        "estados_sem_evidencia": ["tooltip dos gráficos", "hover das linhas da tabela", "filtros", "sidebar recolhida"],
    },
}
with open(os.path.join(OUT, "ground_truth.json"), "w", encoding="utf-8") as fh:
    json.dump(truth, fh, ensure_ascii=False, indent=2)
print("Gerado em", OUT)
