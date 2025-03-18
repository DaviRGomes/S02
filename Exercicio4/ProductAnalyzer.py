from dataset.database import Database
from helper.writeAJson import writeAJson

db = Database(database="mercado", collection="compras")
#db.resetDatabase()


## EXEMPLO DE COMO FAZER >>>>
# 1- Média de gasto total:
#result = db.collection.aggregate([
#{"$unwind": "$produtos"},
#{"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
#{"$group": {"_id": None, "media": {"$avg": "$total"}}}
#])
## <<<<


# QUESTÃO 1:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total": {"$sum": "$produtos.quantidade"}}},
    {"$group": {"_id": None, "soma": {"$sum": "$total"}}}
])
writeAJson(result, "Vendas por dia")

# QUESTÃO 2:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},
    {"$sort": {"total": -1}},
    {"$limit": 1}
])
writeAJson(result, "Produto mais vendido")

# QUESTÃO 3:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$group": {"_id": "$cliente_id", "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
    {"$sort": {"total": -1}},
    {"$limit": 1}                                        
])                
                
writeAJson(result, "Cliente que mais gastou")

# QUESTÃO 4:
result = db.collection.aggregate([
    {"$unwind": "$produtos"},
    {"$match":{"produtos.quantidade":{"$gt": 1}}},
    {"$group": {"_id": "$produtos.descricao", "total": {"$sum": "$produtos.quantidade"}}},   
    {"$sort": {"total": -1}}                          
])                
                
writeAJson(result, "Produto acima de 1")