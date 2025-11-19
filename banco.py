#conexão com o banco de dados
import sqlite3
from tkinter import messagebox

def iniciar():
    try:
        with (sqlite3.connect("database.db")) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf TEXT,
                senha TEXT,
                email TEXT,
                nome TEXT,
                telefone TEXT
            )''')
            conexao.commit()

        print('Banco de dados criado com sucesso.')

    except Exception as e:
        print(f'\033[31mErro ao criar o banco de dados.\n'
              f'{e}\033[m')

def login(login, senha):
        try:
            with (sqlite3.connect("database.db")) as conexao:
                cursor = conexao.cursor()
                cursor.execute('''SELECT cpf, senha, nome FROM usuarios''')

                for usuario in cursor.fetchall():
                    if usuario[0] == login:

                        if usuario[1] == senha:
                            # LOGIN DEU CERTO
                            return True

                        else:
                            # SENHA INCORRETA
                            return False

                # USUÁRIO NÃO ENCONTRADO
                return False

        except Exception as e:
            messagebox.showerror('Erro', f'Tivemos um erro ao fazer login.\n'
                                         f'{e}')


def novoUsuario(usuario):
    try:
        with (sqlite3.connect("database.db")) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''INSERT INTO usuarios (cpf, senha, email, nome, telefone)
            VALUES (:cpf, :senha, :email, :nome, :telefone)
            ''', usuario)
            conexao.commit()

        conexao.close()

        print('Usuário cadastrado com sucesso.')

    except Exception as e:
        messagebox.showerror('Erro', 'Erro ao cadastrar usuário.\n'
              f'{e}\033[m')


def listar(tabela):
    try:
        with (sqlite3.connect("database.db")) as conexao:
            cursor = conexao.cursor()
            cursor.execute(f'''SELECT * FROM {tabela}''')
            for linha in cursor.fetchall():
                print(linha)

    except Exception as e:

        print(f'\033[31mErro ao listar {tabela}.'
              f'{e}\033[m')

iniciar()