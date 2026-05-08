from database import conecta_banco

def select_produtos():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select * from Produto")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

def insert_produto(dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "insert into Produto (nome, categoria, preco, estoque) values (%s, %s, %s, %s)"
    valores = (dados.get('nome'), dados.get('categoria'), dados.get('preco'), dados.get('estoque'))
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def update_produto(idProduto, dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "update Produto set nome=%s, categoria=%s, preco=%s, estoque=%s where id_produto=%s"
    valores = (dados.get('nome'), dados.get('categoria'), dados.get('preco'), dados.get('estoque'), idProduto)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def delete_produto(id_produto):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "delete from Produto where id_produto=%s"
    valores = (id_produto,)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()