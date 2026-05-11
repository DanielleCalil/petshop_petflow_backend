from database import conecta_banco

def autenticar_usuario(dados):
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    comando = "select id_usuario as id, nome, email, perfil from Usuario where email=%s and senha=%s"
    valores = (dados.get('email'), dados.get('senha'))
    cursor.execute(comando, valores)
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado

def select_usuarios():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select id_usuario as id, nome, email, perfil from Usuario")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados