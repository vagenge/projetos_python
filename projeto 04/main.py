# VARIAVEIS <= ESPACOS NA MEMORIA DO COMPUTADOR PARA ARMAZENAR INFORMACOES

# ENTRADAS E SAIDAS DE INFORMACOES <= INPUT() PRINT()

# OPERADORES <= ARITMETICOS, RELACIONAIS, LOGICOS

# ESTRUTURA CONDICIONAL <= IF, ELIF E ELSE

# COLECOES <= LISTA, TUPLA e DICIONARIOS

"""
    Suponha que em um caixa eletrônico existam cédulas 
    disponíveis de 5, 10, 20 e 50 reais.

    Se o valor nao for multiplo de 5 avisar ao usuario que a operacao nao pode ser feita.

    Usando operações de (divisão inteira) e (resto da divisão),
    escrever um programa que solicite ao usuário um valor para saque e, 
    
    a partir deste valor, armazenar em variáveis e apresentar 
    na tela a quantidade de cada cédula para compor o valor do saque.
    
    considerando que o valor de cada cédula 
    permanece armazenado em uma lista e mostrado na tela.

    obs: verificar as maiores notas primeiro.
"""


"""

saque = int(input('Coloque um valor para saque: '))

dinheiro = saque

cedulas = [] 


# condicao para realizar saque
if saque % 5 == 0:
    ced_50 = saque // 50
    cedulas.append(ced_50)
    dinheiro %= 50 # dinheiro = dinheiro % 50

    ced_20 = dinheiro // 20
    cedulas.append(ced_20)
    dinheiro %= 20

    ced_10 = dinheiro // 10
    cedulas.append(ced_10)
    dinheiro %= 10

    ced_5 = dinheiro // 5
    cedulas.append(ced_5)

    print(f'Cedulas 50: {cedulas[0]}')
    print(f'Cedulas 20: {cedulas[1]}')
    print(f'Cedulas 10: {cedulas[2]}')
    print(f'Cedulas 5: {cedulas[3]}')

# mensagem de erro caso nao ser possivel realizar saques
else:
    print('Impossivel realizar saque neste valor. Precisa ser multiplo de 5.')

import random as rn

from random  import random, randint

from random import *

# random()
# randint()

"""

# ESTRUTURA DE REPETICAO - LOOPS

# colecoes(list, tuples, dicts)

colecao = [1, 3, 4, 7, 10]

    # For

pos = 0
for x in colecao:
    #print(f'posicao: {pos}, valor: {x}')
    pos += 1



for x in range(len(colecao)): #[-10, -9,...,10]
    if colecao[x] == 4:
        #print('tem o numero quatro')
        pass


lista = ['julio', 'pereira', 20] 

tamanho = len(lista) # 2

for item in lista:
    # print(item)
    pass


for vez in range(1,10):
    pass
    #print(vez)
else:
    pass
    #print('acabou!!!')


notas = {
    'Ricardo': 8,
    'Ana': 4,
    'Vagner': 10,
    'Alan': 9,
    'Renato': 4
}

# notas['Ricardo']

for x in notas.values():
    # print(x)
    pass

for x in notas.keys():
    # print(x)   ('Ricardo', 8)
    pass

for x in notas.items():
    if x[0] == 'Ricardo':
        # print(x[1])
        pass

for chave,valor in notas.items():
    # print(f'Chave => {chave}')
    # print(f'Valor => {valor}')

    if chave != 'Ana':
       # notas[chave] = notas['Ana']
       pass


#### FOR EM STRING

string = ''

for ch in 'Julio':
    string += ch + '*'

print(string)







