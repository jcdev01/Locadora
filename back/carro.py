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
