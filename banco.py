#conexão com o banco de dados
import sqlite3





def iniciar():
    try:
        with (sqlite3.connect("database.db")) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT NOT NULL,
                senha TEXT NOT NULL,
                email TEXT NOT NULL,
                nome TEXT NOT NULL,
                cpf TEXT NOT NULL UNIQUE,
                telefone TEXT NOT NULL
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
                cursor.execute('''SELECT login, senha, nome FROM usuarios''')

                for usuario in cursor.fetchall():
                    if usuario[0] == login:
                        if usuario[1] == senha:
                            print(f'Bem-vindo(a) {usuario[2]}!')
                            return
                        else:
                            print('\033[31mSenha incorreta. \033[m')
                            return

                print('\033[31mUsuário não encontrado.\033[m')

        except Exception as e:
            print(f'\033[31mTivemos um erro ao fazer login.\n'
                  f'{e}\033[m')


def novoUsuario(senha,email,nome,cpf,telefone,login):
    usuario = {
        'senha': senha,
        'email': email,
        'nome': nome,
        'cpf': cpf,
        'telefone': telefone,
        'login': login,
    }

    try:
        with (sqlite3.connect("database.db")) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''INSERT INTO usuarios (login, senha, email, nome, cpf, telefone)
            VALUES (:login, :senha, :email, :nome, :cpf, :telefone)
            ''', usuario)
            conexao.commit()

        conexao.close()

        print('Usuário cadastrado com sucesso.')

    except Exception as e:
        print(f'\033[31mErro ao cadastrar usuário. Tente novamente\n'
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
