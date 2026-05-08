from database import conecta_banco

def get_stats():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    
    cursor.execute("select count(*) as total from Cliente")
    clientes = cursor.fetchone()['total']
    
    cursor.execute("select count(*) as total from Agendamento where status = 'Agendado'")
    agendamentos = cursor.fetchone()['total']
    
    cursor.execute("select coalesce(sum(valor_total), 0) as total from Venda")
    vendas = cursor.fetchone()['total']
    
    cursor.execute("select count(*) as total from Pet")
    pets = cursor.fetchone()['total']
    
    cursor.close()
    conexao.close()
    
    return {
        "clientes": clientes,
        "agendamentos": agendamentos,
        "vendas": float(vendas),
        "pets": pets
    }