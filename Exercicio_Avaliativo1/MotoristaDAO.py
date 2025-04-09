from bson import ObjectId
from typing import Dict, List, Optional
from model.Motorista import Motorista
from bson import ObjectId
from pymongo.results import UpdateResult

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista: Motorista) -> str:
        motorista_data = {
            "nome": motorista.nome,
            "corridas": [{
                "nota": corrida.nota,
                "distancia": corrida.distancia,
                "valor": corrida.valor,
                "passageiro": {
                    "nome": corrida.passageiro.nome,
                    "documento": corrida.passageiro.documento
                }
            } for corrida in motorista.corridas]
        }

        result = self.db.collection.insert_one(motorista_data)
        print(f"Nome do motorista: {motorista.nome}")
        print(f"Id do motorista: {str(result.inserted_id)}")
        return str(result.inserted_id)
    
    def add_corrida(self, motorista_id: str, corridas: List[Dict]) -> bool:
        if not corridas:
            return False

        result = self.db.collection.update_one(  # <- aqui está o fix
            {"_id": ObjectId(motorista_id)},
            {"$push": {"corridas": {"$each": corridas}}}
        )
        return result.modified_count > 0



    def read_motorista(self, motorista_id: str) -> Optional[Dict]:
        return self.db.collection.find_one({"_id": ObjectId(motorista_id)})

    def update_motorista(self, motorista_id: str, update_data: Dict) -> bool:
        result = self.db.collection.update_one(
            {"_id": ObjectId(motorista_id)},
            {"$set": update_data}
        )
        return result.modified_count > 0

    def delete_motorista(self, motorista_id: str) -> bool:
        result = self.db.collection.delete_one({"_id": ObjectId(motorista_id)})
        return result.deleted_count > 0

    def findAll_motoristas(self) -> List[Dict]:
        return list(self.db.collection.find())
    
