from conexao import conexao_db

# pegar informacoes
id_aluno = int(input('Id do aluno: '))

# conectar ao banco de dados
conn = conexao_db('kasolution')[1]

# pegar o cursor
cur = conn.cursor()

#query sql
sql = 'DELETE FROM alunos WHERE id=%s'

#executar o sql
cur.execute(sql, [id_aluno])

# comitar para deletar
conn.commit()

if cur.rowcount <= 0:
    print('Nenhum aluno encontrado no banco de dados!')
else:
    print(f'Deletado com sucesso!')
    
# fechar conexao com banco

conn.close()