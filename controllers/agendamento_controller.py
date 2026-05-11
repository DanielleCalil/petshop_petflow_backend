from database import conecta_banco

def select_agendamentos():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    comando = """
        select 
            a.id_agendamento as id, 
            a.data, 
            a.hora, 
            a.status, 
            c.id_cliente as clienteId, 
            c.nome as cliente, 
            p.id_pet as petId, 
            p.nome as pet, 
            s.descricao as servico 
        from Agendamento a
        join Pet p on a.id_pet = p.id_pet
        join Cliente c on p.id_cliente = c.id_cliente
        left join Servico s on a.id_servico = s.id_servico
    """
    cursor.execute(comando)
    resultados = cursor.fetchall()
    
    for r in resultados:
        if r['data']:
            r['data'] = str(r['data'])
        if r['hora']:
            r['hora'] = str(r['hora'])
            
    cursor.close()
    conexao.close()
    return resultados


def insert_agendamento(dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    
    nome_servico = dados.get('servico')
    cursor.execute("select id_servico from Servico where LOWER(descricao) = LOWER(%s)", (nome_servico,))
    res_servico = cursor.fetchone()
    id_servico = res_servico[0] if res_servico else None

    comando = "insert into Agendamento (data, hora, status, id_pet, id_servico) values (%s, %s, %s, %s, %s)"
    valores = (
        dados.get('data'), 
        dados.get('hora'), 
        dados.get('status'), 
        dados.get('petId'), 
        id_servico
    )
    
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def update_agendamento(id, dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    
    nome_servico = dados.get('servico')
    cursor.execute("select id_servico from Servico where LOWER(descricao) = LOWER(%s)", (nome_servico,))
    res_servico = cursor.fetchone()
    id_servico = res_servico[0] if res_servico else None

    comando = "update Agendamento set data=%s, hora=%s, status=%s, id_pet=%s, id_servico=%s where id_agendamento=%s"
    valores = (
        dados.get('data'), 
        dados.get('hora'), 
        dados.get('status'), 
        dados.get('petId'), 
        id_servico, 
        id
    )
    
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def delete_agendamento(id):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    cursor.execute("delete from Agendamento where id_agendamento=%s", (id,))
    conexao.commit()
    cursor.close()
    conexao.close()