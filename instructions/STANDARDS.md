# STANDARDS — Padrões únicos (fonte de verdade para números e definições)

> Este arquivo é a **única fonte** de tolerâncias, gravidades, ordem de execução, IDs e categorias de avaliação. Outros arquivos podem citar estes valores como padrão, mas, em caso de divergência, **vale este**. Só altere os valores com aprovação do usuário (registre em Critérios de Aceitação).

## 1. Tags e confiança
Definições em `CORE_IDENTITY.md` (observado, estimado, hipótese, desconhecida, inferida, comprovada; confiança ALTA ≥ 90%, MÉDIA 60–89%, BAIXA < 60%).

## 2. Gravidade de diferenças
| Gravidade | Definição |
|---|---|
| Crítica | Altera significativamente a composição (elemento ausente, ordem/estrutura diferente, região deslocada). |
| Alta | Diferença visual evidente (tamanho, cor, tipografia ou posição claramente distintos). |
| Média | Diferença perceptível, porém localizada. |
| Baixa | Pequenos detalhes (1–2 px, sombra sutil, antialiasing). |
Prioridade de correção: estrutura → dimensão → posição → tipografia → cor → efeitos; dentro disso, da maior para a menor gravidade.

## 3. Tolerâncias
**Margem de medição (ao ler a referência):** ±1 px em imagem nítida @1x; ±2 px em @2x/@3x redimensionada; ±3 px ou mais em imagem comprimida/borrada.
**Limiares de aceitação (ao comparar resultado × referência):**
| Item | Limiar padrão |
|---|---|
| Textos | 100% idênticos ao OCR confirmado |
| Posição/tamanho | ±1 px (referência nítida) / ±2 px (comprimida) |
| Cor em áreas chapadas | ΔE ≤ 2; em estimativas ±3 por canal RGB |
| Diff geral | ≤ 2% de pixels divergentes (tolerância de canal ≤ 8/255), excluindo placeholders de foto |
| Divergências Críticas/Altas | 0 |
| Motion | duração ±50 ms, easing equivalente |
Na validação, os limiares de aceitação prevalecem sobre as margens de medição.

## 4. Ordem de execução (10 etapas)
1 Estrutura e geometria · 2 Layout e posicionamento · 3 Tipografia · 4 Cores e identidade visual · 5 Imagens e assets · 6 Componentes · 7 Animações e efeitos · 8 Responsividade · 9 Refinamento visual · 10 Validação final.

## 5. Identificadores e rastreabilidade
`REF-##` (imagem), `VIDEO-##` (vídeo), `REQ-###` (requisito), `COMP-##` (componente), `AST-##` (asset), `ANIM-##` (animação). Cada REQ tem: origem, tag, confiança, critério de aceitação e status (pendente, implementado, verificado, divergente). REQ sem verificação = "não validado".

## 6. Avaliação final
Categorias: fidelidade estrutural, geométrica, tipográfica, cromática, dos assets, das animações, responsividade e funcionalidade. Status permitidos: Verificada · Parcialmente verificada · Não verificada · Divergente. Cada categoria traz evidências e pendências. Sem notas numéricas arbitrárias; sem aprovação sem validação.

## 7. Limitações a declarar sempre que aplicáveis
Cores de imagem comprimida são estimadas · fontes são identificadas por semelhança · medidas em imagem redimensionada são aproximações · estados, animações e áreas ocultas são hipóteses/desconhecidos · imagens e fotos exigem o arquivo original · sem navegador e ferramenta de comparação não há validação automática (declare e use checklist manual).

## 8. Limites operacionais
Perguntas ao usuário: no máximo 7 por mensagem, com padrão sugerido. Ciclos de autocorreção: no máximo 5 por tela. Relatório final separa: observado · estimado · implementado · testado · não validado · limitações.
