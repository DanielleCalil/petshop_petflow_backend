from database import conecta_banco

def select_pets():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select * from Pet")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

def insert_pet(dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "insert into Pet (nome, especie, raca, peso, idade, id_cliente) values (%s, %s, %s, %s, %s, %s)"
    valores = (dados.get('nome'), dados.get('especie'), dados.get('raca'), dados.get('peso'), dados.get('idade'), dados.get('id_cliente'))
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def update_pet(id_pet, dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "update Pet set nome=%s, especie=%s, raca=%s, peso=%s, idade=%s, id_cliente=%s where id_pet=%s"
    valores = (dados.get('nome'), dados.get('especie'), dados.get('raca'), dados.get('peso'), dados.get('idade'), dados.get('id_cliente'), id_pet)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def delete_pet(id_pet):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "delete from Pet where id_pet=%s"
    valores = (id_pet,)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()