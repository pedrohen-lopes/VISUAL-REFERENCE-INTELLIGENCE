# ASSET_ANALYSIS — Inventário e Tratamento de Assets

## Classificação
| Classe | Exemplos | Estratégia |
|---|---|---|
| A — Reproduzível em código | formas, gradientes, sombras, divisores, padrões simples | Construir com CSS/SVG |
| B — Vetorial identificável | ícones, logos simples | Pedir SVG original; se inexistente, recriar em SVG ou usar biblioteca equivalente (declarar diferença) |
| C — Raster | fotos, ilustrações, texturas, avatares, mockups | Exigir arquivo original; recortar da referência apenas se o usuário autorizar e com aviso de perda de qualidade |
| D — Tipografia | fontes | Identificar; fornecer fonte original ou alternativa livre |
| E — Mídia | vídeo, Lottie, 3D | Exigir arquivo original |

## Inventário por asset
ID · nome sugerido de arquivo · classe · posição e tamanho exibidos · tamanho natural estimado · proporção · formato recomendado (SVG/PNG/JPG/WebP) · uso (ex.: background, `<img>`, ícone) · filtros/máscaras/overlays aplicados · disponibilidade (fornecido / ausente / a recriar) · confiança.

## Regras
1. Nunca substitua assets importantes (fotos, ilustrações, logos, vídeos) por imagens genéricas ou de stock sem autorização do usuário; sem autorização, use placeholder neutro com as dimensões exatas e marque `PLACEHOLDER`.
2. Não afirme identificar marca/logo sem evidência; descreva a forma.
3. Direitos autorais: avise que fontes, ícones e imagens podem ter licença própria; o usuário responde pelo uso.
4. Recortes de screenshot: informe coordenadas (x, y, w, h) e escala; entregue em PNG sem recompressão.
5. Ícones: registre grade (16/20/24), espessura de traço, cantos (arredondado/reto) e cor; sugira biblioteca apenas como aproximação.
6. Imagens de fundo: registre `object-fit`, posição, overlay, desfoque.
7. Peça ao usuário os assets originais sempre que a fidelidade depender deles.

## Investigação por asset (obrigatória)
Para cada imagem, ícone, ilustração, textura ou vídeo registre:
1. **Tipo** (classe A–E) e **características** (estilo, cores dominantes, composição, texturas, filtros).
2. **Arquivo original disponível?** (fornecido / não fornecido / provavelmente em biblioteca pública — hipótese).
3. **Ação recomendada:** *localizar* o original (peça ao usuário ou indique busca), *substituir* por asset licenciado (somente com autorização) ou *recriar* (somente classes A/B quando viável).
4. **Preservação:** proporção, enquadramento, `object-fit`/posição, recortes, máscaras e posição na tela.
5. **Risco de fidelidade:** o que se perde se o asset não for o original.

## Script de apoio
`tools/crop_regions.py` recorta assets da referência em PNG (sem recompressão) e amplia para inspeção. Recortes só são entregues como asset se o usuário autorizar.
