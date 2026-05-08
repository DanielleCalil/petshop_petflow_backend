from database import conecta_banco

def select_servicos():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select * from Servico")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

def insert_servico(dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "insert into Servico (descricao, duracao, preco) values (%s, %s, %s)"
    valores = (dados.get('descricao'), dados.get('duracao'), dados.get('preco'))
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def update_servico(id_servico, dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "update Servico set descricao=%s, duracao=%s, preco=%s where id_servico=%s"
    valores = (dados.get('descricao'), dados.get('duracao'), dados.get('preco'), id_servico)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def delete_servico(id_servico):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "delete from Servico where id_servico=%s"
    valores = (id_servico,)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()