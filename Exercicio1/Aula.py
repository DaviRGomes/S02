class Aula():
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []
        
    def adicionar_aluno(self, aluno): 
        self.alunos.append(aluno)  
    
    def listar_presenca(self):
        for aluno in self.alunos:
            print(f"Presença na aula sobre {self.nome}, aluno: {aluno.nome}")
    