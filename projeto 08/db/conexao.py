import mysql.connector

def conexao_db(db=''):
    try:
        
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port =3306,
            user='root', 
            password='toor projeto ',  
            database=db
        )
        
        #print('Conexao OK')
        return 'Conexao OK', conn
    except mysql.connector.Error as erro:
        print(erro)
       
if __name__ == '__main__':
    print(conexao_db()[0])

# CRUD - CREATE, READ, UPDATE, DELETE  (SQL)