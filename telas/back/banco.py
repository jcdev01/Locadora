#conexão com o banco de dados
import sqlite3
from tkinter import messagebox

from PIL.TiffImagePlugin import DATE_TIME

from Locadora.telas.back.classes import *
import Locadora.session as session
from Locadora.telas.back.classes import Usuario, Carro
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def iniciar():
    try:
        with (sqlite3.connect(DB_PATH)) as conexao:
            cursor = conexao.cursor()

                # CRIAÇÃO DAS TABELAS
            cursor.executescript('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf TEXT,
                senha TEXT,
                email TEXT,
                nome TEXT,
                telefone TEXT
            );

            CREATE TABLE IF NOT EXISTS contratos (
                num INTEGER PRIMARY KEY AUTOINCREMENT,
                cpf TEXT,
                carro TEXT,
                placa TEXT,
                dataInicio DATE,
                dataTermino DATE,
                valor REAL,
                formaPagamento TEXT
            );

            CREATE TABLE IF NOT EXISTS carros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                marca TEXT,
                modelo TEXT,
                ano INTEGER,
                placa TEXT,
                diaria REAL
            );
            ''')
            conexao.commit()

        print('Banco de dados criado com sucesso.')

    except Exception as e:
        print(f'\033[31mErro ao criar o banco de dados.\n'
              f'{e}\033[m')

def login(login, senha):
    try:
        with (sqlite3.connect(DB_PATH)) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
            SELECT * FROM usuarios 
            WHERE cpf = ? AND senha = ?''', (login, senha))
            usuario = cursor.fetchone()


            if usuario is None:
                # SENHA INCORRETA
                return False

            # LOGIN DEU CERTO
            session.usuarioLogado = Usuario(
                cpf=usuario[1],
                senha=usuario[2],
                email=usuario[3],
                nome=usuario[4],
                telefone=usuario[5])
            print('Login realizado com sucesso!\n', session.usuarioLogado)
            return True

    except Exception as e:
        messagebox.showerror('Erro', f'Tivemos um erro ao fazer login.\n'
                                     f'{e}')
        return None


def novoUsuario(usuario):
    try:
        with (sqlite3.connect(DB_PATH)) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''INSERT INTO usuarios (cpf, senha, email, nome, telefone)
            VALUES (:cpf, :senha, :email, :nome, :telefone)
            ''', usuario)
            conexao.commit()

        conexao.close()

        session.usuarioLogado = Usuario(
            cpf=usuario['cpf'],
            senha=usuario['senha'],
            email=usuario['email'],
            nome=usuario['nome'],
            telefone=usuario['telefone']
        )

        print('Usuário cadastrado com sucesso.')

    except Exception as e:
        messagebox.showerror('Erro', 'Erro ao cadastrar usuário.\n'
              f'{e}\033[m')


def novoCarro(carro):
    try:
        dados = carro.__dict__

        with (sqlite3.connect(DB_PATH)) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''INSERT INTO carros (marca, modelo, ano, placa, diaria)
            VALUES (:marca, :modelo, :ano, :placa, :diaria)
            ''', dados)
            conexao.commit()

        conexao.close()
        print('Carro cadastrado com sucesso.')

    except Exception as e:
        print(f'\033[31mErro ao salvar o carro.\n'
              f'{e}\033[m')


def novoContrato(contrato):
    try:
        dados = contrato.__dict__

        with (sqlite3.connect(DB_PATH)) as conexao:
            cursor = conexao.cursor()

            cursor.execute('''
            INSERT INTO contratos (cpf, carro, placa, dataInicio, dataTermino, valor, formaPagamento)
            VALUES (:cpf, :carro, :placa, :dataInicio, :dataTermino, :valor, :formaPagamento)
            ''', dados)
            conexao.commit()

        conexao.close()

        print('Contrato criado com sucesso.')
        print(contrato)
    except Exception as e:
        print(f'\033[31mErro ao salvar o contrato.\n'
              f'{e}\033[m')

def escolherCarro(placa):
    try:
        with sqlite3.connect(DB_PATH) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
            SELECT * FROM carros WHERE placa = ?
            ''', (placa,))

            carro = cursor.fetchone()

            if carro is None:
                return

            session.carroEscolhido = Carro(
                marca=carro[1],
                modelo=carro[2],
                ano=carro[3],
                placa=carro[4],
                diaria=carro[5],
            )


    except Exception as e:
        print(f'\033[31mErro ao escolher o carro.\n'
              f'{e}\033[m')

def escolherContrato(num):
    try:
        with sqlite3.connect(DB_PATH) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
            SELECT * FROM contratos WHERE num = ?
            ''', (num,))

            contratoTupla = cursor.fetchone()

            if contratoTupla is None:
                return

            contrato = Contrato(
                num=contratoTupla[0],
                cpf=contratoTupla[1],
                carro=contratoTupla[2],
                placa=contratoTupla[3],
                dataInicio=contratoTupla[4],
                dataTermino=contratoTupla[5],
                valor=contratoTupla[6],
                formaPagamento=contratoTupla[7]
            )

            return contrato

    except Exception as e:
        print(f'\033[31mErro ao escolher o contrato.\n'
              f'{e}\033[m')

def contratosSalvos():
    '''
    FUNÇÃO QUE RETORNA TODOS OS NÚMEROS, EM UMA LISTA, DOS CONTRATOS
    JÁ SALVOS ANTERIORMENTE

    listaNum = contratosSalvos()
    '''

    try:
        with sqlite3.connect(DB_PATH) as conexao:
            cursor = conexao.cursor()
            cursor.execute('''
            SELECT num FROM contratos
            ''')
            numeros = []
            lista = cursor.fetchall()

            for tupla in lista:
                numeros.append(tupla[0])

            return numeros

    except Exception as e:
        print(f'\033[31mErro ao listar os números dos contratos.\n'
              f'{e}\033[m')


def listar(tabela):
    try:
        print(f'---------------{tabela}---------------')
        with (sqlite3.connect(DB_PATH)) as conexao:
            cursor = conexao.cursor()
            cursor.execute(f'''SELECT * FROM {tabela}''')
            for linha in cursor.fetchall():
                print(linha)

    except Exception as e:

        print(f'\033[31mErro ao listar {tabela}.'
              f'{e}\033[m')

        
def cpf_existe(cpf):
    with sqlite3.connect(DB_PATH) as conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT 1 FROM usuarios WHERE cpf = ?", (cpf,))
        resultado = cursor.fetchone()
        return resultado is not None



iniciar()