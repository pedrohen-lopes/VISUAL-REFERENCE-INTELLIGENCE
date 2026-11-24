# Changelog

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

O formato segue [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/) e este projeto adere a [Semantic Versioning](https://semver.org/lang/pt-BR/).

## [Unreleased]

### Added
- Template `REGIONS_TEMPLATE.json` para `image_diff.py`
- GitHub Actions CI (testes, lint, validação de tokens)
- `.editorconfig` para consistência entre editores
- `CONTRIBUTING.md` e `SECURITY.md`
- Exemplo completo `tokens_example.json` em `examples/`
- Badges no README (tests, license, python)

### Changed
- `make_handoff.py` agora usa `REGIONS_TEMPLATE.json` em vez de formato hardcoded
- Branch padrão renomeada de `master` para `main`

### Fixed
- `spec/regions.json` gerado com estrutura correta esperada por `image_diff.py`

## [0.2.0] - 2026-11-24

### Added
- Kit completo de engenharia reversa visual (VRI)
- 11 arquivos de instruções em `instructions/`
- 7 templates em `templates/`
- 13 scripts Python em `tools/`
- Pacote de entrega para Claude Code (`claude-code-handoff/`)
- Kit de testes com imagens sintéticas (`tests/`)
- Exemplos de fluxo e simulações (`examples/`)

## [0.1.0] - 2026-11-20

### Added
- Estrutura inicial do projeto
- `CLAUDE_PROJECT_INSTRUCTIONS.md` com regras de ouro, fluxo e portão de autorização
- `STANDARDS.md` com tolerâncias, gravidades, ordem de execução e IDs
- Scripts base: `check_env.py`, `image_info.py`, `sample_colors.py`, `crop_regions.py`, `grid_overlay.py`, `ocr_text.py`, `image_report.py`, `image_diff.py`, `screenshot.py`, `extract_frames.py`, `validate_tokens.py`, `make_handoff.py`
- Templates base: especificação, tokens, componentes, critérios de aceitação
- Licença MIT