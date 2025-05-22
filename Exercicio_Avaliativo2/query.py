from database import Database

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://54.81.133.90:7687", "neo4j", "wills-greenwich-architecture")

#Questão 1:
print("Questão 1")
#   Letra A)
query = """MATCH (t:Teacher {name: 'Renzo'})
RETURN t.ano_nasc AS ano_nascimento, t.cpf AS cpf"""
print(db.execute_query(query))


#   Letra B)
query = """MATCH (t:Teacher)
WHERE t.name STARTS WITH 'M'
RETURN t.name AS nome, t.cpf AS cpf"""
print(db.execute_query(query))


#   Letra C)
query = """MATCH (c:City)
RETURN c.name AS nome_cidade"""
print(db.execute_query(query))


#   Letra D)
query = """MATCH (s:School)
WHERE s.number >= 150 AND s.number <= 550
RETURN s.name AS nome_escola, s.address AS endereco, s.number AS numero"""
print(db.execute_query(query))


#Questão 2:
print("Questão 2")
#   Letra A)
query = """MATCH (t:Teacher)
RETURN min(t.ano_nasc) AS mais_velho, max(t.ano_nasc) AS mais_jovem"""
print(db.execute_query(query))


#   Letra B)
query = """MATCH (c:City)
RETURN avg(c.population) AS media_habitantes"""
print(db.execute_query(query))


#   Letra C)
query = """MATCH (c:City {cep: '37540-000'})
RETURN replace(c.name, 'a', 'A') AS nome_modificado"""
print(db.execute_query(query))


#   Letra D)
query = """MATCH (t:Teacher)
RETURN substring(t.name, 2, 1) AS terceira_letra"""
print(db.execute_query(query))