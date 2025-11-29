#conexão com o banco de dados
import sqlite3
from tkinter import messagebox

def iniciar():
    try:
        with (sqlite3.connect("telas/back/database.db")) as conexao:
            cursor = conexao.cursor()

                # CRIAÇÃO DAS TABELAS
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf TEXT,
                senha TEXT,
                email TEXT,
                nome TEXT,
                telefone TEXT
            )''')
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS contratos (
                num INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf TEXT,
                carro TEXT,
                placa TEXT,
                dataInicio DATE,
                dataTermino DATE,
                valor REAL
            )''')
            conexao.commit()

        print('Banco de dados criado com sucesso.')

    except Exception as e:
        print(f'\033[31mErro ao criar o banco de dados.\n'
              f'{e}\033[m')

def login(login, senha):
        try:
            with (sqlite3.connect("telas/back/database.db")) as conexao:
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
            return None


def novoUsuario(usuario):
    try:
        with (sqlite3.connect("telas/back/database.db")) as conexao:
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

def novoContrato(contrato):
    return


def listar(tabela):
    try:
        with (sqlite3.connect("telas/back/database.db")) as conexao:
            cursor = conexao.cursor()
            cursor.execute(f'''SELECT * FROM {tabela}''')
            for linha in cursor.fetchall():
                print(linha)

    except Exception as e:

        print(f'\033[31mErro ao listar {tabela}.'
              f'{e}\033[m')
        
def cpf_existe(cpf):
    with sqlite3.connect("telas/back/database.db") as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT 1 FROM usuarios WHERE cpf = ?", (cpf,))
        resultado = cursor.fetchone()
        return resultado is not None

iniciar()
listar('usuarios')