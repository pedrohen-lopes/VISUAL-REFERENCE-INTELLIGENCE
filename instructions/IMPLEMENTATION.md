# IMPLEMENTATION — Implementação Autorizada

## Pré-condições (todas obrigatórias)
- [ ] Análise e especificação concluídas.
- [ ] Autorização explícita do usuário.
- [ ] Stack definida (ou padrão aprovado).
- [ ] Escopo de arquivos definido.
- [ ] Critérios de aceitação aprovados.

## Escolha de stack (quando não informada)
Padrão: **HTML + CSS + JavaScript puro** (sem build, sem dependências) para telas estáticas ou de baixa complexidade. Use React/Vue/Tailwind apenas se solicitado ou se o projeto existente já usar. Não adicione bibliotecas sem necessidade comprovada e autorização.

## Verificação de ferramentas
Antes de usar Playwright, DevTools, Figma, Git, ffmpeg ou bibliotecas de animação/renderização, verifique se estão disponíveis (comando de versão ou lista de ferramentas conectadas) e informe o resultado. Não presuma instalação; não instale sem autorização.

## Projeto existente
1. Leia estrutura, convenções, tokens e componentes.
2. Mapeie referência → componentes existentes; reutilize.
3. Liste arquivos a criar/alterar; altere somente o autorizado.
4. Preserve estilo de código, nomenclatura e lint.
5. Faça alterações incrementais, pequenas e reversíveis (commits quando houver Git); nunca reescreva histórico.
6. Preserve funcionalidades existentes; evite substituir arquivos inteiros sem necessidade; não remova dependências sem justificativa registrada.
7. Mantenha uma **lista de arquivos modificados** (criado/alterado/removido, com motivo e REQs atendidos) e entregue-a ao final.

## Ordem de construção (por prioridade)
Apresente esta ordem ao usuário antes de programar:
1. Estrutura e geometria (regiões, caixas, dimensões; tokens como variáveis CSS).
2. Layout e posicionamento (grid/flex, alinhamentos, gaps).
3. Tipografia.
4. Cores e identidade visual.
5. Imagens e assets (reais ou `PLACEHOLDER` marcados).
6. Componentes (e estados evidenciados).
7. Animações e efeitos.
8. Responsividade (conforme premissa aprovada).
9. Refinamento visual (ajustes guiados por diff, sem alterar a referência).
10. Validação final (`VISUAL_QA.md`).
Acessibilidade (semântica, `alt`, foco) é adição **proposta** que não altera o visual da referência: HTML semântico e `alt` (invisíveis) entram declarados nas premissas; qualquer mudança visível (ex.: anel de foco, `prefers-reduced-motion`) só com aprovação.

## Regras de código
- Valores medidos exatamente como especificados (não arredondar).
- Sem estilos inline desnecessários; classes com nomes funcionais.
- Todo texto exatamente como transcrito (OCR confirmado).
- Fontes: carregar a especificada; fallback declarado.
- Sem `!important` salvo necessidade documentada.
- Comentários mínimos, indicando origem do valor quando [ESTIMADO] ou [HIPÓTESE].
- Nada de dados reais sensíveis; use apenas o conteúdo da referência.

## Entrega
Lista de arquivos criados/alterados, como executar, premissas aplicadas, itens com PLACEHOLDER, limites conhecidos. Em seguida, **execute a validação** (`VISUAL_QA.md`) antes de declarar concluído.

## Proibido
Implementar sem autorização, "melhorar" o design, trocar conteúdo, afirmar fidelidade sem validação.

## Rastreabilidade
Cada alteração cita os `REQ-###` atendidos.

## Relatório final de implementação
Inclua: observado · estimado · implementado · testado (com método) · não validado · limitações.
