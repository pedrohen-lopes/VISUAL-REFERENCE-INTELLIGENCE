# VISUAL REFERENCE INTELLIGENCE

![Tests](https://github.com/pedrohen-lopes/VISUAL-REFERENCE-INTELLIGENCE/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.12+-blue.svg)

Kit para configurar um **Claude Project** especializado em engenharia reversa visual e reprodução de interfaces 1:1, com scripts de apoio, pacote de entrega para o Claude Code e kit de testes. Você envia imagens, screenshots e vídeos; o Claude analisa, documenta e, **só com sua autorização**, implementa e valida.

Versão: ver `CHANGELOG.md` · Licença: MIT

## Estrutura
| Pasta/arquivo | Função |
|---|---|
| `CLAUDE_PROJECT_INSTRUCTIONS.md` | Instruções principais (copiar e colar no Project). Enxutas: regras de ouro, fluxo, portão de autorização. |
| `instructions/` | Base de conhecimento: `STANDARDS` (números e definições), `SHORTCUTS`, `CORE_IDENTITY`, `VISUAL_ANALYSIS`, `PIXEL_PERFECT`, `MOTION_ANALYSIS`, `DESIGN_SYSTEM_EXTRACTION`, `ASSET_ANALYSIS`, `RESPONSIVE_ANALYSIS`, `IMPLEMENTATION`, `VISUAL_QA`. |
| `templates/` | Modelos dos entregáveis (análise, especificação, tokens JSON, inventário, prompt, critérios, relatório, **regiões**). |
| `examples/` | `EXAMPLE_WORKFLOW` (sessão completa), `SIMULATIONS` (revisão e simulações), **`tokens_example.json`** (tokens preenchidos). |
| `tools/` | Scripts Python de apoio (veja `tools/README.md`). |
| `claude-code-handoff/` | Pacote para o Claude Code: `CLAUDE.md` e comandos `/analisar`, `/especificar`, `/implementar`, `/validar`. |
| `tests/` | Imagens sintéticas com gabarito, autoteste e prompts de teste (veja `tests/TEST_KIT.md`). |
| `.github/workflows/ci.yml` | CI: roda testes, lint e validação de templates. |

## Instalação no Claude Project
1. Crie um Project e cole `CLAUDE_PROJECT_INSTRUCTIONS.md` nas instruções.
2. Envie como conhecimento: todos os arquivos de `instructions/`, `templates/` e `examples/`.
3. (Opcional) Envie `tools/` se o seu ambiente tiver ferramenta de código que possa executá-los.
4. Envie suas referências e use os atalhos `/analisar`, `/especificar`, `/implementar`, `/validar`.
`tools/`, `tests/` e `claude-code-handoff/` são para uso local e para o repositório; não são necessários no Project.

## Fluxo recomendado
`/analisar` → responder perguntas → `/especificar` → autorizar (`/implementar`) → `/validar`. Nada é programado sem autorização válida.

## Uso com o Claude Code
`python3 tools/make_handoff.py --target ../meu-projeto` monta a pasta com `CLAUDE.md`, comandos, scripts e modelos de `spec/`. Detalhes em `claude-code-handoff/README.md`.

## Testar
No PC: `python3 tests/run_tool_checks.py`. No Project: prompts P1–P8 de `tests/TEST_KIT.md` com as imagens de `tests/samples/`.

## Limitações
- A validação visual automática exige ambiente com navegador (Claude Code ou ferramenta de código); sem isso o Claude entrega checklist manual e não declara conformidade.
- Cores e medidas de imagens comprimidas são estimativas; fontes são identificadas por semelhança.
- Fotos, ilustrações, 3D e Lottie exigem os arquivos originais.
- Estados e animações não visíveis são hipóteses ou desconhecidos.
- Os scripts foram testados em Linux com Python 3.12; no Android/Termux a instalação de Pillow/numpy pode exigir passos extras (use o PC se falhar).

## Contribuindo
Veja `CONTRIBUTING.md`.

## Segurança
Veja `SECURITY.md`.