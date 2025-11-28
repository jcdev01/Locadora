class Carro:
    total = 0
    disponiveisAgora = 0

    def __init__(self, marca, modelo, ano, cambio, portas, placa, diaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cambio = cambio
        self.portas = portas
        self.placa = placa
        self.diaria = diaria

        Carro.total += 1
        Carro.disponiveisAgora += 1
class Usuario:
    total = 0
    
    def __init__(self, cpf, email, nome, senha, telefone):
        self.cpf = cpf
        self.email = email
        self.nome = nome
        self.senha = senha
        self.telefone = telefone
class Contratos:
    total = 0

    def __init__(self, cpf, placa, dataInicio, dataTermino):
        self.cpf = cpf
        self.placa = placa
        self.dataInicio = dataInicio
        self.dataTermino = dataTermino



