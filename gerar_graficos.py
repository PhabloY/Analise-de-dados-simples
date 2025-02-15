import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('vendas.db')

# Carregando os dados das tabelas em DataFrames
vendas_df = pd.read_sql_query(''' 
SELECT vendas.id_venda, clientes.nome, produtos.nome_produto, vendas.quantidade, vendas.data_venda, produtos.preco_unitario
FROM vendas
JOIN clientes ON vendas.id_cliente = clientes.id_cliente
JOIN produtos ON vendas.id_produto = produtos.id_produto
''', conn)

# Fechando a conexão
conn.close()

# Passo 1: Análise de Dados

# Total de vendas por cliente
vendas_cliente = vendas_df.groupby('nome')['quantidade'].sum().reset_index()

# Total de vendas por produto
vendas_produto = vendas_df.groupby('nome_produto')[
    'quantidade'].sum().reset_index()

# Total de vendas em valor
vendas_df['valor_venda'] = vendas_df['quantidade'] * \
    vendas_df['preco_unitario']
vendas_valor = vendas_df.groupby('nome_produto')[
    'valor_venda'].sum().reset_index()

# Passo 2: Gerar Gráficos e Salvar como Imagens

# Gráfico 1: Total de vendas por cliente
plt.figure(figsize=(10, 6))
plt.bar(vendas_cliente['nome'], vendas_cliente['quantidade'], color='skyblue')
plt.title('Total de Vendas por Cliente')
plt.xlabel('Cliente')
plt.ylabel('Quantidade de Vendas')
plt.xticks(rotation=45)
plt.tight_layout()  # Ajusta para que tudo caiba
# Salva a imagem com o nome especificado
plt.savefig('grafico_vendas_cliente.png')
plt.close()  # Fecha a figura atual para liberar a memória

# Gráfico 2: Total de vendas por produto (quantidade)
plt.figure(figsize=(10, 6))
plt.bar(vendas_produto['nome_produto'],
        vendas_produto['quantidade'], color='salmon')
plt.title('Total de Vendas por Produto (Quantidade)')
plt.xlabel('Produto')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.tight_layout()  # Ajusta para que tudo caiba
# Salva a imagem com o nome especificado
plt.savefig('grafico_vendas_produto_quantidade.png')
plt.close()

# Gráfico 3: Total de vendas por produto (em valor)
plt.figure(figsize=(10, 6))
plt.bar(vendas_valor['nome_produto'],
        vendas_valor['valor_venda'], color='lightgreen')
plt.title('Total de Vendas por Produto (Valor)')
plt.xlabel('Produto')
plt.ylabel('Valor das Vendas (R$)')
plt.xticks(rotation=45)
plt.tight_layout()  # Ajusta para que tudo caiba
# Salva a imagem com o nome especificado
plt.savefig('grafico_vendas_produto_valor.png')
plt.close()
