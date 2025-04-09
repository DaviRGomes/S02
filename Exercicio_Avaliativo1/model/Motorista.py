from typing import List
from model.Corrida import Corrida

class Motorista:
    def __init__(self, nome: str, corridas: List[Corrida] = None):
        self.nome = nome
        self.corridas = corridas if corridas else []