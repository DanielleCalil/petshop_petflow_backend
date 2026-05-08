from database import conecta_banco

def select_agendamentos():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select * from Agendamento")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()
    return resultados

def insert_agendamento(dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "insert into Agendamento (data, hora, status, id_pet, id_servico) values (%s, %s, %s, %s, %s)"
    valores = (dados.get('data'), dados.get('hora'), dados.get('status'), dados.get('id_pet'), dados.get('id_servico'))
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def update_agendamento(id_agendamento, dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "update Agendamento set data=%s, hora=%s, status=%s, id_pet=%s, id_servico=%s where id_agendamento=%s"
    valores = (dados.get('data'), dados.get('hora'), dados.get('status'), dados.get('id_pet'), dados.get('id_servico'), id_agendamento)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def delete_agendamento(id_agendamento):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "delete from Agendamento where id_agendamento=%s"
    valores = (id_agendamento,)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()