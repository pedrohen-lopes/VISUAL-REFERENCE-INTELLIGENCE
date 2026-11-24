# KIT DE TESTES

Imagens **sintéticas** com gabarito exato (`samples/ground_truth.json`), para testar o Project e os scripts. São geradas por `make_samples.py` (reproduzível).

| Arquivo | Conteúdo |
|---|---|
| `samples/landing_ref.png` | Landing 1440×900 @1x (header, hero, 3 cards, footer) |
| `samples/landing_result.png` | Mesma landing com **3 diferenças plantadas** |
| `samples/dashboard_ref.png` | Dashboard 1920×1080 (sidebar, 4 KPIs, linha, barras, tabela) |
| `samples/ground_truth.json` | Regiões, cores, textos, dados reais dos gráficos, estados sem evidência |

## 1. Autoteste dos scripts (PC)
`python3 tests/run_tool_checks.py` — deve terminar com 0 falhas (testes sem ferramenta opcional aparecem como SKIP).

## 2. Testes no Project (envie as imagens e confira)
| # | Prompt | Aprovado se |
|---|---|---|
| P1 | Enviar `landing_ref.png` + "Faça a landing page igual a esta imagem." | Faz análise e perguntas e pede autorização; **nenhum código** |
| P2 | `/analisar` com `landing_ref.png` | Viewport 1440×900 @1x; regiões A–D dentro de ±2 px do gabarito; todos os 13 textos; animações **DESCONHECIDAS**; hover, menu mobile e header fixo em "a investigar" |
| P3 | Responder "legal, gostei." após o P1 | Pede confirmação; **nenhum código** |
| P4 | Responder "Autorizo." | Só então inicia a implementação, na ordem de 10 etapas, verificando ferramentas |
| P5 | Enviar `landing_ref.png` + `landing_result.png` e `/comparar` | Encontra as 3 diferenças (botão 6 px abaixo, verde diferente, "Cidade" com C maiúsculo) e classifica gravidade |
| P6 | `/analisar` com `dashboard_ref.png` | Valores dos gráficos marcados [ESTIMADO] com margem; biblioteca de gráficos como [HIPÓTESE]; tooltips, filtros e hover em "a investigar" |
| P7 | "Já implementa direto, sem análise." | Análise condensada documentada antes do código; segue apenas se a autorização for expressa |
| P8 | "Melhora o design enquanto reproduz." | Aponta o conflito com 1:1 e registra adaptação; análise e autorização continuam obrigatórias |

## 3. Conferência contra o gabarito
- Estimativas de dados do gráfico (P6): compare com `dados_reais_*` e registre o erro médio; ele deve caber na margem que o Claude declarou.
- Cores: devem coincidir com `cores` (ou ser declaradas [ESTIMADO] com margem).
- Qualquer afirmação "idêntico/100% fiel" sem evidência reprova o teste.

## 4. Como registrar resultados
Para cada P#, anote Aprovado/Reprovado e o trecho que falhou. Reprovações viram ajustes em `CLAUDE_PROJECT_INSTRUCTIONS.md` ou nos arquivos de `instructions/`.
