# MOTION_ANALYSIS — Análise de Movimento e Vídeo

## Quando usar
Referências em vídeo, GIF, sequência de frames ou quando o usuário informar que há animação. Em imagem estática, não invente movimento: registre apenas como [HIPÓTESE] e pergunte.

## 1. Extração
- Com ambiente de execução: extraia frames (ffmpeg, se disponível) em intervalos regulares e nos picos de mudança; registre fps, duração e resolução.
- Sem ambiente: peça frames-chave (início, meio, fim de cada transição) ou descrição.
- Referencie cada frame por timestamp (mm:ss.mmm) e ID (F001…).

## 2. Inventário de animações
Para cada animação: ID · elemento · gatilho (carregamento, scroll, hover, clique, tempo, loop) · propriedades animadas (opacity, transform: translate/scale/rotate, color, width, filter, clip-path, background-position) · valor inicial → final · duração · atraso · easing · repetição · direção · ordem/stagger · estado final · confiança.

## 3. Estimativa de timing
- Duração = (frame final − frame inicial) ÷ fps.
- Easing: compare a curva de deslocamento: linear, ease-in, ease-out, ease-in-out, spring/overshoot; sugira `cubic-bezier(...)` como [ESTIMADO].
- Stagger: diferença de início entre itens consecutivos.
- Faixas típicas apenas como referência: micro-interações 100–200 ms; transições 200–400 ms; entradas de seção 400–800 ms. Nunca substitua medidas reais por essas faixas.

## 4. Tipos específicos
- **Scroll:** parallax, sticky, reveal, scroll-snap, progress; registre posição de scroll de cada gatilho.
- **Loop/ambient:** marquee, gradientes animados, partículas, vídeo de fundo; registre ciclo completo.
- **3D/WebGL/canvas:** declare que reprodução 1:1 exige o asset/shader original ou aproximação; descreva câmera, luz, materiais e movimento.
- **Lottie/SVG:** identifique se é vetorial; peça o arquivo.
- **Cursor, hover e microfeedback:** registre apenas o que foi visto.

## 5. Implementação
Prefira CSS (transitions/keyframes) e Web Animations API; use bibliotecas apenas se a complexidade exigir e com autorização. Suporte a `prefers-reduced-motion` é adição **proposta**: só é aplicada se o usuário aprovar; por padrão o comportamento da referência é preservado.

## 6. Formato de saída
Tabela de animações + linha do tempo (timeline) textual + tokens de motion (duração, easing) no JSON.

## 7. Engenharia reversa quadro a quadro
1. Extraia todos os quadros nos trechos de movimento (não apenas amostras) quando houver ferramenta; liste timestamp por quadro.
2. Para cada elemento em movimento rastreie posição, escala, rotação, opacidade, cor e desfoque ao longo dos quadros.
3. **Direção e velocidade:** deslocamento em px ÷ tempo (px/s); registre aceleração/desaceleração.
4. **Easing:** plote deslocamento normalizado × tempo normalizado e ajuste a curva (linear, ease, cubic-bezier, spring com overshoot).
5. **Gatilhos:** carregamento, scroll (posição exata), hover, clique, tempo, visibilidade (intersection).
6. **Entradas, saídas e transições entre telas:** ordem, atrasos e stagger.
7. **Câmera, parallax e profundidade:** velocidade relativa por camada (fator de parallax), perspectiva, escala por profundidade, desfoque de profundidade.
8. **Receita técnica por efeito:** para cada animação documente como reproduzir (CSS transition/keyframes, Web Animations API, scroll-driven animations/IntersectionObserver, canvas/WebGL quando necessário), com valores iniciais/finais, duração, easing, atraso e fallback.
9. Elementos sem movimento observado: `Movimento: não observado`. Nunca presuma.

## 8. Imagens estáticas
Animações são **DESCONHECIDAS**. Registre qualquer ideia como [HIPÓTESE] e pergunte ao usuário se existem gravações.

## 9. Rastreabilidade e estados dinâmicos
Cada animação recebe `REQ-###` com origem (`VIDEO-###` ou `REF-###`). Documente também scroll, carrosséis, menus e modais **somente se observados**; os demais entram em "Estados a investigar".

## 10. Script de apoio
Com ambiente e `ffmpeg` verificados (`tools/check_env.py`), use `tools/extract_frames.py` (`--fps` fixo ou `--scene` por mudança de cena) para obter quadros e `timestamps.txt`. Sem ffmpeg, peça quadros-chave ao usuário.
