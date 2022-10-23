from conexao import conexao_db

# pegar informacoes
id_aluno = int(input('Id do aluno: '))

nome = input('Nome: ')
media = float(input('Media: '))

situacao = 'Aprovado' if media > 6.9 else 'Reprovado'

# conectar ao banco de dados
conn = conexao_db('kasolution')[1]

# pegar o cursor
cur = conn.cursor()

# query SQL
sql = 'UPDATE alunos SET nome=%s, media=%s, situacao=%s WHERE id=%s'

# executar o sql
cur.execute(sql,[nome, media, situacao, id_aluno])

# comitar para inserir
conn.commit()

print(f'Foram alterados {cur.rowcount} registro(s).')

#fechar conexao com banco
conn.close()