
#  variaveis, condicao, loops, modulos

# funcoes, classes e objetos

# FUNCAO

# definicao de funcao


def imprimir_na_tela():
    print('executando a funcao imprimir_na_tela')
    
# chamar a funcao
#imprimir_na_tela()


# definicao de funcao que retorna
def imprimir_na_tela_1():
    return 'executando a funcao imprimir_na_tela'
    
# chamar a funcao que returna
# texto = imprimir_na_tela_1()
# print(texto)

def somar(num_1, num_2): # '2', '8'
    if type(num_1) is not int and type(num_2) is not int:
        return 'precisa ser do tipo inteiro'
    else:
        return num_1 + num_2

v1 = somar('2', '8')

# print(v1)


        # inferencia de tipo => serve para acessarmos metodos dos tipos
def colocar_nome_maiusculo(nome: str):
    print(nome.upper())

# colocar_nome_maiusculo('julio cezar')


        # parametro opcional

def definir_valor(preco, quantidade=1): # quantidade e opcional.
    total = quantidade * preco
    print(f'o total de {quantidade} e: {total}')
    
# definir_valor(10)


    # ARGS e KARGS
    
#args
def calcular_divida(*args): # (12, 45, 30)
    
    soma = 0
    
    for valor in args:
        soma += valor
        
    print(f'o total a pagar e: {soma}')
    

# calcular_divida(80,45,30, 30, 40 ,50)

 
# funcao sem o KARGS  
def pegar_chave_valor(preco, taxas):
    p_taxa = 0
    
    v_taxa = taxas.get('taxa1') # None
    
    if v_taxa != None:
        p_taxa = preco * v_taxa / 100
    
    print(p_taxa)
    

#pegar_chave_valor(100, {'taxa1': 20, 'imposto': 18})


#kargs

def calcular_preco_final(preco,**kargs): # taxa=10
    
    p_taxa = 0
    
    v_taxa = kargs.get('taxa1') # ['taxa']
    
    if v_taxa != None:
        p_taxa = preco * v_taxa / 100
    
    print(p_taxa)
    

# calcular_preco_final(100, taxa1=20, imposto=18, icms=30)


# FUNCAO QUE RETURNA VARIOS VALORES

def mostrar_analises(s: str):
    
    quant_a = s.count('a')
    maiusculo = s.upper()
    tamanho = len(s)
    
    return quant_a, maiusculo, tamanho
    

v1,v2,v3 = mostrar_analises('Ana Ricardo Alan')
   
# print(v1)
# print(v2)
# print(v3)


# programacao funcional

#lambda

def soma(x):
    return x + 10

#valor = soma(20)

valor = lambda x: x + 10

#print(valor(20))

# ==========

def em_maiusculo(x: str):
    return x.capitalize()

cap = lambda x: em_maiusculo(x) 

# print(cap('julio'))

import nomes_class



