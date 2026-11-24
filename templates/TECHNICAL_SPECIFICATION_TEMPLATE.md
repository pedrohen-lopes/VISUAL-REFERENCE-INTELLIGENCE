# ESPECIFICAÇÃO TÉCNICA — {{projeto}} · {{REF-IDs}}

## 1. Escopo e modo
- Modo: 1:1 estrito / 1:1 com adaptações aprovadas
- Stack: {{stack}}
- Projeto existente: sim/não ({{caminho}})
- Viewport de referência: {{W×H}} @ {{escala}}

## 2. Estrutura de arquivos
```
{{árvore de arquivos a criar/alterar}}
```

## 3. Regiões e estrutura de layout
Tabela de regiões (A, B, C…) com x, y, w, h, distâncias e relacionamento; depois a hierarquia de elementos.
Hierarquia de elementos (DOM lógico) com tipo de layout (flex/grid/absolute), dimensões, gaps, padding, alinhamento.

## 4. Tokens
Referência ao arquivo `design-tokens.json`; liste os principais.

## 5. Especificação por componente
Para cada componente: nome · estrutura · dimensões · espaçamento · tipografia · cores · bordas/raio/sombra · estados · conteúdo literal · assets · confiança.

## 6. Tipografia e fontes
Fonte principal, alternativas, pesos a carregar, fallback.

## 7. Assets
Tabela (ver Inventário).

## 8. Motion
| ID | Elemento | Gatilho | Propriedades | De → Para | Duração | Easing | Atraso | Conf. |
|---|---|---|---|---|---|---|---|---|

## 9. Responsividade
Modo escolhido e matriz de breakpoints.

## 10. Acessibilidade (adições propostas, sujeitas a aprovação)
Semântica, alt, foco, contraste — sem alterar a aparência da referência.

## 10A. Estrutura inferida da aplicação
Todos os itens marcados **[INFERIDA]** (ou **[COMPROVADA]** com evidência): hierarquia de componentes, reutilizáveis, relação entre seções, navegação, estados possíveis, organização de arquivos.

## 10B. Estados a investigar
| Componente | Estado | Motivo | Pergunta ao usuário |
|---|---|---|---|

## 10C. Ordem de execução
1 Estrutura/geometria · 2 Layout · 3 Tipografia · 4 Cores · 5 Assets · 6 Componentes · 7 Animações/efeitos · 8 Responsividade · 9 Refinamento · 10 Validação.

## 10D. Matriz de rastreabilidade
| REQ | Requisito | Origem (REF/VIDEO) | Tag | Conf. | Critério | Status |
|---|---|---|---|---|---|---|
| REQ-001 | Altura do header | REF-001 | | | | pendente |
| REQ-002 | Cor do botão principal | REF-001 | | | | pendente |
| REQ-003 | Animação do hero | VIDEO-001 | | | | pendente |

## 11. Premissas, lacunas e riscos
| Item | Tipo | Impacto | Mitigação |
|---|---|---|---|

## 12. Critérios de aceitação
Ver `ACCEPTANCE_CRITERIA`.
