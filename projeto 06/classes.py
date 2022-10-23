

from importlib.util import module_for_loader


nome, idade, peso, altura = '', 0, 0.0, 0.0

# pegar estas informacoes de tres pessoas.


#classe <= Abstracao
class Pessoa: 
    # (atributos e methodos)
    pass 

# Objeto <= Elemento
pessoa1 = Pessoa()
pessoa2 = Pessoa()
pessoa3 = Pessoa()

########################



"""
class Calculadora:
    
    @property
    def operador(self):
        return self.__operador
    
    @operador.setter
    def operador(self, c_operador):
        self.__operador = c_operador
        
soma = Calculadora()

soma.operador = '+'

print(soma.operador)
"""

#definicao da classe automovel

class Automovel:
    
    #ler propriedade
    @property
    def marca(self):
        return self.__marca
    
    # gravar na propriedade
    @marca.setter
    def marca(self, p_marca):
        self.__marca = p_marca
    
        
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, p_modelo):
        self.__modelo = p_modelo
        
        
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, p_ano):
        self.__ano = p_ano
        
    def getLinha(self):
        linha = f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}'
        return linha
    
        
carro_bwm = Automovel() # "bmw" NO argument

carro_bwm.marca = "bmw"
carro_bwm.modelo = "a30"
carro_bwm.ano = 2010

# print(carro_bwm.getLinha())


carro_gol = Automovel()

carro_gol.marca = 'VW'
carro_gol.modelo = 'Gol'
carro_gol.ano = 2022

# print(carro_gol.getLinha())



class Auto:
    
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    #ler propriedade
    @property
    def marca(self):
        return self.__marca
    
    # gravar na propriedade
    @marca.setter
    def marca(self, p_marca):
        self.__marca = p_marca
    
        
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, p_modelo):
        self.__modelo = p_modelo
        
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, p_ano):
        self.__ano = p_ano
        
    def getLinha(self):
        linha = f'Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}'
        return linha


auto = Auto("Fiat", "Ford KA", 2010)

print(auto.marca)