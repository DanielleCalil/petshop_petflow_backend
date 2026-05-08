from database import conecta_banco

def select_clientes():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select * from Cliente")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

def insert_cliente(dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "insert into Cliente (nome, cpf, email, telefone) values (%s, %s, %s, %s)"
    valores = (dados.get('nome'), dados.get('cpf'), dados.get('email'), dados.get('telefone'))
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def update_cliente(id_cliente, dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "update Cliente set nome=%s, cpf=%s, email=%s, telefone=%s where id_cliente=%s"
    valores = (dados.get('nome'), dados.get('cpf'), dados.get('email'), dados.get('telefone'), id_cliente)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def delete_cliente(id_cliente):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "delete from Cliente where id_cliente=%s"
    valores = (id_cliente,)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()