# VISUAL REFERENCE INTELLIGENCE

Kit para configurar um **Claude Project** especializado em engenharia reversa visual e reprodução de interfaces 1:1, com scripts de apoio, pacote de entrega para o Claude Code e kit de testes. Você envia imagens, screenshots e vídeos; o Claude analisa, documenta e, **só com sua autorização**, implementa e valida.

Versão: ver `CHANGELOG.md` · Licença: MIT

![CI](https://github.com/pedrohen-lopes/VISUAL-REFERENCE-INTELLIGENCE/workflows/CI/badge.svg)

## 🎯 O que ele faz (em 1 diagrama)

```mermaid
flowchart TD
    A[📸 Você envia imagem/video] --> B[/analisar]
    B --> C[Análise forense: regiões, OCR, cores, tipografia, espaçamentos, estrutura]
    C --> D[/especificar]
    D --> E[Gera spec/: specification.md, requirements.md, tokens.json, regions.json]
    E --> F{🤝 Autorização explícita?}
    F -->|Não| G[Aguardar "Autorizo" / "pode implementar" / /implementar]
    F -->|Sim| H[/implementar]
    H --> I[Implementa em 10 etapas: estrutura → layout → tipografia → cores → assets → componentes → animações → responsividade → refinamento → validação]
    I --> J[/validar]
    J --> K[Screenshot Playwright + Diff por região + Heatmap + Overlay + Side-by-side]
    K --> L[Relatório por categoria: estrutural, geométrica, tipográfica, cromática, assets, animações, responsividade, funcionalidade]
    L --> M{✅ Aprovado?}
    M -->|Divergências| N[Corrige prioridade: Crítica → Alta → Média → Baixa<br/>Máx 5 ciclos]
    M -->|Sim| O[🎉 Entregue: observado · estimado · implementado · testado · não validado · limitações]
    N --> J
```

## 🔍 O que a validação produz

| Saída | Descrição |
|-------|-----------|
| **Heatmap** | Vermelho = pixels divergentes (tolerância ±8/255 por canal) |
| **Overlay** | Referência + resultado 50% transparência |
| **Side-by-side** | Referência \| Resultado para inspeção visual |
| **report.json** | % divergência total, por região, SSIM, bounding box das diferenças |

### Exemplo real (landing_ref.png vs landing_result.png — 3 diferenças plantadas)

```mermaid
flowchart LR
    A[landing_ref.png] --> C[image_diff.py]
    B[landing_result.png] --> C
    C --> D[diff_heatmap.png]
    C --> E[overlay.png]
    C --> F[side_by_side.png]
    C --> G[report.json]
    G --> H{Região B_hero: 2.34% divergente}
    H --> I[Caixa da divergência: x=96 y=230 w=704 h=260]
    I --> J[Diferenças detectadas:<br/>• Botão 6px abaixo<br/>• Verde #388E3C vs #2E7D32<br/>• 'Cidade' com C maiúsculo]
```

#### Saídas visuais geradas

| Heatmap (vermelho = divergência) | Overlay (50% ref + 50% resultado) | Side-by-side |
|:---:|:---:|:---:|
| ![Heatmap](docs/diff-example/diff_heatmap.png) | ![Overlay](docs/diff-example/overlay.png) | ![Side-by-side](docs/diff-example/side_by_side.png) |

#### Regiões marcadas

![Regiões](docs/diff-example/regions_marked.png)

## Estrutura
| Pasta/arquivo | Função |
|---|---|
| `CLAUDE_PROJECT_INSTRUCTIONS.md` | Instruções principais (copiar e colar no Project). Enxutas: regras de ouro, fluxo, portão de autorização. |
| `instructions/` | Base de conhecimento: `STANDARDS` (números e definições), `SHORTCUTS`, `CORE_IDENTITY`, `VISUAL_ANALYSIS`, `PIXEL_PERFECT`, `MOTION_ANALYSIS`, `DESIGN_SYSTEM_EXTRACTION`, `ASSET_ANALYSIS`, `RESPONSIVE_ANALYSIS`, `IMPLEMENTATION`, `VISUAL_QA`. |
| `templates/` | Modelos dos entregáveis (análise, especificação, tokens JSON, inventário, prompt, critérios, relatório). |
| `examples/` | `EXAMPLE_WORKFLOW` (sessão completa) e `SIMULATIONS` (revisão e simulações). |
| `tools/` | Scripts Python de apoio (veja `tools/README.md`). |
| `claude-code-handoff/` | Pacote para o Claude Code: `CLAUDE.md` e comandos `/analisar`, `/especificar`, `/implementar`, `/validar`. |
| `tests/` | Imagens sintéticas com gabarito, autoteste e prompts de teste (veja `tests/TEST_KIT.md`). |

## 📦 Duas formas de usar

```mermaid
flowchart TD
    subgraph Project [Claude Web — Project]
        P1[Criar Project]
        P2[Colar CLAUDE_PROJECT_INSTRUCTIONS.md nas Instructions]
        P3[Anexar instructions/, templates/, examples/ como Knowledge]
        P4[Usar: anexar imagem → /analisar → /especificar → autorizar → /implementar → /validar]
    end

    subgraph Code [Claude Code — Local]
        C1[python3 tools/make_handoff.py --target ../meu-projeto]
        C2[Gera: CLAUDE.md, .claude/commands/, tools/, spec/]
        C3[Abrir Claude Code na pasta do projeto]
        C4[Usar: /analisar → /especificar → /implementar → /validar]
    end

    style Project fill:#e8f5e9,stroke:#2e7d32
    style Code fill:#e3f2fd,stroke:#1565c0
```

### Instalação no Claude Project (Web)
1. Crie um **Project** e cole `CLAUDE_PROJECT_INSTRUCTIONS.md` nas **Instructions**
2. Como **Knowledge**, anexe: `instructions/`, `templates/`, `examples/`
3. (Opcional) Anexe `tools/` se seu ambiente executar Python
4. Use: anexe imagem → `/analisar` → `/especificar` → **autorize explicitamente** → `/implementar` → `/validar`

> `tools/`, `tests/`, `claude-code-handoff/` são para uso local/repo; **não** precisam ir no Project.

### Uso com o Claude Code (Local)
```bash
python3 tools/make_handoff.py --target ../meu-projeto
```
Gera na pasta do seu projeto:
- `CLAUDE.md` — regras de implementação
- `.claude/commands/` — `/analisar`, `/especificar`, `/implementar`, `/validar`
- `tools/` — 12 scripts essenciais
- `spec/` — templates prontos (specification.md, tokens.json, etc.)
- `references/`, `assets/`, `reports/` — pastas de trabalho

Detalhes em `claude-code-handoff/README.md`.

## Fluxo recomendado (igual nos dois)
`/analisar` → responder perguntas → `/especificar` → **autorizar explicitamente** (`/implementar`) → `/validar`. **Nada é programado sem autorização válida.**

## 🔧 10 Etapas de implementação (ordem fixa)

```mermaid
flowchart TD
    S1[1. Estrutura e geometria] --> S2[2. Layout e posicionamento]
    S2 --> S3[3. Tipografia]
    S3 --> S4[4. Cores e identidade visual]
    S4 --> S5[5. Imagens e assets]
    S5 --> S6[6. Componentes]
    S6 --> S7[7. Animações e efeitos]
    S7 --> S8[8. Responsividade]
    S8 --> S9[9. Refinamento visual]
    S9 --> S10[10. Validação final]
    style S10 fill:#fff3e0,stroke:#ef6c00
```

Cada etapa só avança quando a anterior passa na validação visual.

## 🏷️ Sistema de tags (rastreabilidade obrigatória)

| Tag | Quando usar | Exemplo |
|-----|-------------|---------|
| `[OBSERVADO]` | Medido direto na imagem nítida | `raio: 12px [OBSERVADO] ALTA` |
| `[ESTIMADO]` | Medido com margem (imagem comprimida/@2x) | `cor: #2E7D32 [ESTIMADO] ±3 MÉDIA` |
| `[HIPÓTESE]` | Não visível, deduzido (hover, animação) | `hover: scale(1.02) [HIPÓTESE] BAIXA` |
| `[DESCONHECIDA]` | Sem evidência nenhuma (imagem estática) | `animação de entrada [DESCONHECIDA]` |
| `[INFERIDA]` | Estrutura técnica deduzida (HTML/JS) | `componente: Button [INFERIDA] MÉDIA` |
| `[COMPROVADA]` | Confirmada por evidência direta (DevTools, Figma, código) | `fonte: Inter [COMPROVADA] ALTA` |

**Confiança**: ALTA ≥ 90% · MÉDIA 60–89% · BAIXA < 60%

## 📊 Categorias de avaliação final

```mermaid
pie title Avaliação por categoria (sem notas numéricas)
    "Estrutural" : 1
    "Geométrica" : 1
    "Tipográfica" : 1
    "Cromática" : 1
    "Assets" : 1
    "Animações" : 1
    "Responsividade" : 1
    "Funcionalidade" : 1
```

Status por categoria: **Verificada** · **Parcialmente verificada** · **Não verificada** · **Divergente**  
Cada uma traz: evidências + pendências. **Sem notas arbitrárias; sem aprovação sem validação.**

## Testar
No PC: `python3 tests/run_tool_checks.py`. No Project: prompts P1–P8 de `tests/TEST_KIT.md` com as imagens de `tests/samples/`.

## Limitações
- A validação visual automática exige ambiente com navegador (Claude Code ou ferramenta de código); sem isso o Claude entrega checklist manual e não declara conformidade.
- Cores e medidas de imagens comprimidas são estimativas; fontes são identificadas por semelhança.
- Fotos, ilustrações, 3D e Lottie exigem os arquivos originais.
- Estados e animações não visíveis são hipóteses ou desconhecidos.
- Os scripts foram testados em Linux com Python 3.12; no Android/Termux a instalação de Pillow/numpy pode exigir passos extras (use o PC se falhar).
