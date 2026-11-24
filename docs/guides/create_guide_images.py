#!/usr/bin/env python3
"""Gera imagens ilustrativas para o guia passo a passo do README."""
from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "guides")
os.makedirs(OUT_DIR, exist_ok=True)

# Cores
BG = "#0d1117"
CARD = "#161b22"
ACCENT_GREEN = "#2ea04f"
ACCENT_BLUE = "#58a6ff"
ACCENT_ORANGE = "#d29922"
TEXT = "#e6edf3"
TEXT_MUTED = "#8b949e"
BORDER = "#30363d"
WHITE = "#ffffff"

def get_font(size=16, bold=False):
    """Tenta carregar fonte do sistema."""
    try:
        if bold:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
        return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size)
    except:
        return ImageFont.load_default()

def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=2):
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def create_step_image(step_num, title, description, details, color, filename, width=900, height=500):
    """Cria uma imagem de passo ilustrativo."""
    img = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(img)

    font_title = get_font(28, bold=True)
    font_desc = get_font(18)
    font_detail = get_font(14)
    font_num = get_font(48, bold=True)
    font_small = get_font(12)

    # Número do passo (círculo)
    circle_x, circle_y = 60, 60
    draw.ellipse([circle_x, circle_y, circle_x+80, circle_y+80], fill=color, outline=WHITE, width=3)
    draw.text((circle_x+25, circle_y+15), str(step_num), fill=WHITE, font=font_num)

    # Título
    draw.text((170, 60), title, fill=WHITE, font=font_title)

    # Linha decorativa
    draw.line([(170, 105), (width-60, 105)], fill=color, width=3)

    # Descrição
    draw.text((170, 120), description, fill=TEXT, font=font_desc)

    # Detalhes (bullet points)
    y = 170
    for detail in details:
        # Bullet
        draw.ellipse([170, y+6, 182, y+18], fill=color)
        draw.text((195, y), detail, fill=TEXT_MUTED, font=font_detail)
        y += 35

    # Card ilustrativo à direita
    card_x = width - 380
    card_y = 130
    card_w = 340
    card_h = 320
    draw_rounded_rect(draw, (card_x, card_y, card_x+card_w, card_y+card_h), 12, CARD, BORDER)

    # Texto no card
    draw.text((card_x+20, card_y+20), "📋 O que você vê", fill=ACCENT_GREEN, font=font_desc)
    draw.line([(card_x+20, card_y+55), (card_x+card_w-20, card_y+55)], fill=BORDER, width=1)

    # Simular UI do Claude
    ui_items = [
        ("🔧", "Settings / Instructions"),
        ("📁", "Knowledge (arquivos)"),
        ("💬", "Chat com /analisar"),
        ("✅", "Botão Autorizar"),
        ("📊", "Relatório final"),
    ]
    for i, (icon, label) in enumerate(ui_items):
        iy = card_y + 70 + i * 45
        draw.text((card_x+25, iy), icon, fill=ACCENT_BLUE, font=get_font(20))
        draw.text((card_x+55, iy), label, fill=TEXT, font=font_detail)

    # Rodapé
    draw.text((60, height-40), "VISUAL REFERENCE INTELLIGENCE  •  Guia visual", fill=TEXT_MUTED, font=font_small)

    img.save(os.path.join(OUT_DIR, filename), quality=95)
    print(f"Criado: {filename}")

# ===== GUIA 1: CLAUDE PROJECT (WEB) =====
create_step_image(
    1, "Criar Project novo",
    "Acesse claude.ai → Projects → Create Project",
    [
        "Nome: 'VRI - Minha Interface'",
        "Descrição: 'Engenharia reversa visual 1:1'",
        "Clique em Create Project",
    ],
    ACCENT_GREEN, "guide-project-01-create.png"
)

create_step_image(
    2, "Colar Instruções",
    "Aba Instructions → cole CLAUDE_PROJECT_INSTRUCTIONS.md",
    [
        "Copie TODO o conteúdo do arquivo",
        "Cole na caixa Instructions do Project",
        "Salve (auto-save)",
    ],
    ACCENT_GREEN, "guide-project-02-instructions.png"
)

create_step_image(
    3, "Anexar Knowledge",
    "Aba Knowledge → Upload files → selecione 3 pastas",
    [
        "instructions/ (11 arquivos .md)",
        "templates/ (7 arquivos)",
        "examples/ (2 arquivos)",
        "Arraste as pastas inteiras de uma vez",
    ],
    ACCENT_BLUE, "guide-project-03-knowledge.png"
)

create_step_image(
    4, "Usar: anexar imagem + /analisar",
    "No chat do Project: arraste screenshot → digite /analisar",
    [
        "Anexe: screenshot, mockup, foto ou vídeo",
        "Digite: /analisar (ou clique no comando)",
        "VRI responde com análise + perguntas (máx 7)",
    ],
    ACCENT_ORANGE, "guide-project-04-analyze.png"
)

create_step_image(
    5, "Responder → /especificar → Autorizar → /implementar → /validar",
    "Fluxo completo: responda perguntas → gere spec → autorize → implemente → valide",
    [
        "Responda as perguntas (ou use padrões)",
        "Digite: /especificar → gera spec/ completo",
        'Digite: "Autorizo" ou /implementar',
        "Digite: /validar → diff + relatório 8 categorias",
    ],
    ACCENT_GREEN, "guide-project-05-full-flow.png"
)

# ===== GUIA 2: CLAUDE CODE (LOCAL) =====
create_step_image(
    1, "Gerar handoff local",
    "Terminal: python3 tools/make_handoff.py --target ../meu-projeto",
    [
        "Rode na raiz do repo VRI",
        "Cria pasta com CLAUDE.md + comandos + tools + spec/",
        "Se já tem imagens em references/, gera regions.json auto",
    ],
    ACCENT_BLUE, "guide-code-01-handoff.png"
)

create_step_image(
    2, "Abrir no Claude Code",
    "cd ../meu-projeto && claude",
    [
        "Abre Claude Code na pasta do projeto",
        "Detecta CLAUDE.md e .claude/commands/ automaticamente",
        "Comandos disponíveis: /analisar /especificar /implementar /validar",
    ],
    ACCENT_BLUE, "guide-code-02-open.png"
)

create_step_image(
    3, "Colar referências + /analisar",
    "Arraste imagens para references/ → /analisar",
    [
        "cp seus-screenshots.png references/",
        "Digite: /analisar",
        "VRI analisa, faz perguntas, documenta tudo",
    ],
    ACCENT_ORANGE, "guide-code-03-analyze.png"
)

create_step_image(
    4, "Autorizar + /implementar + /validar",
    "'Autorizo' → /implementar → /validar (Playwright + diff)",
    [
        "Responda perguntas → /especificar",
        'Digite: "Autorizo" → /implementar (10 etapas)',
        "Digite: /validar → screenshot + diff + relatório",
        "Máx 5 ciclos de correção automática",
    ],
    ACCENT_GREEN, "guide-code-04-implement-validate.png"
)

# ===== DIAGRAMAS MERMAID CORRIGIDOS (SVG) =====
def create_mermaid_svg(name, mermaid_code, filename):
    """Salva código Mermaid para referência (GitHub renderiza nativo)."""
    path = os.path.join(OUT_DIR, filename)
    with open(path, "w") as f:
        f.write(mermaid_code)
    print(f"Mermaid salvo: {filename}")

# Fluxo principal (sem emojis nos labels, subgraphs simples)
create_mermaid_svg("flow-main", """flowchart TD
    A[Entrada: Imagem ou Video] --> B[Fase 0: Metadados]
    B --> C[Fase 1: Perguntas max 7]
    C --> D[Fase 2: Analise Forense]
    D --> E[spec/specification.md]
    D --> F[spec/requirements.md]
    D --> G[spec/tokens.json]
    D --> H[spec/regions.json]
    D --> I[spec/components.md]
    D --> J[spec/acceptance.md]
    E --> K{Autorizacao Explicita?}
    F --> K
    G --> K
    H --> K
    I --> K
    J --> K
    K -->|Nao| L[Aguardar: Autorizo / pode implementar /implementar]
    K -->|Sim| M[Implementacao: 10 etapas]
    M --> N[Validacao: Playwright + Diff]
    N --> O[Heatmap + Overlay + Side-by-side]
    O --> P[Relatorio 8 categorias]
    P --> Q{Divergencias?}
    Q -->|Sim| N
    Q -->|Nao| R[Entrega: Verificada/Parcial/Nao verificada/Divergente]
""", "mermaid-flow-main.mmd")

# Project vs Code
create_mermaid_svg("flow-install", """flowchart LR
    subgraph PROJECT[Claude Web Project]
        P1[1. Criar Project]
        P2[2. Colar Instructions]
        P3[3. Anexar Knowledge: instructions templates examples]
        P4[4. Usar: imagem + /analisar]
        P1 --> P2 --> P3 --> P4
    end

    subgraph CODE[Claude Code Local]
        C1[make_handoff.py --target]
        C2[Gera: CLAUDE.md commands tools spec]
        C3[cd projeto && claude]
        C4[Usar: /analisar /especificar /implementar /validar]
        C1 --> C2 --> C3 --> C4
    end
""", "mermaid-install.mmd")

# 10 etapas
create_mermaid_svg("flow-steps", """flowchart TD
    S1[1. Estrutura e Geometria] --> S2[2. Layout e Posicionamento]
    S2 --> S3[3. Tipografia]
    S3 --> S4[4. Cores e Identidade]
    S4 --> S5[5. Imagens e Assets]
    S5 --> S6[6. Componentes]
    S6 --> S7[7. Animacoes e Efeitos]
    S7 --> S8[8. Responsividade]
    S8 --> S9[9. Refinamento Visual]
    S9 --> S10[10. Validacao Final]
""", "mermaid-steps.mmd")

print("\n✅ Todas as imagens e diagramas criados em docs/guides/")