from conexao import conexao_db


# conexao
conn = conexao_db()[1] #[1] significa a conexao

# pegar o cursor
cursor = conn.cursor()

# define a sua sql(script)
sql = 'show databases'

# executa sua sql
cursor.execute(sql)

dados = cursor.fetchall()

for db in dados:
    print(db)

conn.close()

