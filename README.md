# Banco de Preços em Saúde (BPS) | Análise de Compras 2020–2026

Projeto acadêmico de Visualização de Dados e Business Intelligence da **Carreira Tech – Trilha Análise de Dados**.

> **Status:** o dashboard foi montado no Looker Studio com KPIs, filtros e gráficos. Antes da publicação final, substitua os campos indicados como pendentes pelos links reais do relatório e do repositório. Este README descreve a versão CSV enviada para revisão.

## 1. Objetivo

Analisar registros de compras de medicamentos e dispositivos médicos presentes no Banco de Preços em Saúde (BPS), observando valores registrados, quantidades, distribuição geográfica, produtos, fornecedores e modalidades de compra entre 2020 e 2026.

A análise é descritiva e exploratória. Diferenças de preços não comprovam, por si só, economia, sobrepreço ou irregularidade.

## 2. Perguntas de negócio

1. Como o valor financeiro registrado evoluiu por ano?
2. Quais estados e municípios concentram maior valor registrado?
3. Quais produtos e fornecedores apresentam maior participação financeira?
4. Quais modalidades de compra concentram maior valor?
5. Quais diferenças de preços merecem investigação adicional, depois de controlar produto, apresentação, unidade, fabricante, quantidade, localidade, modalidade e período?

## 3. Fonte dos dados

- **Fonte oficial:** Ministério da Saúde, Portal Brasileiro de Dados Abertos, Banco de Preços em Saúde (BPS): https://dadosabertos.saude.gov.br/dataset/bps
- **Dicionário oficial:** https://dadosabertos.saude.gov.br/dataset/bps/resource/0e76f527-5e7e-417d-9d0b-f46d00afb717
- **Período analisado:** registros com `ano_compra` de 2020 a 2026.

O arquivo utilizado no Looker Studio é `BPS_20_26_Carolina_Dashboard_Looker.csv`. A versão recebida contém **369,152 linhas e 13 colunas**.

## 4. Arquivo e preparação dos dados

A versão de dashboard contém estes campos:

`ano_compra`, `dt_compra`, `sg_uf`, `ds_item`, `no_fornecedor`, `no_fabricante`, `qt_medicamento`, `no_instituicao`, `no_municipio`, `modalidade`, `vl_preco_unitario`, `vl_preco_total` e `co_seq_bps`.

O CSV está codificado em UTF-8 com BOM e utiliza vírgula como delimitador, formato usado para importação no Looker Studio.

### Procedimentos a documentar no repositório

O arquivo final consolidado está disponível, mas os sete CSVs anuais originais e o script usado na concatenação **não foram incluídos nos arquivos enviados para esta revisão**. Para tornar o processo totalmente reproduzível, inclua no GitHub o script efetivamente usado para baixar/ler e concatenar os arquivos anuais, ou ajuste esta seção para refletir fielmente o método que você utilizou.

Não declare que os arquivos anuais foram tratados de uma forma específica sem confirmar que esse procedimento foi executado.

### Validações feitas no CSV recebido

- Linhas: **369,152**.
- Colunas: **13**.
- Identificadores `co_seq_bps` distintos: **369,152**.
- IDs duplicados no arquivo: **0**.
- Instituições distintas com nome preenchido: **688**.
- Fornecedores distintos com nome preenchido: **3,470**.
- Fabricantes distintos com nome preenchido: **2,208**.
- Valores ausentes em `no_instituicao`: **312**.
- Soma de `vl_preco_total`: **R$ 115,44 bi**.
- Soma de `qt_medicamento`: **64,914,068,551**.
- Preço unitário médio ponderado: **R$ 1.78**.

A contagem de instituições deve ignorar valores vazios/nulos. O Looker pode apresentar um valor uma unidade maior se tratar o campo vazio como uma categoria distinta; por isso, confira a configuração do KPI de instituições.

## 5. Campos principais

| Campo | Uso |
|---|---|
| `ano_compra` | Ano para análise anual e filtro |
| `dt_compra` | Data da compra |
| `sg_uf` | Estado |
| `no_municipio` | Município |
| `no_instituicao` | Nome da instituição compradora |
| `ds_item` | Descrição do produto |
| `no_fornecedor` | Nome do fornecedor |
| `no_fabricante` | Nome do fabricante |
| `modalidade` | Modalidade da compra |
| `qt_medicamento` | Quantidade registrada |
| `vl_preco_unitario` | Preço unitário informado |
| `vl_preco_total` | Valor total registrado |
| `co_seq_bps` | Identificador do registro |

## 6. KPIs e fórmulas

| KPI | Fórmula / agregação | Interpretação |
|---|---|---|
| Valor total registrado | `SUM(vl_preco_total)` | Soma dos valores dos registros filtrados |
| Quantidade total de itens | `SUM(qt_medicamento)` | Soma das quantidades registradas |
| Número de registros | `COUNT(co_seq_bps)` ou contagem de registros | Quantidade de linhas no contexto dos filtros |
| Instituições compradoras | Contagem distinta de `no_instituicao`, excluindo vazio/nulo | Número de nomes distintos de instituições |
| Fornecedores | Contagem distinta de `no_fornecedor` | Número de fornecedores distintos |
| Preço unitário médio ponderado | `SUM(vl_preco_total) / SUM(qt_medicamento)` | Valor total dividido pela quantidade total |

O preço ponderado geral não deve ser usado para comparar diretamente produtos ou unidades diferentes.

## 7. Dashboard

**Ferramenta:** Looker Studio.

**Dashboard Looker Studio:** o link compartilhável deve ser adicionado após configurar o acesso ao relatório.

Filtros visíveis na versão atual:
- Ano (`ano_compra`)
- Estado (`sg_uf`)
- Município (`no_municipio`)
- Modalidade (`modalidade`)
- Fornecedor (`no_fornecedor`)

Visuais montados:
1. Top estados por valor registrado.
2. Top municípios por valor registrado.
3. Top fornecedores por valor registrado.
4. Evolução anual do valor registrado (gráfico de barras).
5. Top produtos por valor registrado.
6. Valor por modalidade de compra.

Os gráficos de ranking usam a soma de `vl_preco_total`. Quando a opção “Agrupar o restante como Outros” está habilitada, a categoria “Outros” agrega todos os itens que ficaram fora do limite de exibição e não representa um único fornecedor/produto.

## 8. Principais resultados observados

### Resumo geral

- Valor total registrado: **R$ 115,44 bi**.
- Quantidade total registrada: **64.91 bilhões**.
- Registros: **369,152**.
- Instituições com nome preenchido: **688**.
- Fornecedores distintos: **3,470**.
- Preço unitário médio ponderado: **R$ 1.78**.

### Evolução anual

| Ano | Registros | Valor registrado | Quantidade | Preço ponderado |
|---:|---:|---:|---:|---:|
| 2020 | 84.920 | R$ 5.05 bi | 8,77 bi | R$ 0,58 |
| 2021 | 85.160 | R$ 7.42 bi | 10,73 bi | R$ 0,69 |
| 2022 | 89.663 | R$ 16.87 bi | 15,21 bi | R$ 1,11 |
| 2023 | 33.874 | R$ 4.96 bi | 10,27 bi | R$ 0,48 |
| 2024 | 28.902 | R$ 9.10 bi | 5,73 bi | R$ 1,59 |
| 2025 | 34.961 | R$ 50.97 bi | 8,87 bi | R$ 5,75 |
| 2026 | 11.672 | R$ 21.07 bi | 5,33 bi | R$ 3,95 |

O ano de 2026 contém somente os registros presentes no arquivo recebido e pode representar um período incompleto. Não deve ser comparado diretamente com anos completos sem verificar a cobertura temporal.

### Estados

Os cinco estados com maior soma de valor registrado são: **PR (R$ 43,18 bi), SP (R$ 42,75 bi), RS (R$ 6,21 bi), CE (R$ 5,40 bi), RJ (R$ 5,36 bi)**.

### Produtos com maior valor registrado

- **PENICILAMINA, DOSAGEM:250 MG**: R$ 22,86 bi.
- **OCTREOTIDA, DOSAGEM:0,1 MG/ML, FORMA FARMACÊUTICA:SOLUÇÃO INJETÁVEL**: R$ 14,60 bi.
- **AMOXICILINA, CONCENTRAÇÃO:500MG**: R$ 13,42 bi.

### Fornecedores com maior valor registrado

- **AGILLE COMERCIO DE MEDICAMENTOS LTDA**: R$ 22,86 bi.
- **PORTAL LTDA**: R$ 15,06 bi.
- **MED4 IMPORTADORA E DISTRIBUIDORA LTDA**: R$ 13,36 bi.

### Modalidade

A modalidade com maior soma de valor registrado é **Pregão**, com **R$ 106,45 bi**.

### Ponto para investigação

O valor registrado em 2025 é consideravelmente maior que em 2024 na base analisada. Esse resultado deve ser investigado por produto, estado, instituição e fornecedor. O gráfico, isoladamente, não explica a causa do aumento.

## 9. Recomendações

1. Usar os filtros para localizar concentrações de valores por estado, município, produto, fornecedor e modalidade.
2. Investigar alterações anuais expressivas por meio de recortes por produto e instituição.
3. Comparar preços somente entre registros comparáveis, verificando descrição/apresentação, unidade, fabricante, quantidade, período e modalidade.
4. Tratar a categoria “Outros” como um agrupamento de itens fora do ranking exibido.
5. Não concluir sobre irregularidade, economia ou sobrepreço apenas a partir de diferenças descritivas.
6. Atualizar o conjunto de dados quando houver novos registros e documentar a data de extração.

## 10. Limitações

- O CSV do dashboard não contém todos os campos do arquivo original; contém uma seleção de 13 colunas.
- O campo de instituição tem **312 valores ausentes**, o que afeta a contagem distinta.
- O valor total registrado não equivale necessariamente a gasto liquidado ou pago.
- O ano de 2026 pode estar incompleto.
- A média ponderada geral mistura itens diferentes e não é adequada para comparar preços de produtos distintos.
- Os gráficos de ranking mostram concentração financeira, não necessariamente maior quantidade física adquirida.
- O arquivo CSV final, sozinho, não permite reproduzir a etapa de concatenação sem os arquivos anuais ou o script correspondente.

## 11. Como reproduzir

1. Baixe os arquivos anuais de 2020 a 2026 na fonte oficial do BPS.
2. Consulte o dicionário de dados e confira a estrutura de cada arquivo.
3. Prepare e concatene os arquivos anuais, padronizando as colunas e os tipos de dados. O script Python utilizado nessa etapa deverá ser incluído no repositório para permitir a reprodução do processo.
4. Conecte o CSV consolidado/enxuto ao Looker Studio.
5. Confira os tipos e agregações dos campos e valide os KPIs com os totais calculados no arquivo.
6. Aplique os filtros e compare os valores com os resultados registrados neste README.

## 12. Estrutura recomendada do repositório

BPS_20_26_Carolina/
├── README.md
├── data/
│   └── processed/
│       └── BPS_20_26_Carolina_Dashboard_Looker.csv
├── scripts/
│   └── tratamento_bps.py
├── dashboard/
│   └── dashboard.png
└── video/
    └── apresentacao.mp4

## 13. Versionamento sugerido

Use commits pequenos e descritivos, conforme as mudanças realmente realizadas. Exemplos:

- `docs: cria README do projeto`
- `data: adiciona base consolidada para o dashboard`
- `feat: documenta KPIs e métricas`
- `feat: adiciona capturas do dashboard`
- `docs: registra limitações e recomendações`

Crie apenas commits e branches correspondentes a atividades que você realmente executou.

14. Links do projeto

Dashboard Looker Studio: https://datastudio.google.com/s/v3OGKY2_CQY
Repositório GitHub: https://github.com/carolsscv/BPS-Analise-Compras-Saude-2020-2026/

Autora

Carolina da Silva Corrêa

Projeto acadêmico – Carreira Tech | Trilha Análise de Dados
