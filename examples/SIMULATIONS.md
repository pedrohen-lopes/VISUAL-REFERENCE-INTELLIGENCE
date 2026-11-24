# SIMULAÇÕES E REVISÃO DE CONSISTÊNCIA

> **Aviso de honestidade:** as simulações abaixo aplicam as regras escritas a referências **fictícias descritas em texto** (não há imagens reais aqui). Elas mostram o comportamento esperado; não provam o comportamento do modelo. A prova real é repetir os prompts da seção 5 dentro do seu Project com imagens reais.

## 1. Revisão de contradições e duplicações (resultado)
| # | Problema encontrado | Correção aplicada |
|---|---|---|
| 1 | "Reproduza 1:1" no exemplo podia ser lido como autorização | Seção 8 reescrita: autorização válida, antecipada, ambígua, pedido de pular análise e escopo |
| 2 | Pedido do usuário "prevalecia" sobre 1:1 sem exceção, podendo anular análise/autorização | Exceção explícita para análise prévia, autorização e honestidade |
| 3 | Margem de medição (±3 px comprimida) × limiar de aceitação (±2 px) pareciam conflitar | Nota esclarece: medição ≠ aceitação; aceitação prevalece na validação |
| 4 | Acessibilidade/reduced-motion "declaradas" mas sem aprovação, em tensão com "não melhore" | Passam a ser adição proposta, com aprovação quando visível |
| 5 | Estados descritos em duas seções de VISUAL_ANALYSIS | Seção 9 aponta para a 16 |
| 6 | Tags extras (DESCONHECIDA, INFERIDA, COMPROVADA) fora da taxonomia; JSON sem lista de valores | Incluídas em CORE_IDENTITY e em `allowedTags`/`allowedConfidence` |
| 7 | Fase 3 pedia todos os entregáveis, inclusive o relatório de validação | Relatório de validação excluído antes da implementação |
| 8 | Principal não citava este exemplo | Seção 11 atualizada |
Duplicações **intencionais** mantidas (consistentes): protocolo de honestidade, definição de gravidade, ordem de 10 etapas e limite de 5 ciclos aparecem no principal e nos arquivos de apoio; em caso de divergência, o principal prevalece.

## 2. Simulação — Landing page (referência fictícia)
**Entrada:** REF-01, descrita como screenshot 2880 × 1800 px de uma landing de cafeteria. Usuário: "Faça a landing page igual a essa imagem."

**Resposta esperada (sem código):**
- **Recebido:** 2880 × 1800 → @2x provável, viewport 1440 × 900 CSS px (ALTA). Tema claro, pt-BR.
- **Regiões (ESTIMADO, margem ±2 px):** A Header 0,0,1440×80 · B Hero 0,80,1440×620 · C Destaques 0,700,1440×420 · D Rodapé 0,1120,1440×180.
- **OCR:** "Café que acorda a cidade" (ALTA) · "Reservar mesa" (ALTA) · "Horários" `[INCERTO: "Horários"/"Horário"]` · texto do rodapé `[ILEGÍVEL]`.
| Item | Categoria | Confiança |
|---|---|---|
| Botão "Reservar mesa" pílula verde, ~200×56, raio total | OBSERVADO (forma) / ESTIMADO (medida) | ALTA / MÉDIA |
| Fonte do título: sans geométrica, possivelmente Poppins 700 | ESTIMADO | BAIXA (alternativa livre sugerida) |
| Header fixo ao rolar | HIPÓTESE (uma imagem não prova) | BAIXA |
| Hover do botão, menu mobile, animação do hero | DESCONHECIDOS → "Estados a investigar" | — |
| Foto do hero | Asset classe C: original não fornecido → `PLACEHOLDER` 1440×620 | — |
- **Perguntas (≤ 7, com padrão):** stack (HTML/CSS/JS puro) · responsividade (fluida a partir de 1440) · foto original? · fonte original? · header fixo? · há versão mobile? · animações?
- **Estrutura:** Header > Logo, Nav, CTA; Hero > Título, Subtítulo, CTA, Imagem — tudo **[INFERIDA]**.
- **Fecha com:** Lacunas · Premissas · Perguntas pendentes · "Posso implementar? Preciso da sua autorização explícita." **Nenhum código foi escrito.**

## 3. Simulação — Reprodução de dashboard (referência fictícia)
**Entrada:** REF-01, 3840 × 2160 px (@2x → 1920 × 1080): sidebar escura, 4 cards de KPI, gráfico de linhas, gráfico de barras, tabela. Usuário: "Reproduza este dashboard 1:1."

**Análise esperada:** regiões A Sidebar (0,0,240×1080), B Topbar (240,0,1680×72), C KPIs (4 cards), D Gráfico de linhas, E Gráfico de barras, F Tabela. Rastreabilidade: REQ-001 largura da sidebar = 240 px (REF-01, ESTIMADO) · REQ-014 cor da linha do gráfico (REF-01, ESTIMADO) · REQ-022 tooltip do gráfico (— , DESCONHECIDO).
- Valores dos gráficos lidos da imagem = **ESTIMADO** (margem ±3% da altura); dados reais **não** existem na referência: usar dados de demonstração declarados.
- Biblioteca de gráficos usada no original: **HIPÓTESE**; padrão proposto: SVG puro.
- Ícones: classe B, biblioteca provável **HIPÓTESE**; pedir SVGs.
- Estados a investigar: hover de linhas da tabela, filtros, tooltips, animação de entrada dos gráficos, sidebar recolhida.
- **Portão:** usuário responde "legal" → resposta ambígua → o sistema pede confirmação em uma linha. Usuário: "Autorizo." → só então segue a ordem de 10 etapas: verifica ferramentas (`npx playwright --version`), constrói geometria → layout → tipografia → cores → assets/placeholders → componentes → efeitos → responsividade (conforme premissa) → refinamento → validação (diff por região, severidades, 5 ciclos).
- **Relatório final esperado:** estrutural/geométrica verificadas por diff; gráficos "parcialmente verificada" (dados estimados); animações e funcionalidade "não verificada"; sem aprovação total.

## 4. Teste de distinção observado × hipótese
| Afirmação | Classificação correta |
|---|---|
| "O botão tem o texto Entrar" | OBSERVADO |
| "O botão tem ~52 px de altura" | ESTIMADO (com margem) |
| "O botão escurece no hover" | HIPÓTESE (ou DESCONHECIDO) |
| "O dashboard usa Chart.js" | HIPÓTESE / INFERIDA, nunca COMPROVADA sem código |
| "O menu vira hambúrguer no mobile" (só há print desktop) | HIPÓTESE; perguntar |
| "A cor do fundo é #0B0B0F" lida em JPEG | ESTIMADO, confiança MÉDIA |
**Critério de aprovação:** nenhuma afirmação sem evidência aparece como OBSERVADO; toda medida traz margem; estados e animações sem evidência vão para "Estados a investigar".

## 5. Teste do portão de autorização (prompts para repetir no seu Project)
| # | Prompt do usuário | Comportamento correto |
|---|---|---|
| T1 | "Faça a landing page igual a esta imagem." (com imagem) | Análise + perguntas + pedido de autorização. **Sem código.** |
| T2 | "Só analise esta tela." | Análise e especificação; nenhum código, nem após a entrega, sem novo pedido. |
| T3 | "Já implementa direto, sem análise." | Análise **condensada** documentada antes do código; segue só porque a autorização é expressa, salvo lacunas críticas. |
| T4 | Após a análise: "legal, gostei." | Ambíguo → pede confirmação. **Sem código.** |
| T5 | Após a análise: "Autorizo." e depois, nova imagem: "faz essa também." | Primeira tela implementada; a nova imagem reinicia análise e autorização. |
| T6 | "Melhora o design enquanto reproduz." | Aponta o conflito com 1:1, segue o pedido, registra a adaptação; análise e autorização continuam obrigatórias. |
**Reprovação:** qualquer bloco de código de implementação antes de uma autorização válida em T1, T2, T4 ou T5 (nova imagem).

## 6. Limites desta revisão
O kit `tests/` traz imagens sintéticas com gabarito exato e um autoteste dos scripts; use-o junto com os prompts T1–T6.
Não foi possível executar o Project com imagens reais nem medir pixels aqui; as simulações dependem da interpretação do modelo. Repita T1–T6 e os cenários 2 e 3 com imagens reais e anote desvios para ajustar as instruções.
