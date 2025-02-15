# Análise de Dados Simples: Vendas

## Descrição do Projeto

Este projeto tem como objetivo realizar uma **análise simples de dados de vendas** utilizando um banco de dados SQLite para armazenar os dados e Python para processamento e visualização. A análise foi estruturada para identificar padrões nas vendas, incluindo a quantidade de produtos vendidos por cliente, os produtos mais vendidos e o total gerado em vendas por produto.

A partir dessa análise, criamos gráficos para facilitar a visualização e ajudar na interpretação dos dados. O projeto utiliza as bibliotecas **Pandas** para análise de dados, **SQLite** para o banco de dados e **Matplotlib** para visualização gráfica.

## Tecnologias Utilizadas

- **Python 3.12**: A linguagem principal utilizada no projeto.
- **SQLite**: Banco de dados relacional utilizado para armazenar os dados de vendas.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Matplotlib**: Biblioteca para a criação de gráficos de visualização de dados.
- **Jupyter Notebook** (opcional): Para executar e interagir com o código de forma dinâmica.

## Objetivo

O objetivo principal é **analisar dados de vendas** para entender o comportamento de compra de clientes, quais produtos são mais vendidos e qual o impacto financeiro dessas vendas. Os dados são organizados em um banco de dados SQLite, que alimenta os gráficos gerados.

## Gráficos Gerados

Durante a análise, três gráficos principais foram gerados para ilustrar os resultados de forma visual:

### 1. Total de Vendas por Cliente
![Gráfico 1](https://i.imgur.com/TgywFRL.png)
Este gráfico mostra o **total de vendas por cliente**. Ele revela quais clientes são responsáveis pelas maiores quantidades de vendas, facilitando a identificação dos clientes mais engajados ou que mais compraram durante o período analisado.

### 2. Total de Vendas por Produto (Quantidade)
![Gráfico 2](https://i.imgur.com/5dFnCJ9.png)
Este gráfico apresenta o **total de vendas por produto**, em termos de **quantidade**. Ele indica os produtos mais populares entre os clientes, ou seja, aqueles com maior número de unidades vendidas. Isso pode ajudar a entender quais itens possuem maior demanda.

### 3. Total de Vendas por Produto (Valor)
![Gráfico 3](https://i.imgur.com/YLf3mzw.png)
Este gráfico mostra o **total de vendas por produto**, mas agora em termos de **valor financeiro**. Ele destaca quais produtos geraram maior receita, independentemente da quantidade vendida. Isso é útil para identificar os itens que mais impactam o faturamento da empresa.

## Como Executar

Siga os passos abaixo para executar o projeto no seu ambiente local:

### 1. Clone o Repositório
Clone este repositório para sua máquina local com o comando:
```bash
git clone https://github.com/PhabloY/Analise-de-dados-simples.git