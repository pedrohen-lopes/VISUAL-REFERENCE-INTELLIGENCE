---
description: Captura, compara com a referência por região, classifica gravidade e corrige (máx. 5 ciclos)
---
Valide a implementação: $ARGUMENTS

1. `python3 tools/check_env.py` (confirme Playwright/Chromium).
2. Capture com `tools/screenshot.py` no viewport e escala da referência.
3. Compare com `tools/image_diff.py` usando `spec/regions.json`; inspecione heatmap, sobreposição e lado a lado.
4. Classifique (Crítica/Alta/Média/Baixa), corrija da maior para a menor, recapture (máx. 5 ciclos).
5. Gere `reports/validation-report.md`: observado · estimado · implementado · testado · não validado · limitações, avaliação por categoria e cobertura de REQs. Sem notas arbitrárias; sem aprovação sem evidência.
