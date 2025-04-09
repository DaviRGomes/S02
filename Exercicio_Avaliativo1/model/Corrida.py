from model.Passageiro import Passageiro

class Corrida:
    def __init__(self, nota: float, distancia: float, valor: float, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro