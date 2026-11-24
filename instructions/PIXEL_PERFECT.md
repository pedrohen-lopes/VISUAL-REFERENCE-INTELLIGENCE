# PIXEL_PERFECT — Análise em Nível de Pixel

## Objetivo
Obter medidas e cores o mais próximas possível do original e declarar a margem de erro de cada uma.

## 1. Calibração
1. Determine a resolução da imagem (largura × altura).
2. Determine a escala: compare com larguras de viewport comuns (360, 375, 390, 393, 412, 768, 1024, 1280, 1366, 1440, 1536, 1920 CSS px). Ex.: 1170 px de largura → provável iPhone @3x = 390 CSS px.
3. Use uma âncora: altura de status bar iOS (47–59 pt), Android (24 dp), ícone padrão 24 px, input 40–48 px, texto de corpo 14–16 px.
4. Registre: `escala = X; método = ...; confiança = ...`.
5. Todas as medidas finais ficam em **CSS px** (px da imagem ÷ escala), mantendo também o valor bruto.

## 2. Medição
- Meça de borda a borda do elemento visível (sem sombra).
- Espaçamentos: distância entre bordas de elementos adjacentes.
- Tipografia: tamanho = altura de caixa-alta (cap height) ÷ ~0,7 para fontes sans comuns (estimativa); altura de linha = distância entre linhas de base.
- Raio: observe a curvatura em cantos; compare com 2, 4, 6, 8, 12, 16, 24, 9999.
- Bordas: 1 px, 1,5 px, 2 px; cor e opacidade.
- Sombra: offset x/y, blur, spread, cor+alpha (estime por halo visível).
- Procure padrões: se medidas caem em múltiplos de 4/8, adote a grade e registre como premissa.
- Margem de erro: use as margens de medição de `STANDARDS.md` §3 (os limiares de aceitação são outro conceito e prevalecem na validação).

## 3. Cor
- Se houver ferramenta de execução, leia os pixels reais (Pillow/NumPy): amostre o centro de áreas chapadas, use a mediana de uma região 5×5, evite bordas antialiasadas.
- Sem ferramenta, estime visualmente e marque **[ESTIMADO] confiança MÉDIA/BAIXA**.
- Gradientes: amostre 3+ pontos ao longo do eixo; estime ângulo e stops.
- Transparências: diferencie cor sólida de cor + alpha sobre fundo; registre o fundo.
- JPEG: avise sobre artefatos; arredonde para a cor dominante.
- Verifique contraste texto/fundo (WCAG) apenas como informação, sem alterar a cor.

## 4. Tipografia
Identifique pelas formas (terminais, "a", "g", "R", "1"), proporções e peso. Liste candidata principal + 2 alternativas, com confiança. Se a fonte for proprietária, indique a alternativa livre mais próxima e diga que não será idêntica.

## 5. Formato de registro
| ID | Propriedade | Valor bruto (px img) | Valor CSS | Método | Margem | Confiança | Tag |
|---|---|---|---|---|---|---|---|

## 6. Proibições
- Não arredonde para "números bonitos" sem declarar.
- Não assuma um design system conhecido (Material, Tailwind) sem evidência; se usar como aproximação, marque como [HIPÓTESE].
- Não ajuste medidas para "ficar certinho" se isso contraria a referência em modo 1:1.

## 7. Medição por regiões
Meça primeiro as regiões (caixas delimitadoras), depois os elementos dentro delas. Registre distâncias entre bordas de regiões vizinhas. Verifique consistência: soma de alturas/larguras de regiões e gaps deve igualar o viewport; se não igualar, registre a discrepância em vez de ajustar valores.

## 8. Scripts de apoio (se o ambiente puder executá-los)
Rode antes `python3 tools/check_env.py`. Depois: `tools/image_info.py` (escala e viewport candidatos), `tools/sample_colors.py` (mediana por ponto/região; a paleta automática funde cores próximas, então use regiões para valores exatos), `tools/crop_regions.py` (recortes e ampliação) e `tools/grid_overlay.py` (grade de coordenadas). Resultados continuam [ESTIMADO] e entram no registro com método declarado.
