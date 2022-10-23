from conexao import conexao_db

# pegar informacoes
id_aluno = int(input('Id do aluno: '))

# conectar ao banco de dados
conn = conexao_db('kasolution')[1]

# pegar o cursor
cur = conn.cursor()

if id_aluno == 0:
    # query sql
    sql = 'SELECT id, foto, nome, turma, media, situacao, ativo FROM alunos'

    # executar sql
    cur.execute(sql)
    
    
    # 01 forma de imprimir os resultados
    #for registro in cur:
    #    print(registro[2]) # égar o nome
        
    # 02 forma de imprimir os resultados
    for (id, foto, nome, turma, media, situacao, ativo) in cur:
        print(nome)
        
else:
    # query sql
    sql = 'SELECT id, foto, nome, turma, media, situacao, ativo FROM alunos WHERE id=%s'

    # executar sql
    cur.execute(sql, [id_aluno])
    
    registro = cur.fetchone()
    
    if cur.rowcount <= 0:
        print('Nenhum aluno encontrado no banco de dados!')
    else:
        print(f'Nome do aluno: {registro[2]}')
        
conn.close()