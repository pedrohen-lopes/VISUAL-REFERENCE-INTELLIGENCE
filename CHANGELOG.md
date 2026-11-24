# Changelog

Formato: [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [2.0.0] - 2026-11-24
### Adicionado
- `tools/`: 12 scripts (verificação de ambiente, escala/viewport, cores, recortes, grade, OCR, relatório textual de imagem, image diff por região, screenshot com Playwright, extração de quadros, validação de tokens, montagem do pacote de entrega).
- `claude-code-handoff/`: `CLAUDE.md`, comandos `/analisar`, `/especificar`, `/implementar`, `/validar` e README do pacote.
- `tests/`: imagens sintéticas com gabarito, gerador reproduzível, autoteste dos scripts e kit de testes P1–P8.
- `instructions/STANDARDS.md` (fonte única de tolerâncias, gravidade, ordem, IDs e categorias) e `instructions/SHORTCUTS.md` (atalhos).
- `LICENSE` (MIT), `.gitignore`, este changelog.
### Alterado
- `CLAUDE_PROJECT_INSTRUCTIONS.md` reduzido para ~6,7 mil caracteres, com as regras de ouro e o portão de autorização; o detalhe ficou nos arquivos de conhecimento.
- Duplicações de tolerâncias e gravidade substituídas por referências a `STANDARDS.md`.

## [1.2.0] - 2026-11-24
- Revisão de consistência; simulações; regra de autorização reescrita (autorização válida, antecipada, ambígua, escopo).

## [1.1.0] - 2026-11-24
- Análise forense e por regiões, motion quadro a quadro, investigação de assets, múltiplas referências, estrutura [INFERIDA], rastreabilidade REQ, avaliação por categoria.

## [1.0.0] - 2026-11-24
- Estrutura inicial: instruções, templates e exemplo.
