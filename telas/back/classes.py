class Carro:
    total = 0

    def __init__(self, marca, modelo, ano, placa, diaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.diaria = diaria

        Carro.total += 1

    def __str__(self):
        return (f'---CARRO---\n'
                f'MARCA: {self.marca}\n'
                f'MODELO: {self.modelo}\n'
                f'ANO: {self.ano}\n'
                f'PLACA: {self.placa}\n'
                f'DIARIA: R$ {self.diaria:.2f}\n')


class Usuario:
    total = 0
    
    def __init__(self, cpf, senha, email, nome, telefone):
        self.cpf = cpf
        self.senha = senha
        self.email = email
        self.nome = nome
        self.telefone = telefone

        Usuario.total += 1

    def __str__(self):
        return (f'---USUÁRIO---\n'
                f'NOME: {self.nome}\n'
                f'CPF: {self.cpf}\n'
                f'EMAIL: {self.email}\n'
                f'SENHA: {self.senha}\n'
                f'TELEFONE: {self.telefone}\n')

class Contratos:
    total = 0

    def __init__(self, cpf, placa, dataInicio, dataTermino, valor, formaPagamento):
        self.cpf = cpf
        self.placa = placa
        self.dataInicio = dataInicio
        self.dataTermino = dataTermino
        self.valor = valor
        self.formaPagamento = formaPagamento

        Contratos.total += 1
