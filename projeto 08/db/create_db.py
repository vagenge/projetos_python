from conexao import conexao_db

# captar infomacoes
foto = 'https://cdn.pixabay.com/photo/2021/06/25/13/22/girl-6363743_960_720.jpg'
nome = input('Nome: ')
turma = input('Turma: ')
media = float(input('Media'))

situacao = 'Aprovado' if media > 6.9 else 'Reprovado'
ativo = 1

# conectar ao banco de dados
conn = conexao_db('kasolution')[1]

# pegar o cursor
cur = conn.cursor()

# query sql
sql = 'INSERT INTO alunos(foto, nome, turma, media, situacao, ativo) VALUES (%s, %s, %s, %s, %s, %s)'

# executar sql
cur.execute(sql, [foto, nome, turma, media, situacao, ativo])

# comitar para inserir
conn.commit()

#fechar conexao com banco
conn.close()

print('Dados inserido com sucesso!')


