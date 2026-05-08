from database import conecta_banco

def select_pets():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    comando = """
        select 
            p.id_pet as id, 
            p.nome, 
            p.especie as tipo, 
            p.raca, 
            p.peso, 
            p.idade, 
            c.id_cliente as clienteId, 
            c.nome as clienteNome 
        from Pet p
        join Cliente c on p.id_cliente = c.id_cliente
    """
    cursor.execute(comando)
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

def insert_pet(dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "insert into Pet (nome, especie, raca, peso, idade, id_cliente) values (%s, %s, %s, %s, %s, %s)"
    valores = (
        dados.get('nome'), 
        dados.get('tipo'), 
        dados.get('raca'), 
        dados.get('peso'), 
        dados.get('idade'), 
        dados.get('clienteId')
    )
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def update_pet(id, dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "update Pet set nome=%s, especie=%s, raca=%s, peso=%s, idade=%s, id_cliente=%s where id_pet=%s"
    valores = (dados.get('nome'), dados.get('tipo'), dados.get('raca'), dados.get('peso'), dados.get('idade'), dados.get('clienteId'), id)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def delete_pet(id):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    cursor.execute("delete from Pet where id_pet=%s", (id,))
    conexao.commit()
    cursor.close()
    conexao.close()