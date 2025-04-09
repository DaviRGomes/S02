from Database import Database
from MotoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

db = Database(database="Av1_ValeDriver", collection="Motoristas")
motoristaDAO = MotoristaDAO(database=db)


MotoristaCLI = MotoristaCLI(motoristaDAO)
MotoristaCLI.run() 