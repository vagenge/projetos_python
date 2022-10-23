"""
Escrever um programa em Python que solicite informações de três produtos, 
como nome, quantidade, preco e esta_ativo. 
Apresentar na tela estas informações de modo que permaneçam alinhados verticalmente. 
Usar a formatação de interpolação.

"""

"""
pegar o nome1 do produto e armazenar na memoria.
pegar a quantidade1 do produto e armazenar na memoria
pegar a preco1 do produto e armazenar na memoria
pegar a esta_ativo1 do produto e armazenar na memoria

pegar o nome2 do produto e armazenar na memoria.
pegar a quantidade2 do produto e armazenar na memoria
pegar a preco2 do produto e armazenar na memoria
pegar a esta_ativo2 do produto e armazenar na memoria

pegar o nome3 do produto e armazenar na memoria.
pegar a quantidade3 do produto e armazenar na memoria
pegar a preco3 do produto e armazenar na memoria
pegar a esta_ativo3 do produto e armazenar na memoria

mostrar vertcalmente

nome_1 = input('Coloque o nome do produto 1: ') # str
quantidade_1 = int( input('Coloque a quantidade do produto 1: ') ) #int
preco_1 = float( input('Coloque o preco do produto 1: ') ) #float
esta_ativo_1 = bool( input('Coloque True ou False para o produto 1: ') ) #bool

# print('Produto 01: ', nome_1, ' - ', quantidade_1, ' - ', preco_1, ' - ', esta_ativo_1)
print(f'Produto 01: {nome_1} - qtd: {quantidade_1} - R$ {preco_1} - Ativo: {esta_ativo_1}')
"""


# OPERADORES

n1 = 100
n2 = 20
n3 = 30
n4 = 50
n5 = 39
n6 = 10


## Aritmeticos

op_1 = n1 / n3  # Divisao real 100/30 = 3.333333...
op_2 = n1 // n3 # Divisao Inteira 100/30 = 3
op_3 = n1 % n3 # Resto da divisão inteira

op_4 = n1 + n4 # somar
op_5 = n1 - n4 # subtrair
op_6 = n1 / n4 # divisao
op_7 = n1 * n4 # produto


n6 += 10.9 #n6 = n6 + 10
n6 -= 10 # n6 = n6 - 10
n6 /= 10 # n6 = n6 / 10
n6 *= 10 # n6 = n6 * 10


# Operadores relacionais

 # == iguais
 # != diferentes
 # > maior
 # >= maior igual
 # < menor
 # <= menor igual

op_8 = 100 >= 100


# ESTRUTURA CONDICIONAL

qtd =  0 #input('Coloque a quantidade do produto: ')
preco = 0 #input('Coloque o preco do produto: ')

qtd = int(qtd)
preco = float(preco)

    # se o qtd que o usuario colocar for <= 0 mostre para o cliente mensagem

if qtd <= 0:
    qtd = 1
    #print(f'A quantidade atualizou para {qtd}')
else:
    lucro = preco * qtd
    #print(f'O lucro total sera de: {lucro}')


# < 7  REP , > 7.9 APR, REC

media_final = 8

"""
if media_final < 7:
    print('esta reprovado!')
elif media_final > 7.9:
    print('esta aprovado!')
else:
    print('esta em recuperacao!')

"""

# Operadores logicos (and, or, not)

if media_final < 7:
    print('esta reprovado!')
elif media_final >= 7 and media_final < 8:
    print('esta em recuperacao!')
else:
    print('esta aprovado!')




# COLECOES

numero = 12

minha_lista = [12, 13, 14, 15, 'julio', True]

minha_tupla = (12, 13, 14, 15, 'julio', True)

meu_dicionario = {"chave":"valor", "produto": "Bermuda", "preco": 20.80}









    












