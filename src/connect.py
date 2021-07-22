from getpass import getpass
from mysql.connector import connect, Error

# Conectar a base de dados existente MySQL
try:
    with connect(
        host="localhost",
        user=input("Digite o username: "),
        password=getpass("Digite o  password: "),
        # Base de dados
        database="TUTORIAL_MYSQL",
    ) as connection:
        print(connection)
except Error as e:
    print(e)

# O código acima retonar a conexão em forma de objeto:
# <mysql.connector.connection_cext.CMySQLConnection object at 0x7effdac85220>
