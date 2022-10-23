import mysql.connector

try:
    senha = 'root' #
    conn = mysql.connector.connect(
        host='127.0.0.1',
        port =3306,
        user='root', 
        password='toor',  
        database='db_funcionarios'
    )
    
    print('Conexao OK')
except mysql.connector.Error as erro:
    print(erro)

# CRUD - CREATE, READ, UPDATE, DELETE  (SQL)