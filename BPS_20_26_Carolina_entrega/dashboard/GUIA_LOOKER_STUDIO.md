# Guia de construção do dashboard no Looker Studio

## Fonte

Use `data/processed/BPS_20_26_Carolina_Dashboard.csv` como fonte. O arquivo possui 369.152 linhas e 13 colunas, contendo apenas os campos necessários para a análise visual.

## Campos calculados

### Valor total registrado
`SUM(vl_preco_total)`

### Quantidade total
`SUM(qt_medicamento)`

### Número de registros
`COUNT(co_seq_bps)`

### Instituições
`COUNT_DISTINCT(no_instituicao)`

### Fornecedores
`COUNT_DISTINCT(no_fornecedor)`

### Preço unitário médio ponderado
`SUM(vl_preco_total) / SUM(qt_medicamento)`

## Página 1 – Visão geral

**Filtros:** Ano, UF, Município, Produto, Fornecedor, Fabricante e Modalidade.

**KPIs:** seis cartões no topo.

**Gráficos:**
1. Linha: valor registrado por ano.
2. Barras horizontais: top estados por valor.
3. Barras horizontais: top 10 produtos.
4. Barras horizontais: top 10 fornecedores.
5. Barras ou donut: valor por modalidade.

## Página 2 – Investigação de preços

Filtros adicionais: produto, fabricante, UF, ano e modalidade.

Tabela recomendada com:
- Produto
- Fabricante
- Fornecedor
- UF
- Ano
- Quantidade
- Preço unitário
- Valor total

Ordene por preço unitário para localizar diferenças que mereçam investigação. Não classifique automaticamente uma diferença como irregularidade.

## Design

Use fundo claro, azul escuro/cinza e um tom de destaque discreto. Priorize legibilidade e mantenha o título, filtros e KPIs na parte superior. Evite excesso de gráficos.
