# RESPONSIVE_ANALYSIS — Responsividade

## Princípio
A referência define **apenas** o viewport mostrado. Comportamento em outros tamanhos é [HIPÓTESE] e só é implementado conforme premissa aprovada.

## Procedimento
1. **Viewport da referência:** largura/altura em CSS px, orientação, dispositivo provável.
2. **Modo de responsividade** (perguntar): (a) apenas o viewport da referência, fixo; (b) fluido a partir da referência; (c) múltiplos breakpoints com referências para cada um. Padrão sugerido: (b) preservando 1:1 no viewport da referência.
3. **Identifique elementos de comportamento evidente:** largura fluida vs. fixa, `max-width` aparente, elementos centralizados, ancorados (sticky/fixed), proporções constantes (aspect-ratio).
4. **Múltiplas referências em tamanhos diferentes:** compare para inferir breakpoints, reordenação, colapso (menu → hambúrguer), mudança de colunas, escala de tipografia e espaçamento. Registre o breakpoint provável entre duas referências como [ESTIMADO] (intervalo, não ponto exato).
5. **Safe areas e barras do sistema:** notch, home indicator, barra de status, barra de navegação.
6. **Unidades:** reproduza o viewport de referência em px; use unidades relativas apenas onde o comportamento fluido for evidente ou aprovado.

## Matriz de breakpoints
| Breakpoint | Fonte (REF-ID / HIPÓTESE) | Layout | Mudanças | Confiança |
|---|---|---|---|---|

## Itens a documentar
Grid por breakpoint, visibilidade de elementos, ordem, tipografia fluida, imagens (srcset/ratios), toque vs. ponteiro (alvos ≥ 44 px como observação, sem alterar a referência), overflow e rolagem horizontal.

## Proibição
Não invente layout mobile/desktop a partir de uma única referência sem declarar e obter aprovação.

## Páginas e referências múltiplas
Ao receber várias imagens do mesmo produto, classifique-as (página, estado, breakpoint, versão) antes de inferir breakpoints. Mudanças de layout entre páginas diferentes não são breakpoints.
