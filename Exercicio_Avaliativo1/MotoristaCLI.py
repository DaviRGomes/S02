from model.Motorista import Motorista
from model.Corrida import Corrida
from model.Passageiro import Passageiro

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")



class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_dao):
        super().__init__()
        self.dao = motorista_dao
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)
        self.add_command("findall", self.findall_motoristas)
        self.add_command("add corrida", self.add_corrida)


    def create_motorista(self):
        nome = input("Nome do motorista: ")
        corridas = []
        
        while True:
            nota = float(input("Nota (1-5): "))
            distancia = float(input("Distância (km): "))
            valor = float(input("Valor: R$ "))
            
            print("\nDados do Passageiro:")
            p_nome = input("Nome: ")
            p_doc = input("Documento: ")
            
            passageiro = Passageiro(p_nome, p_doc)
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)
            
            continuar = input("Adicionar outra corrida? (s/n): ")
            if continuar.lower() != 's':
                break
        
        motorista = Motorista(nome, corridas)
        motorista_create = self.dao.create_motorista(motorista)

    def read_motorista(self):
        motorista_id = input("Id do motorista: ")
        motorista = self.dao.read_motorista(motorista_id)
        if motorista:
            print(f"\nId do motorista: {motorista['_id']}")
            print(f"Nome: {motorista['nome']}")
            print("Corridas:")
            for i, corrida in enumerate(motorista['corridas'], 1):
                print(f"  {i}. Nota: {corrida['nota']}, Distância: {corrida['distancia']}km, Valor: R${corrida['valor']:.2f}")
                print(f"     Passageiro: {corrida['passageiro']['nome']} Documento: {corrida['passageiro']['documento']}")
        else:
            print("Motorista não exite")

    def update_motorista(self):
        motorista_id = input("Id do motorista: ")
        nome = input("Novo nome: ")
        if self.dao.update_motorista(motorista_id, {"nome": nome}):
            print("Motorista atualizado")
        else:
            print("Motorista não existe")


    def add_corrida(self):
        motorista_id = input("Id do motorista: ")

        nota = float(input("Nota da corrida: "))
        distancia = float(input("Distância (km): "))
        valor = float(input("Valor (R$): "))
        nome_passageiro = input("Nome do passageiro: ")
        doc_passageiro = input("Documento do passageiro: ")

        nova_corrida = {
            "nota": nota,
            "distancia": distancia,
            "valor": valor,
            "passageiro": {
                "nome": nome_passageiro,
                "documento": doc_passageiro
            }
        }

        if self.dao.add_corrida(motorista_id, [nova_corrida]):
            print("Corrida adicionada com sucesso.")
        else:
            print("Erro ao adicionar corrida.")      

    def delete_motorista(self):
        motorista_id = input("Id do motorista: ")
        if self.dao.delete_motorista(motorista_id):
            print("Motorista deletado")
        else:
            print("Motorista não existe")

    def findall_motoristas(self):
        motoristas = self.dao.findAll_motoristas()
        if motoristas:
            print("\nLista de Motoristas:")
            for motorista in motoristas:
                print(f"Id: {motorista['_id']} - Nome: {motorista['nome']} ({len(motorista['corridas'])} corridas)")
        else:
            print("Nenhum motorista encontrado")

    def run(self):
        print("Boas vindas ao  Vale Driver CLI!")
        print("Comandos de entrada do CRUD: create, read, update, delete, quit, findall and add corrida")
        super().run()