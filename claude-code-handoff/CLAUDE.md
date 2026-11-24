# CLAUDE.md — Regras para implementação 1:1 guiada por especificação

Você implementa uma interface a partir de `spec/` e `references/`. Seu objetivo é **reproduzir corretamente, não reinventar**.

## Portão de autorização
- Não escreva código de implementação sem `spec/specification.md` e `spec/requirements.md` existentes **e** autorização explícita do usuário nesta sessão ("pode implementar", "autorizo", `/implementar`). Respostas ambíguas não autorizam.
- Autorização vale para a stack e os arquivos listados em `spec/specification.md`. Mudanças fora disso exigem nova autorização.
- Se faltar especificação, execute `/analisar` e `/especificar` primeiro (somente leitura e documentação).

## Fontes de verdade
1. `spec/requirements.md` (REQ ↔ origem) e `spec/specification.md`.
2. `spec/tokens.json` (valide com `python3 tools/validate_tokens.py spec/tokens.json`).
3. `references/` (imagens/vídeos). Se você não consegue ver imagens, use `python3 tools/image_report.py <imagem>` e `python3 tools/ocr_text.py <imagem>`; trate a saída como [ESTIMADO].
Em conflito: a especificação prevalece sobre sua interpretação; pergunte ao usuário em vez de supor.

## Regras de implementação
- Valores exatamente como especificados; não arredonde nem "melhore".
- Textos literais conforme a especificação (capitalização, acentos, símbolos).
- Assets ausentes: `PLACEHOLDER` com dimensões exatas; nunca imagens genéricas sem autorização.
- Estados e animações só se constarem na especificação como evidenciados.
- Ordem de construção: estrutura/geometria → layout → tipografia → cores → assets → componentes → animações/efeitos → responsividade → refinamento → validação.
- Projeto existente: leia antes, reutilize, altere incrementalmente, não remova dependências sem justificar, mantenha `reports/modified-files.md` (arquivo, ação, motivo, REQs).
- Não instale dependências novas sem autorização.

## Verificação de ferramentas
Antes de usar, rode `python3 tools/check_env.py` e use apenas o que estiver OK. Sem Playwright/navegador, não afirme validação visual.

## Validação (obrigatória antes de declarar concluído)
1. `python3 tools/screenshot.py <arquivo-ou-url> --viewport <WxH> --scale <n> --freeze-animations --out reports/result.png`
2. `python3 tools/image_diff.py references/<REF>.png reports/result.png --regions-file spec/regions.json --out reports/diff`
3. Classifique divergências (Crítica, Alta, Média, Baixa), corrija da maior para a menor, repita (máx. 5 ciclos).
4. Escreva `reports/validation-report.md` com: observado · estimado · implementado · testado · não validado · limitações, avaliação por categoria e cobertura de REQs.
Nunca declare "100% fiel" sem evidência; use os limiares de aceitação de `spec/acceptance.md`.
