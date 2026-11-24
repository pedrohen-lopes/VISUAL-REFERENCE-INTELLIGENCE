# CRITÉRIOS DE ACEITAÇÃO — {{projeto}} · {{REF-IDs}}

## 1. Condições de teste
Viewport {{W×H}} · escala {{x}} · navegador {{Chromium}} · fontes carregadas · animações {{congeladas/ativas}}.

## 2. Critérios globais
Valores padrão vindos de `instructions/STANDARDS.md` §3; só altere com aprovação do usuário e registre em "Exceções aprovadas".
| # | Critério | Limiar | Método | Obrigatório |
|---|---|---|---|---|
| G1 | Textos idênticos ao OCR confirmado | 100% | Comparação de texto | Sim |
| G2 | Posição/tamanho de elementos-chave | ±1 px (nítida) / ±2 px (comprimida) | Medição CSS computado | Sim |
| G3 | Cores em áreas chapadas | ΔE ≤ 2 | Leitura de pixel | Sim |
| G4 | Diff geral de pixels | ≤ 2% (tolerância canal ≤ 8/255) | Image diff | Sim |
| G5 | Divergências Críticas/Altas | 0 | Lista de divergências | Sim |
| G6 | Tipografia (família, peso, tamanho, line-height) | Igual à especificação | Inspeção | Sim |
| G7 | Assets | Todos presentes ou PLACEHOLDER declarado | Inventário | Sim |
| G8 | Motion | Duração ±50 ms, easing equivalente | Gravação/inspeção | Se houver |
| G9 | Responsividade | Conforme modo aprovado | Capturas em breakpoints | Se houver |

## 2A. Critérios por requisito
| REQ | Origem | Valor esperado | Limiar | Método | Obrigatório |
|---|---|---|---|---|---|

## 3. Critérios por componente
| Componente | Item | Valor esperado | Limiar | Método |
|---|---|---|---|---|

## 4. Exceções aprovadas
| Item | Motivo | Aprovado por |
|---|---|---|

## 5. Definição de pronto
Todos os critérios obrigatórios atendidos **ou** exceção aprovada; relatório de validação entregue com evidências; limitações declaradas.
