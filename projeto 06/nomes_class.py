

class Nome:
    
    # construtor => obriga instanciar com os valores
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    # Pegar propriedade nome   
    @property
    def nome(self):
        return self.__nome
    
    # gravar na atributo nome
    @nome.setter
    def nome(self, v_nome):
        self.__nome = v_nome
        
    # Pegar propriedade sobrenome
    @property
    def sobrenome(self):
        return self.__sobrenome
    
    # gravar na atributo sobrenome
    @sobrenome.setter
    def sobrenome(self, v_sobrenome):
        self.__sobrenome = v_sobrenome
        
    # funcao que returna o nome maiusculo
    def nome_maiusculo(self):
        return self.nome.upper()
        
    
    

aluno1 = Nome("Julio", "Pereira")


print(aluno1.nome)
print(aluno1.sobrenome)
print(aluno1.nome_maiusculo())
        