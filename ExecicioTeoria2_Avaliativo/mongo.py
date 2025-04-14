import threading
import time
import random
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
db = client['bancoiot']
sensores = db.sensores

# result = sensores.find({"name.common": {"$regex" :"^A.*r"}})
# for doc in result:
#     print(doc['name']['common'])
def sense(nome, intervalo):
    while True:
        sensor = sensores.find_one({"nomeSensor": nome})

        if sensor:
            sensorAlarmado = sensor["sensorAlarmado"]
            
        else:
            print("Sensor não encontrado!")

              
        # Verifica a temperatura
        if sensorAlarmado:
           print(f"Atenção! Temperatura muito alta! Verificar Sensor {nome}!")
           break
        else:
            temperatura = round(random.uniform(0, 38.001), 4)

            result = sensores.update_one(
                {"nomeSensor": nome},
                {
                    "$set": {
                        "sensorValor": temperatura,  
                        "sensorAlarmado": temperatura > 38 
                    }
                }
            )
            print(f"{sensor['nomeSensor']} - Temperatura: {temperatura}°C, Sensor Alarmado: {temperatura > 38}")

        time.sleep(intervalo)

# Cria threads para simular sensores
sensor1 = threading.Thread(target=sense, args=("Temp 1", 1))
sensor2 = threading.Thread(target=sense, args=("Temp 2", 1))
sensor3 = threading.Thread(target=sense, args=("Temp 3", 1))

# Inicia as threads
sensor1.start()
sensor2.start()
sensor3.start()
