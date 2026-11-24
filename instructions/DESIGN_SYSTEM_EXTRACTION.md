# DESIGN_SYSTEM_EXTRACTION — Extração de Design System

## Objetivo
Transformar valores observados em tokens consistentes, preservando os valores reais da referência (modo 1:1).

## Regras
1. **Valores reais primeiro:** o token recebe o valor medido, mesmo que "feio". Normalizações (ex.: 15 px → 16 px) só com declaração e autorização.
2. **Camadas de token:** primitivo (ex.: `color.green.500`) → semântico (`color.primary`) → componente (`button.primary.bg`).
3. **Nome por função, não por aparência**, quando a função é evidente; caso contrário, nome neutro (`color.neutral.900`).
4. **Deduplicação:** valores com diferença imperceptível (ΔE < 2 ou ±1 px) podem ser unificados apenas se declarado e confiança ALTA.
5. Cada token tem: valor, unidade, origem (REF-ID + elemento), tag (OBSERVADO/ESTIMADO/HIPÓTESE), confiança.

## Categorias obrigatórias
- **Cor:** primitivas, semânticas, superfícies, texto, bordas, feedback, gradientes, overlays.
- **Tipografia:** famílias, pesos, tamanhos, alturas de linha, letter-spacing, estilos compostos (`typography.heading.lg`).
- **Espaçamento:** escala detectada, paddings/margens/gaps recorrentes.
- **Layout:** breakpoints, larguras máximas, colunas, gutters, safe areas.
- **Raio, borda, sombra/elevação, opacidade, blur.**
- **Z-index:** camadas (base, sticky, dropdown, modal, toast).
- **Motion:** durações, easings, atrasos.
- **Iconografia:** tamanhos, espessura de traço.
- **Componentes:** variantes, estados, tokens por componente.

## Saída
Preencha `DESIGN_TOKENS_TEMPLATE.json` (JSON estrito: aspas duplas, sem comentários, sem vírgula final) e valide com `python -m json.tool` quando houver ambiente.

## Exportação opcional (somente se solicitado)
CSS custom properties, Tailwind theme, SCSS variables, Style Dictionary. Não introduza ferramentas não pedidas.

## Inconsistências
Liste valores que parecem inconsistentes na própria referência (ex.: dois verdes quase iguais). Em 1:1, mantenha ambos e sinalize.

## Múltiplas páginas
Consolide os tokens de todas as páginas em um único conjunto; cada token cita as referências onde aparece. Divergências de valor entre páginas viram conflitos listados (não unificar sem autorização).
