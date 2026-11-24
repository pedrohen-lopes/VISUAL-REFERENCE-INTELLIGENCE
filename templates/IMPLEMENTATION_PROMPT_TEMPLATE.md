# PROMPT DE IMPLEMENTAÇÃO — {{projeto}}

> Preencha os campos e entregue ao Claude Code (ou outro agente). Anexe: imagens de referência, `design-tokens.json`, especificação técnica, inventário e critérios de aceitação.

## Papel
Você é um desenvolvedor front-end responsável por reproduzir **1:1** a interface das referências anexas.

## Contexto
- Projeto: {{nome}} · Stack: {{stack}} · Diretório: {{caminho}}
- Viewport de referência: {{W×H}} @ {{escala}}
- Projeto existente: {{sim/não; convenções a seguir}}

## Regras
0. Verifique a disponibilidade das ferramentas (Playwright, Git etc.) antes de usá-las; não presuma instalação.
1. Siga exatamente a especificação técnica e os tokens; não arredonde, não melhore, não traduza.
2. Textos literais conforme a tabela de OCR anexa.
3. Altere **somente** os arquivos listados em "Escopo".
4. Não instale dependências além de: {{lista ou "nenhuma"}}.
5. Assets ausentes: nunca substitua por imagens genéricas sem autorização; use placeholder com as dimensões exatas e marque `PLACEHOLDER`.
6. Valores [ESTIMADO]/[HIPÓTESE] devem ter comentário de origem.

## Escopo de arquivos
- Criar: {{...}}
- Alterar: {{...}}
- Não tocar: {{...}}

## Tarefas (em ordem de prioridade)
1. Estrutura e geometria (tokens como variáveis CSS).
2. Layout e posicionamento.
3. Tipografia.
4. Cores e identidade visual.
5. Imagens e assets.
6. Componentes e estados evidenciados.
7. Animações e efeitos.
8. Responsividade: {{modo}}.
9. Refinamento visual.
10. Validação final.

## Validação obrigatória
1. Renderize em {{viewport}} @ {{escala}} e capture screenshot.
2. Compare com a referência (lado a lado, sobreposição, image diff).
3. Liste divergências por severidade e corrija até atender aos critérios de aceitação (máx. 5 ciclos).
4. Entregue o relatório de validação (com observado/estimado/implementado/testado/não validado/limitações) e as imagens de comparação.

## Rastreabilidade e projeto existente
Cite os REQ-### atendidos em cada alteração. Preserve funcionalidades existentes, não remova dependências sem justificativa, altere incrementalmente e entregue a lista de arquivos modificados.

## Entrega
Arquivos alterados, como executar, premissas aplicadas, placeholders, divergências remanescentes. Não declare fidelidade sem números do relatório.
