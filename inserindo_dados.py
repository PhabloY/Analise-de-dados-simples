import sqlite3

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

# Inserindo dados na tabela de clientes
cursor.execute(
    "INSERT INTO clientes (nome, email, idade, cidade) VALUES ('João', 'joao@email.com', 28, 'São Paulo')")
cursor.execute(
    "INSERT INTO clientes (nome, email, idade, cidade) VALUES ('Maria', 'maria@email.com', 35, 'Rio de Janeiro')")
cursor.execute(
    "INSERT INTO clientes (nome, email, idade, cidade) VALUES ('Carlos', 'carlos@email.com', 22, 'Belo Horizonte')")
cursor.execute(
    "INSERT INTO clientes (nome, email, idade, cidade) VALUES ('Ana', 'ana@email.com', 29, 'Curitiba')")
cursor.execute(
    "INSERT INTO clientes (nome, email, idade, cidade) VALUES ('José', 'jose@email.com', 40, 'Porto Alegre')")
cursor.execute(
    "INSERT INTO clientes (nome, email, idade, cidade) VALUES ('Paula', 'paula@email.com', 26, 'São Paulo')")

# Inserindo dados na tabela de produtos
cursor.execute(
    "INSERT INTO produtos (nome_produto, preco_unitario) VALUES ('Cadeira', 200.00)")
cursor.execute(
    "INSERT INTO produtos (nome_produto, preco_unitario) VALUES ('Mesa', 600.00)")
cursor.execute(
    "INSERT INTO produtos (nome_produto, preco_unitario) VALUES ('Teclado', 100.00)")

# Inserindo dados na tabela de vendas
cursor.execute(
    "INSERT INTO vendas (id_cliente, id_produto, quantidade, data_venda) VALUES (1, 2, 1, '2025-02-14')")
cursor.execute(
    "INSERT INTO vendas (id_cliente, id_produto, quantidade, data_venda) VALUES (2, 1, 3, '2025-02-13')")
cursor.execute(
    "INSERT INTO vendas (id_cliente, id_produto, quantidade, data_venda) VALUES (3, 3, 2, '2025-02-12')")
cursor.execute(
    "INSERT INTO vendas (id_cliente, id_produto, quantidade, data_venda) VALUES (4, 1, 1, '2025-02-10')")
cursor.execute(
    "INSERT INTO vendas (id_cliente, id_produto, quantidade, data_venda) VALUES (5, 2, 2, '2025-02-08')")

# Commitando as alterações
conn.commit()

# Fechando a conexão
conn.close()

print("Dados inseridos com sucesso!")
