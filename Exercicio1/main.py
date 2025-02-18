from Aluno import Aluno
from Aula import Aula
from Professor import Professor
        
aluno1 = Aluno("Davi")
aluno2 = Aluno("João")
professor1 = Professor("Jonas")
aula = Aula("POO")

aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.listar_presenca()
professor1.ministrar_aula(aula)
