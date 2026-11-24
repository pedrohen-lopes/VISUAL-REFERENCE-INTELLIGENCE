# VISUAL_ANALYSIS — Procedimento de Análise Visual

Siga a ordem abaixo para cada referência. Registre resultados no `VISUAL_ANALYSIS_TEMPLATE.md`.

## 1. Metadados
Tipo (screenshot, mockup, foto de tela, vídeo), dimensões aparentes, proporção, orientação, dispositivo/viewport provável, escala (@1x/@2x/@3x), qualidade (compressão, ruído, recorte, distorção de perspectiva), tema (claro/escuro), idioma.

## 2. Visão geral
Propósito da tela, tipo de produto, hierarquia visual (o que se vê primeiro, segundo, terceiro), densidade, estilo (flat, glassmorphism, neumorphism, material etc.), mood.

## 3. Decomposição em camadas (de trás para frente)
1. Fundo (cor, gradiente, imagem, padrão, ruído).
2. Estrutura (containers, grids, colunas, gutters, margens, safe areas).
3. Seções (header, hero, conteúdo, sidebar, footer, modais, overlays).
4. Componentes (botões, inputs, cards, tabs, menus, badges, tabelas, listas, avatares…).
5. Elementos atômicos (texto, ícone, imagem, forma, divisor).
6. Efeitos (sombras, blur/backdrop, gradientes, bordas, opacidade, blend modes, máscaras).
7. Indicadores de estado (ativo, selecionado, desabilitado, erro, foco, carregamento).
8. Elementos flutuantes (tooltips, toasts, FABs, barras fixas).

## 4. Layout
Sistema de grid, número de colunas, larguras, alinhamentos, eixos de alinhamento recorrentes, ritmo vertical, escala de espaçamento detectada (ex.: múltiplos de 4 ou 8), comportamento de elementos fixos/sticky.

## 5. Tipografia
Por estilo de texto: família provável, peso, tamanho, altura de linha, letter-spacing, transformação, cor, alinhamento, truncamento. Agrupe em escala (display, h1…h6, body, caption, label, button, overline).

## 6. Cor
Paleta completa com HEX (e RGB), papel semântico (primária, superfície, texto, borda, feedback), usos, gradientes (ângulo, stops, cores), opacidades. Indique o método (leitura de pixel vs. estimativa visual).

## 7. OCR
Tabela: ID do elemento · texto literal · idioma · confiança. Preserve quebras, caixa, pontuação e símbolos. Use `[ILEGÍVEL]` e `[INCERTO: "..."]`.

## 8. Ícones e imagens
Estilo (outline, filled, duotone), grade, espessura de traço, tamanhos, biblioteca provável (informe como hipótese), cor. Imagens: proporção, enquadramento, raio, filtros, overlay.

## 9. Interação e estados
Ver seção 16 (tabela de estados, evidências e itens a investigar).

## 10. Mapa de lacunas
Tudo que está cortado, borrado, oculto, ilegível ou ambíguo.

## 11. Múltiplas referências
Compare elementos entre referências, marque conflitos, unifique tokens, indique qual referência é a "fonte de verdade" de cada elemento.

## Checklist de completude
- [ ] Todo texto visível transcrito
- [ ] Todo elemento com posição e tamanho
- [ ] Todas as cores catalogadas
- [ ] Todos os estilos de texto agrupados
- [ ] Efeitos descritos com parâmetros
- [ ] Lacunas e hipóteses listadas
- [ ] Confiança atribuída

## 12. Análise forense (obrigatória)
- **Relações espaciais:** eixos de alinhamento, razões de proporção, distâncias entre elementos, contenção/sobreposição, ordem de empilhamento.
- **Hierarquia visual:** ordem de leitura, pontos focais, contraste (cor, tamanho, peso), distribuição de peso (esquerda/direita, topo/base), espaço negativo.
- **Padrões repetidos:** liste instâncias de cada padrão e compare-as; registre variações sutis.
- **Inconsistências:** desalinhamentos, valores quase iguais, diferenças entre instâncias que deveriam ser iguais. Em 1:1, preserve-as e sinalize.
- **Detalhes pequenos:** divisores finos, sombras sutis, bordas internas, brilhos, texturas, ruído, opacidade de ícones, elementos cortados, artefatos de compressão (diferencie artefato de design).

## 13. Divisão por regiões e coordenadas
1. Divida a imagem em regiões nomeadas e contíguas que cubram toda a área (Região A: Header; B: Hero; C: Conteúdo principal; D: Cards; E: Footer; adapte à tela).
2. Para cada região registre: x, y, largura, altura (px da imagem e CSS px), distância até a região acima/abaixo/lados, relação com vizinhas e elementos contidos (IDs).
3. Dentro de cada região, use coordenadas relativas à região e absolutas à imagem.
4. Marque cada medida como [OBSERVADO] ou [ESTIMADO] com margem.
5. Se não for possível medir (imagem sem escala ou muito comprimida), registre a região de forma qualitativa e declare a limitação.

| Região | Nome | x | y | w | h | Acima | Abaixo | Esquerda | Direita | Elementos | Tag | Conf. |
|---|---|---|---|---|---|---|---|---|---|---|---|---|

## 14. Animações em imagem estática
Registre sempre: `Animações: DESCONHECIDAS (referência estática)`. Qualquer sugestão vira [HIPÓTESE] com pergunta ao usuário.

## 15. Estrutura provável da aplicação
Documente: hierarquia de componentes, componentes reutilizáveis, relação entre seções, estrutura de navegação e organização recomendada de arquivos. Rotule cada dedução **[INFERIDA]**; **[COMPROVADA]** apenas com evidência direta (código, DevTools, Figma, árvore de arquivos fornecida). Nunca apresente a estrutura inferida como a original.

## 16. Comportamento e estados
| Elemento | Estado | Evidência (REF/VIDEO) | Situação |
|---|---|---|---|
Estados a considerar: hover, active, focus, loading, disabled, menu aberto/fechado, modal, carrossel, scroll, transições, formulário e validação. Situação: **Evidenciado** ou **A investigar** (com pergunta ao usuário). Sem evidência, nada é implementado.

## 17. Várias referências do mesmo site/produto
1. Classifique cada imagem: página distinta / estado distinto / breakpoint distinto / versão distinta (pergunte se não for evidente).
2. Reconheça elementos compartilhados e compare instâncias entre páginas.
3. Identifique padrões de design (grid, ritmo, componentes recorrentes).
4. Detecte mudanças de layout entre páginas (header que muda, sidebar que some).
5. Construa a visão unificada: mapa de páginas, componentes comuns, tokens únicos.
6. Registre inconsistências entre páginas como conflitos com a referência de cada versão; não unifique em silêncio.

## 18. Rastreabilidade
Atribua `REQ-###` a cada requisito visual com origem (`REF-###`/`VIDEO-###`). Use a matriz do template técnico.

## 19. Scripts de apoio
Se o ambiente executar Python (`tools/check_env.py`): `tools/image_report.py` gera um relatório textual (paleta, faixas, mapa de cores, OCR) útil para agentes sem visão; `tools/ocr_text.py` extrai texto com confiança (baixa confiança vira `[INCERTO]`). A saída é [ESTIMADO] e complementa, sem substituir, a análise visual.
