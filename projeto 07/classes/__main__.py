

# CLASSES e OBJETOS

    #HERANCA

class Pessoa:
    # construtor da classe == obriga quando instaciar colocar os valores das propriedades
    def __init__(self, nome):
        self.nome = nome
    
    # propriedade nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, v_nome):
        self.__nome = v_nome
    
    # Metodo que coloca o nome em maiusculo
    def nome_maiusculo(self):
        return self.nome.upper()
        

#heranca
class Aluno(Pessoa):
    # pass
    def __init__(self, nome, turma):
        super().__init__(nome) # polimorfismo
        self.turma = turma

    @property
    def turma(self):
        return self.__turma
    
    @turma.setter
    def turma(self, v_turma):
        self.__turma = v_turma
        
    def nome_e_turma_em_maiusculo(self):
        nome_em_maiusculo = super().nome_maiusculo() # polimorfismo de metodos
        turma_em_maiusculo = self.turma.upper()
        
        linha = f'Nome: {nome_em_maiusculo}, Turma: {turma_em_maiusculo}'
        
        return linha
        
        

aluno1 = Aluno('Ricardo', 'Programando em Python')

print(aluno1.nome)
print(aluno1.nome_maiusculo())
print(aluno1.turma)
print(aluno1.nome_e_turma_em_maiusculo())

