from database import conecta_banco

def select_servicos():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select id_servico as id, descricao as nome, preco, duracao from Servico")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

def insert_servico(dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "insert into Servico (descricao, preco, duracao) values (%s, %s, %s)"
    valores = (dados.get('nome'), dados.get('preco'), dados.get('duracao'))
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def update_servico(id, dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "update Servico set descricao=%s, preco=%s, duracao=%s where id_servico=%s"
    valores = (dados.get('nome'), dados.get('preco'), dados.get('duracao'), id)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def delete_servico(id):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    cursor.execute("delete from Servico where id_servico=%s", (id,))
    conexao.commit()
    cursor.close()
    conexao.close()