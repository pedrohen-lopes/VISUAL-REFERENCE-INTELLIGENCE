# VISUAL_QA — Validação Visual e Autocorreção

## Requisitos
Verifique a disponibilidade das ferramentas antes de usá-las (ex.: `npx playwright --version`, navegador headless, Figma/DevTools conectados) e registre o resultado; não presuma instalação.
Ambiente com navegador headless (Playwright/Puppeteer/Chromium) ou preview que permita screenshot. **Sem isso, a validação automática é impossível**: informe ao usuário, entregue o checklist manual e não declare conformidade.

## Procedimento
1. **Preparação:** mesmo viewport e escala (deviceScaleFactor) da referência; mesma fonte carregada; aguardar fim de carregamento e animações; congelar animações quando comparar estado estático.
2. **Captura:** screenshot do resultado (full page ou região correspondente).
3. **Alinhamento:** garanta mesma dimensão em px entre referência e captura; se diferir, redimensione apenas para comparação e registre.
4. **Comparações:**
   - Lado a lado (referência | resultado).
   - Sobreposição com 50% de opacidade.
   - **Image diff:** pixel a pixel (ex.: Pillow `ImageChops.difference`, pixelmatch, odiff ou similar); gere mapa de calor.
5. **Métricas:** % de pixels divergentes (com tolerância declarada, ex.: canal ≤ 8/255), SSIM quando disponível, e medição manual de pontos-chave (posição, tamanho, cor) comparando CSS computado.
6. **Lista de divergências:** ID · região (x, y, w, h) · tipo (posição, tamanho, cor, tipografia, efeito, conteúdo, asset) · magnitude · severidade (Crítica, Alta, Média, Baixa) · causa provável · correção.
7. **Autocorreção:** corrija da maior para a menor severidade, recapture, recompare. Máximo de 5 ciclos por tela.
8. **Encerramento:** quando os critérios de aceitação forem atingidos ou o limite de ciclos esgotado, gere o `VALIDATION_REPORT_TEMPLATE.md`.

## Limiares
Use os limiares de aceitação de `STANDARDS.md` §3 (ajustáveis apenas nos Critérios de Aceitação, com aprovação).

## Causas comuns de diferença
Fonte diferente/ausente, antialiasing e subpixel, escala do dispositivo, compressão JPEG da referência, scroll/animação em andamento, imagens placeholder, barras do sistema na referência, perfil de cor.

## Honestidade
Reporte divergências remanescentes mesmo que pequenas. Diga qual parte da fidelidade **não pôde** ser verificada. Fidelidade declarada = números do relatório.

## Gravidade
Use as definições e a prioridade de correção de `STANDARDS.md` §2.

## Comparação por região e prioridade
1. Compare referência e resultado na **mesma resolução e escala**.
2. Compare região a região (A, B, C…) e registre diferenças por região.
3. Priorize correções nesta ordem: estrutura → dimensão → posição → tipografia → cor → efeitos.
4. Após cada correção, recapture e repita a comparação de todas as regiões (uma correção pode deslocar outras).
5. Use as ferramentas de comparação disponíveis (screenshots, sobreposição, diff); se nenhuma estiver disponível, declare e entregue checklist manual sem afirmar conformidade.

## Relatório honesto
O relatório separa: observado · estimado · implementado · testado · não validado · limitações.

## Avaliação final por categoria
| Categoria | Status | Evidências | Pendências |
|---|---|---|---|
| Fidelidade estrutural | | | |
| Fidelidade geométrica | | | |
| Fidelidade tipográfica | | | |
| Fidelidade cromática | | | |
| Fidelidade dos assets | | | |
| Fidelidade das animações | | | |
| Responsividade | | | |
| Funcionalidade | | | |
Status permitidos: Verificada · Parcialmente verificada · Não verificada · Divergente. Não use notas numéricas arbitrárias e não declare aprovação sem validação.

## Cobertura de requisitos
Confira cada `REQ-###` (esperado × medido × evidência). REQ sem verificação = "não validado".

## Scripts de apoio (se o ambiente puder executá-los)
Primeiro rode `python3 tools/check_env.py` e use só o que estiver OK.
- `tools/screenshot.py` captura o resultado (viewport, escala, animações congeladas).
- `tools/image_diff.py` compara referência × resultado, por região, e gera heatmap, sobreposição e lado a lado. A "sugestão de atenção" é só indicador numérico; a gravidade é decidida por inspeção.
- `tools/validate_tokens.py` valida o JSON de tokens.
Sem ambiente: entregue checklist manual e não declare conformidade.
