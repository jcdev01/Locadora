class Carro:

    def __init__(self, marca, modelo, ano, placa, diaria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.diaria = diaria

    def __str__(self):
        return (f'---CARRO---\n'
                f'MARCA: {self.marca}\n'
                f'MODELO: {self.modelo}\n'
                f'ANO: {self.ano}\n'
                f'PLACA: {self.placa}\n'
                f'DIARIA: R$ {self.diaria:.2f}\n')
    def __int__(self,onix_retro,onix_sedan,mobi,kwid,civic,tracker):
        self.onix_retro=onix_retro
        self.onix_sedan=onix_sedan
        self.mobi=mobi
        self.civic=civic
        self.kwid=kwid
        self.tracker=tracker




class Usuario:

    def __init__(self, cpf, senha, email, nome, telefone):
        self.cpf = cpf
        self.senha = senha
        self.email = email
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return (f'---USUÁRIO---\n'
                f'NOME: {self.nome}\n'
                f'CPF: {self.cpf}\n'
                f'EMAIL: {self.email}\n'
                f'SENHA: {self.senha}\n'
                f'TELEFONE: {self.telefone}\n')

class Contrato:

    def __init__(self, num, cpf, carro, placa, dataInicio, dataTermino, valor, formaPagamento):
        self.num = num
        self.cpf = cpf
        self.carro = carro
        self.placa = placa
        self.dataInicio = dataInicio
        self.dataTermino = dataTermino
        self.valor = valor
        self.formaPagamento = formaPagamento

    def __str__(self):
        return (f'---CONTRATO---\n'
                f'CPF: {self.cpf}\n'
                f'CARRO: {self.carro}\n'
                f'PLACA: {self.placa}\n'
                f'DATA INICIAL: {self.dataInicio}\n'
                f'DATA FINAL: {self.dataTermino}\n'
                f'VALOR: {self.valor}\n'
                f'FORMA PAGAMENTO: {self.formaPagamento}\n')