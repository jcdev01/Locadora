import sqlite3

# abre o banco
conexao = sqlite3.connect("back/database.db")
cursor = conexao.cursor()

# mostra as tabelas existentes
print("Tabelas no banco:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# mostra todos os usuários cadastrados
print("\nUsuários cadastrados:")
cursor.execute("SELECT * FROM usuarios;")
for linha in cursor.fetchall():
    print(linha)

conexao.close()
