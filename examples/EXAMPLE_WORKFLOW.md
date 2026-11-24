# EXEMPLO DE FLUXO — Tela de login (fictícia)

## 1. Usuário envia
Screenshot `login.png` (1170 × 2532) e escreve: "Reproduza esta tela 1:1 em HTML/CSS."

## 2. Resposta do VRI — Recebimento e perguntas
**Recebido:** REF-01, 1170 × 2532 px; escala provável @3x → viewport 390 × 844 CSS px (ALTA, proporção de iPhone @3x). Tema escuro, idioma pt-BR.

**Perguntas (padrão se não responder):**
1. Stack? (HTML + CSS + JS puro)
2. Responsividade? (fluida a partir de 390 px, 1:1 em 390 × 844)
3. Possui o logo em SVG? (placeholder marcado)
4. Fonte original? (alternativa livre: Inter)
5. Há estados de erro/foco? (hipótese; não implementar sem confirmação)

## 3. Usuário responde
"Pode usar os padrões. Sem logo."

## 4. Análise (trecho)
| ID | Elemento | x | y | w | h | Valor | Tag | Conf. |
|---|---|---|---|---|---|---|---|---|
| T-01 | Título "Bem-vindo de volta" | 24 | 120 | 342 | 36 | 28/36, peso 700, #FFFFFF | ESTIMADO | MÉDIA |
| I-01 | Input e-mail | 24 | 220 | 342 | 52 | raio 12, borda 1 px #2A2A2A, fundo #141414 | OBSERVADO/ESTIMADO | ALTA/MÉDIA |
| B-01 | Botão "Entrar" | 24 | 400 | 342 | 52 | raio 12, fundo #22C55E, texto #0A0A0A 16/24 peso 600 | ESTIMADO | MÉDIA |

Tokens gerados em `design-tokens.json` (JSON validado). Hipóteses: hover do botão, foco do input.

**Lacunas:** logo ausente; fonte não confirmada.
**Premissas:** escala @3x; grade de 4 px.
**Perguntas pendentes:** nenhuma.
**Próximo passo:** autorização para implementar.

## 4A. Regiões (trecho)
| Região | Nome | x | y | w | h | Tag |
|---|---|---|---|---|---|---|
| A | Status bar + topo | 0 | 0 | 390 | 96 | ESTIMADO |
| B | Título | 0 | 96 | 390 | 96 | ESTIMADO |
| C | Formulário | 0 | 192 | 390 | 300 | ESTIMADO |
| D | Botão e links | 0 | 492 | 390 | 140 | ESTIMADO |
Animações: DESCONHECIDAS (referência estática).

## 4B. Rastreabilidade (trecho)
| REQ | Requisito | Origem | Tag |
|---|---|---|---|
| REQ-001 | Altura do botão "Entrar" = 52 px | REF-01 | ESTIMADO |
| REQ-002 | Cor de fundo do botão #22C55E | REF-01 | ESTIMADO |
| REQ-003 | Animação do botão | — | DESCONHECIDA (referência estática) |
Estrutura de componentes: [INFERIDA] (LoginScreen > Header, Form > Input, Button). Estados a investigar: hover, foco, erro de validação, carregamento.

## 5. Autorização
Usuário: "Autorizo."

## 6. Implementação
Arquivos: `index.html`, `styles.css`. Logo como `PLACEHOLDER` 96 × 96.

## 7. Validação
Chromium headless, 390 × 844 @3x. Ciclo 1: diff 3,8%, 2 divergências Altas (peso do título e raio do input). Correções aplicadas. Ciclo 2: diff 0,9%, 0 Crítica/Alta.

## 8. Relatório
Status: APROVADO COM EXCEÇÕES (logo placeholder; fonte alternativa). Avaliação por categoria: estrutural e geométrica = Verificadas (diff e medição); tipográfica = Parcialmente verificada (fonte alternativa); cromática = Verificada; assets = Parcialmente verificada (placeholder); animações = Não verificada (desconhecidas); responsividade = Não verificada; funcionalidade = Não verificada. Observado: layout e textos. Estimado: medidas e cores. Implementado: tela completa com placeholder. Testado: diff em 390 × 844 @3x (0,9%). Não validado: hover/foco, outras resoluções. Limitações: fonte alternativa, logo ausente.
