import mysql.connector
from mysql.connector import Error

# APGCMT Funcao responsavel por estabelecer a conexao com o MySQL do XAMPP
def get_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',          # Geralmente 'localhost'
            user='root',         # Geralmente 'root'
            password='banco',       # Geralmente vazio '' no XAMPP
            database='petshop_bd'      # Nome do banco criado no phpMyAdmin
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar: {e}")
        return None