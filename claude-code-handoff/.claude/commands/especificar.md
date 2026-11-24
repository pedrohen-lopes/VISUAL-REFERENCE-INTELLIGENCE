---
description: Gera/atualiza spec/ (especificação, requisitos, tokens, inventário, critérios) sem implementar
---
Gere ou atualize a especificação em `spec/` a partir da análise: $ARGUMENTS

Crie `spec/specification.md`, `spec/requirements.md` (REQ-### com origem e status), `spec/tokens.json` (valide com `python3 tools/validate_tokens.py spec/tokens.json`), `spec/components.md`, `spec/acceptance.md` e `spec/regions.json` (nome -> [x,y,w,h]). Rotule [INFERIDA]/[COMPROVADA]. Não escreva código de implementação. Termine pedindo autorização explícita para implementar.
