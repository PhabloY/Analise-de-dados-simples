import sqlite3

# Conectando ou criando o banco de dados SQLite
# Cria ou abre o banco de dados chamado 'vendas.db'
conn = sqlite3.connect('vendas.db')

# Criando um cursor para executar os comandos SQL
cursor = conn.cursor()

# Criando a tabela de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    idade INTEGER,
    cidade TEXT
)
''')

# Criando a tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_produto TEXT,
    preco_unitario REAL
)
''')

# Criando a tabela de vendas
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER,
    id_produto INTEGER,
    quantidade INTEGER,
    data_venda TEXT,
    FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
    FOREIGN KEY(id_produto) REFERENCES produtos(id_produto)
)
''')

# Commitando as alterações
conn.commit()

# Fechando a conexão
conn.close()
