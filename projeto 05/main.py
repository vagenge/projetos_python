"""  
    EXERCICIO 01 - pagina 117
    
    Escrever um programa em Python que solicite informações de três pessoas, 
    como nome, idade, peso e altura. Apresentar na tela estas informações de modo que permaneçam alinhados verticalmente. 
    Usar a formatação de interpolação.

"""
def exe_01():
    pessoas = []

    for x in range(1,4):
        nome = input(f'Coloque o nome da PESSOA {x}: ')
        idade = int(input(f'Coloque a idade da PESSOA {x}: '))
        peso = float(input(f'Coloque o peso da PESSOA {x}: '))
        altura = float(input(f'COloque a altura da PESSOA {x}: '))
        
        pessoa = [nome, idade, peso, altura]
        
        pessoas.append(pessoa)
        
        
    for pessoa in pessoas:
        print(f'Nome: {pessoa[0]}, idade: {pessoa[1]}, peso: {pessoa[2]}, altura: {pessoa[3]}')

"""
    EXERCICIO 02 - pagina 121
    
    Criar um programa que utilize uma estrutura de repetição for. Nesta estrutura, 
    o usuário deverá fornecer 5 nomes a serem adicionados em uma lista. No final, apresentar os nomes em ordem crescente.
    
"""

def exe_02():
    nomes = []

    for i in range(5):
        nomes.append(input(f"Escreva o nome{(i+1)}: "))

    nomes.sort()
    print(nomes)

"""
    EXERCICIO 03 - pagina 121
    Neste laboratório, uma lista de 100 números será criada de forma aleatória, 
    ou seja, os elementos serão números aleatórios.
    Escrever o programa de forma a exibir E adicionar em uma lista, apenas os valores gerados que sejam maiores que 10.
    
"""

def exe_03():
    import random as rn


    count = 0
    valores = []

    for i in range(100):
        numeoro = rn.randint(0,20)
        
        if numeoro > 10:
            count += 1
            valores.append(numeoro)
            print(f'{count} => {numeoro}')
        
    print(f'Total de numeros gerados maiores que 10: {count}')
    print(f'Valores: {valores}')


"""
    EXERCICIO 04 - pagina 121
    
    Escrever um programa que produza uma senha com 4 dígitos numéricos entre 0 e 9.
    A senha resultante deve ser uma string.
    
    Observação: cada dígito gerado deve ser concatenado com o próximo.
    
"""

def exe_04():
    
    import random as rn

    senha = ''

    for i in range(4):
        digito = str(rn.randint(0,9))
        
        senha += digito
        
        
    print(f'senha criada pelo sistema: {senha}')

"""
    EXERCICIO 05

    Neste laboratório, o usuário fornece as informações: dia, mês e ano.
    Com base nestas informações, determinar quantos dias restam para terminar o ano informado.
    Realizar as validações:
    
    => O mês informado deve estar na faixa entre 1 e 12;
    => O dia informado deve ser compatível com o mês informado;
    => Usar o ano para determinar o número de dias do mês de fevereiro. 
"""

def exe_05():
    dia = int(input('Informe o dia: '))
    mes = int(input('Informe o mês: '))
    ano = int(input('Informe o ano: '))

    fev = 29 if ano % 4 == 0 else 28

    meses = (31, fev, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    if mes < 1 or mes > 12:
        raise TypeError('O mês tem que ser entre 1 e 12')
        
    if dia < 1 or dia > meses[mes - 1]:
        raise TypeError('O dia não corresponde ao mês digitado.')
        
    dias_restantes = meses[mes - 1] - dia

    for x in range(mes, 12):
        dias_restantes += meses[x]
        
    print(f'Falta {dias_restantes} para terminar o ano')

"""
    EXERCICIO 06
    
    Este programa representa um jogo para adivinhar números. Os passos são apresentados a seguir, com um exemplo de uso:
    
    => O programa produz um número aleatório inteiro entre 1 e 100 (suponha: 49); 
    => O programa pede para o usuário: "Informe um valor entre 0 e 100": 60; 
    => Como o número informado é maior que o produzido, o programe pede: "Informe um valor entre 0 e 59": 20; 
    => Como o número informado é menor que o produzido, o programa pede: "Informe um valor entre 21 e 59"; 
    => No final, o programa apresenta o número de tentativas.
    
    Observação: se o usuário fornece um valor fora da faixa solicitada, conta como tentativa. 
"""

def exe_06():
    import random as rn

    numero_aleatorio = rn.randint(1,100)

    tentativas = 0

    min = 1
    max = 100

    while True:
        numero = int(input(f'Informe um valor entre {min} e {max}: '))
        
        tentativas += 1
        
        if numero == numero_aleatorio:
            print(f'Parabéns. Você venceu após {tentativas} tentativas')
            break
        if numero > numero_aleatorio:
            min = min
            max = numero - 1
            
        if numero < numero_aleatorio:
            min = numero + 1
            max = max


