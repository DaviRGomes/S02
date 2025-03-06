from database import Database
from helper.WriteAJson import writeAJson

db = Database(database="inatel", collection="aula")
db.resetDatabase()