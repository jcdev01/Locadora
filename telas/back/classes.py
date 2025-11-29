class Carro:
    total = 0

    def __init__(self, marca, modelo, ano, placa, diaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.diaria = diaria

        Carro.total += 1


class Usuario:
    total = 0
    
    def __init__(self, cpf, email, nome, senha, telefone):
        self.cpf = cpf
        self.email = email
        self.nome = nome
        self.senha = senha
        self.telefone = telefone

        Usuario.total += 1

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
