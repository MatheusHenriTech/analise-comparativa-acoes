# Análise Comparativa de Ações

Projeto de análise de dados desenvolvido com Python, utilizando Pandas, yfinance e Matplotlib para comparar o desempenho histórico das ações BBSE3, ITSA4 e VALE3.

## Objetivo

Analisar o comportamento das três ações ao longo de 12 meses, comparando rentabilidade, volatilidade e evolução dos preços.

## Tecnologias utilizadas

- Python
- Pandas
- yfinance
- Matplotlib
- Jupyter Notebook

## Indicadores analisados

- Preços de fechamento
- Rentabilidade acumulada
- Retornos diários
- Volatilidade diária e anualizada
- Preços máximos e mínimos
- Retorno por volatilidade

## Principais resultados

Período analisado: 17/11/2025 a 17/11/2026.

| Indicador               |  BBSE3 |  ITSA4 |  VALE3 |
| ----------------------- | -----: | -----: | -----: |
| Rentabilidade           | 24,32% | 24,90% |  0,09% |
| Volatilidade anualizada | 22,83% | 31,17% | 28,89% |

A ITSA4 apresentou a maior rentabilidade acumulada, enquanto a BBSE3 registrou a menor volatilidade anualizada.

Já a VALE3 apresentou a menor rentabilidade entre os ativos analisados.

## Conclusão

A ITSA4 se destacou pela maior rentabilidade no período, mas também apresentou maior volatilidade.

A BBSE3 apresentou uma rentabilidade próxima à ITSA4, com menor volatilidade, destacando-se pela melhor relação risco-retorno entre os ativos analisados.

## Estrutura do projeto

- `analise_comparativa_acoes.ipynb`: notebook responsável pela exploração, análise e visualização dos dados.
- `coletar_dados.py`: script responsável pela coleta dos dados históricos utilizando yfinance.
- `dados_acoes.csv`: arquivo com os dados históricos utilizados na análise.
- `README.md`: documentação e apresentação do projeto.

## Como executar o projeto

### 1. Instalar as bibliotecas

```bash
pip install pandas yfinance matplotlib jupyter
```

### 2. Executar a análise

Abra o arquivo `analise_comparativa_acoes.ipynb` no VS Code ou Jupyter Notebook e execute todas as células.

O notebook utiliza os dados históricos armazenados em `dados_acoes.csv`, referentes ao período de 17/11/2025 a 17/11/2026.
