import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('vendas.db')
cursor = conn.cursor()

# Atualizando a idade de um cliente
cursor.execute("UPDATE clientes SET idade = 30 WHERE nome = 'João'")

# Commitando as alterações
conn.commit()

# Fechando a conexão
conn.close()

print("Dados atualizados com sucesso!")
