# Pacote de entrega para o Claude Code

Leva o resultado do Project (especificação, tokens, assets, critérios) para o Claude Code implementar e validar com disciplina.

## Como usar
1. No Project, gere as entregas (`/especificar`).
2. Crie a pasta do seu projeto e rode, a partir da raiz do kit:
   `python3 tools/make_handoff.py --target ../meu-projeto`
   Isso copia `CLAUDE.md`, os comandos `.claude/commands/`, os scripts `tools/` e cria a estrutura abaixo.
3. Coloque as imagens de referência em `references/`, a especificação em `spec/` e os recortes autorizados em `assets/`.
4. Abra o Claude Code na pasta e rode `/analisar`, depois `/especificar`; só então `/implementar` (com autorização) e `/validar`.

## Estrutura criada
```
meu-projeto/
├── CLAUDE.md                  regras de implementação (portão de autorização, validação)
├── .claude/commands/          /analisar /especificar /implementar /validar
├── tools/                     scripts de apoio (imagem -> texto, diff, screenshot, validação)
├── references/                imagens e vídeos de referência (REF-##, VIDEO-##)
├── spec/
│   ├── specification.md       especificação técnica (modelo em templates/)
│   ├── requirements.md        matriz REQ ↔ REF com status
│   ├── tokens.json            design tokens (validar com tools/validate_tokens.py)
│   ├── components.md          inventário de componentes e assets
│   └── acceptance.md          critérios de aceitação
├── assets/                    assets autorizados (recortes, SVGs, fontes)
└── reports/                   validação: screenshots, diffs, relatório
```

## Importante
- O Claude Code **não lê imagens** em algumas configurações: use `python3 tools/image_report.py references/REF-01.png` para obter um relatório textual (paleta, faixas, mapa de cores, OCR). É auxiliar e [ESTIMADO]; a análise visual continua sendo feita no Project.
- Os comandos e o `CLAUDE.md` não substituem a autorização do usuário.

modelo usado, nemotron

