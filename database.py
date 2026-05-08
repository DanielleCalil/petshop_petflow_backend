import mysql.connector

def conecta_banco():
    return mysql.connector.connect(
        host='localhost',
        user='db_admin',
        password='admin123',
        database='petshop_bd'
    )