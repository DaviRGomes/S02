from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

# Função para consultar o grafo com base no nome e capturar labels dinâmicos
def GetFamilyGradle(tx, name):
    query = f"""
    MATCH (n {{name: '{name}'}})
    RETURN n AS pessoa, labels(n) AS labels
    """
    print(f"Consulta gerada: {query}") 
    try:
        result = tx.run(query)
        return [{
            'name': row['pessoa']['name'],
            'sexo': row['pessoa']['sexo'],
            'idade': row['pessoa']['idade'],
            'especialidade': row['pessoa']['especialidade'],
            'raça':row['pessoa']['raça'],
            'labels': row['labels']
        } for row in result] # TRANSFORMA EM DICT
    except ServiceUnavailable as exception:
        print(f"{query} raised an error: \n {exception}")
        raise
def GetLabel(tx, label):
    query = """
    MATCH (n)
    WHERE $label IN labels(n)
    RETURN n.name AS nome, n.sexo AS sexo, n.idade AS idade, n.especialidade AS especialidade, n.raça AS raça;
    """
    print(f"Consulta gerada: {query}") 
    try:
        result = tx.run(query, {"label": label})
        return [dict(record) for record in result]
    except ServiceUnavailable as exception:
        print(f"{query} raised an error: \n {exception}")
        raise
def GetRelationships(tx, relationship_type):
    query = f"""
    MATCH (a)-[r:{relationship_type}]->(b)
    RETURN a.name AS origem, type(r) AS relacionamento, r.desde AS ano, b.name AS destino;
    """
    result = tx.run(query)
    return [dict(record) for record in result]
def main():
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "12121212"

    driver = GraphDatabase.driver(uri, auth=(user, password))

    # while True:
    #     print("\n--- Menu de Consulta ao Grafo ---")
    #     print("1. Consultar pessoa ou objeto no grafo")
    #     print("2. Consulta por label")
    #     print("3. Sair")
    #     opcao = input("Escolha uma opção: ")

    #     if opcao == "1":

    #         name = input("Digite o nome do nó (ex.: Davi, Rex): ")

    #         with driver.session() as session:
    #             result = session.execute_read(GetFamilyGradle, name)
    #             if result:
    #                 print("\nResultados encontrados:")
    #                 for pessoa in result:
                       
    #                     labels_str = ", ".join(pessoa['labels'])
    #                     if pessoa['especialidade']:
    #                         print(f"Nome: {pessoa['name']}, Sexo: {pessoa['sexo']}, Idade: {pessoa['idade']}, Labels: {labels_str}, Especialidade: {pessoa['especialidade']}")
    #                     elif pessoa['labels'][0] == "Cachorro":
    #                         print(f"Nome do cachorro {pessoa['name']}, idade {pessoa['idade']}, sexo {pessoa['sexo']}, raça {pessoa['raça']}")
    #                     else:
                            
    #                         print(f"Nome: {pessoa['name']}, Sexo: {pessoa['sexo']}, Idade: {pessoa['idade']}, Labels: {labels_str}")
    #             else:
    #                 print("\nNenhum resultado encontrado.")
    #     elif opcao == "2":
    #         label = input("Digite a label (ex.: Pessoa, Engenheiro, Aposentados): ")

    #         with driver.session() as session:
    #             result = session.execute_read(GetLabel, label)
    #             if result:
    #                 print("\nNós encontrados:")
    #                 for node in result:
    #                     print(f"Nome: {node['nome']}, Sexo: {node['sexo']}, Idade: {node['idade']}")
    #             else:
    #                 print("\nNenhum nó encontrado com a label especificada.")
    #     elif opcao == "3":
    #         print("Saindo do programa...")
    #         break
    #     else:
    #         print("Opção inválida. Tente novamente.")

    with driver.session( ) as sessions:

        print("Engenheiros da familia")
        result = sessions.execute_read(GetLabel, "Engenheiro")
        for pessoa in result:
            print(f"Nome {pessoa['nome']}, idade {pessoa['idade']}")

        
        print("\nPessoas aposentadas da familia")
        result = sessions.execute_read(GetLabel, "Aposentado")
        for pessoa in result:
            print(f"Nome {pessoa['nome']}, idade {pessoa['idade']}")


        print("\nMostrando o relacionamento de Neto")
        relationships = sessions.execute_read(GetRelationships, "NETO_DE")
        for rel in relationships:
            print(f"{rel['origem']} {rel['relacionamento']} {rel['destino']}")


        print("\nMostrando os casamentos")
        relationships = sessions.execute_read(GetRelationships, "CASADO_COM")
        for rel in relationships:
            print(f"{rel['origem']} {rel['relacionamento']}  {rel['destino']} desde {rel['ano']}")


        print("\nMostrando os cachorros")
        cachorro = sessions.execute_read(GetLabel, "Pastor")
        for dog in cachorro:
            print(f"Nome do cachorro {dog['nome']} , idade {dog['idade']} e raça {dog['raça']}")
        
        print("\nMostrando os tipos de cachorros da família")
        relationships = sessions.execute_read(GetRelationships, "TIO_DE")
        for rel in relationships:
            print(f"{rel['origem']} {rel['relacionamento']} {rel['destino']}")

        print("\nMostrando os advogados")
        relationships = sessions.execute_read(GetLabel, "Advogado")
        for rel in relationships:
            print(f"{rel['nome']} {rel['idade']}")

        print("\nMostrando os irmãos da família")
        relationships = sessions.execute_read(GetRelationships, "IRMÃO_DE")
        for rel in relationships:
            print(f"{rel['origem']} {rel['relacionamento']} {rel['destino']}")


      
        

    driver.close()

if __name__ == "__main__":
    main()
