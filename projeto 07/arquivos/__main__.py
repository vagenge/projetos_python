
# criando arquivo

alunos = ['Ricardo', 'Vagner', 'Renato', 'Ana', 'Alan']

arquivo = open('dados.txt', 'w')

# arquivo.write('gravando informacao 123') # gravando apenas uma linha

for x in alunos:
    arquivo.write(f'Aluno: {x}\n')

arquivo.close()


# Ler arquivo

file = open('dados.txt', 'r')

conteudo = ''

for x in file:
    # print(x)
    conteudo += x

file.close()
# print(conteudo)

# metodo READ
arquivo = open('conteudo.txt')

texto = arquivo.read(2)

#print(texto)

# metodo TELL
posicao = arquivo.tell()

#print(posicao)

texto1 = arquivo.read(6)

#print(texto1)

"""
# Verificando se a palavra Python Existe no arquivo

palavra = ''
palavras = []

for x in arquivo.read():
    if x != ' ':
        palavra += x
    else:
        palavras.append(palavra)
        palavra = ''

if palavras.count('Python') > 0:
    print('tem a palavra')
        
"""

arquivo.close()


import os

# Renomeia arquivo

# os.rename('dados.txt', 'dados_1.txt') => Renomeia arquivo
# os.remove('dados_1.txt') => remove arquivo
# os.mkdir('dados') => cria pasta
# os.rmdir('dados_1') => pasta

x = os.path.exists('dados1.txt') # verifica se o arquivo existe
y = os.path.isdir('dados.txt') # verifica se e um diretorio
z = os.path.isfile('dados.xlsx') # verifica se e um arquivo

# print(x)
# print(y)
# print(z)
