# SHORTCUTS — Atalhos de comando (digitáveis no celular)

Atalhos são apenas conveniência: **não** alteram nenhuma regra (análise prévia, autorização, honestidade). Se o usuário digitar um atalho, execute a ação correspondente; se digitar texto livre, interprete a intenção.

| Atalho | Ação | Escreve código? |
|---|---|---|
| `/analisar` | Fases 0–2: recebimento, perguntas necessárias e análise completa (regiões, OCR, medidas, cores, tipografia, estados, estrutura [INFERIDA]). | Não |
| `/perguntas` | Lista só as perguntas pendentes que mudam o resultado, com padrão sugerido. | Não |
| `/especificar` | Fase 3: especificação técnica, tokens JSON, inventário, critérios de aceitação e matriz REQ. | Não |
| `/comparar` | Compara 2+ referências: classifica páginas/estados, elementos compartilhados, mudanças de layout, conflitos. | Não |
| `/implementar` | Equivale a autorização **se** já existe análise/especificação apresentada. Se não existir, faz análise condensada primeiro (e só então implementa, por autorização antecipada). | Sim, mediante a regra de autorização |
| `/validar` | Fase 6: captura, compara por região, classifica gravidade, corrige (máx. 5 ciclos) e emite o relatório. Exige ferramentas verificadas. | Apenas correções do escopo autorizado |
| `/status` | Resumo: referências, REQs (pendente/implementado/verificado/divergente), lacunas, perguntas e próximo passo. | Não |
| `/relatorio` | Relatório honesto: observado · estimado · implementado · testado · não validado · limitações + avaliação por categoria. | Não |

Observações:
- `/implementar` em nova imagem ou nova tela reinicia a análise dessa referência.
- Se uma ferramenta necessária não estiver disponível, diga o que deixa de ser validado.
