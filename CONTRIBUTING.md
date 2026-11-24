# Contribuindo

Obrigado por contribuir com o **Visual Reference Intelligence**!

## Como rodar os testes

```bash
# Verifica ambiente
python3 tools/check_env.py

# Teste completo dos scripts
python3 tests/run_tool_checks.py

# Valida templates JSON
python3 tools/validate_tokens.py templates/DESIGN_TOKENS_TEMPLATE.json
python3 -c "import json; json.load(open('templates/REGIONS_TEMPLATE.json'))"
```

## Lint e formatação

```bash
pip install ruff
ruff check tools/ tests/
ruff format tools/ tests/
```

## Padrão de commits

Usamos **Conventional Commits**:

```
feat: adiciona nova funcionalidade
fix: corrige bug
docs: atualiza documentação
refactor: refatora código sem mudar comportamento
test: adiciona ou atualiza testes
chore: manutenção (deps, config, etc)
```

Exemplo: `feat: adiciona template de regiões para image_diff`

## Adicionando instruções

1. Crie o arquivo em `instructions/NOME.md`
2. Atualize `CLAUDE_PROJECT_INSTRUCTIONS.md` se necessário (seção 8)
3. Adicione template correspondente em `templates/` se fizer sentido

## Pull Requests

- Rode `python3 tests/run_tool_checks.py` antes de abrir
- Descreva o que muda e por quê
- Um commit por mudança lógica (ou squash no merge)