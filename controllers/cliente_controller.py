from database import conecta_banco

def select_clientes():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select id_cliente as id, nome, cpf, email, telefone from Cliente")
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

def update_cliente(id, dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "update Cliente set nome=%s, email=%s, telefone=%s where id_cliente=%s"
    valores = (dados.get('nome'), dados.get('email'), dados.get('telefone'), id)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def delete_cliente(id):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    cursor.execute("delete from Cliente where id_cliente=%s", (id,))
    conexao.commit()
    cursor.close()
    conexao.close()