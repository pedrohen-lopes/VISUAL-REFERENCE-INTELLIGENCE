# tools/ — Scripts de apoio

Transformam imagens em medidas e texto verificáveis e automatizam a comparação. **Rode primeiro `python3 check_env.py`** e use só o que estiver OK. Todos os resultados de leitura de imagem são **[ESTIMADO]**.

Instalação (PC com Zorin/Ubuntu): `pip install -r requirements.txt`; `sudo apt install tesseract-ocr tesseract-ocr-por ffmpeg`; `playwright install chromium`. Só Pillow e numpy são obrigatórios; o resto é opcional.

| Script | Para que serve | Exemplo |
|---|---|---|
| `check_env.py` | Lista o que está disponível | `python3 check_env.py` |
| `image_info.py` | Resolução, escala e viewport candidatos | `python3 image_info.py ref.png` |
| `sample_colors.py` | Cor por ponto/região (mediana) e paleta | `python3 sample_colors.py ref.png --region 810,150,100,100 --palette 6` |
| `crop_regions.py` | Recortes em PNG, com ampliação | `python3 crop_regions.py ref.png --region botao=96,420,240,64 --upscale 3` |
| `grid_overlay.py` | Grade com coordenadas sobre a imagem | `python3 grid_overlay.py ref.png --step 100` |
| `ocr_text.py` | Texto com caixa e confiança (baixa = `[INCERTO]`) | `python3 ocr_text.py ref.png --region 0,80,1440,300` |
| `image_report.py` | Relatório textual da imagem (para agentes sem visão) | `python3 image_report.py ref.png --out ref.md` |
| `image_diff.py` | Diff referência × resultado, por região, com heatmap/sobreposição/lado a lado | `python3 image_diff.py ref.png result.png --regions-file regions.json --out diff/` |
| `screenshot.py` | Screenshot com Playwright (viewport, escala, animações congeladas) | `python3 screenshot.py index.html --viewport 1440x900 --scale 1 --out result.png` |
| `extract_frames.py` | Quadros de vídeo e timestamps (ffmpeg) | `python3 extract_frames.py video.mp4 --fps 10` |
| `validate_tokens.py` | Valida JSON de tokens (sintaxe, tags, HEX, referências) | `python3 validate_tokens.py spec/tokens.json` |
| `make_handoff.py` | Monta a pasta de entrega para o Claude Code | `python3 make_handoff.py --target ../meu-projeto` |

## Limitações conhecidas
- `sample_colors --palette` e `image_report` fundem cores muito próximas (ex.: branco e cinza claríssimo); para valores exatos, use `--region` em áreas chapadas.
- OCR sem o idioma `por` instalado erra acentos (o script avisa); sempre confirme o texto literal visualmente.
- `image_diff` exige imagens na **mesma resolução/escala**; se diferirem, o aviso indica que posição e tamanho não são confiáveis. A "sugestão de atenção" é só um indicador numérico: a gravidade é decidida por inspeção.
- `image_report` detecta faixas por cor média de linha: serve para layouts com blocos de cor distintos, não para interfaces de fundo uniforme.
- Imagens JPEG têm cores e bordas estimadas com confiança menor.
- Autoteste dos scripts: `python3 ../tests/run_tool_checks.py`.
