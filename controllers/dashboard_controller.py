from database import conecta_banco
from datetime import datetime

def get_stats():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    
    data_hoje = datetime.now().strftime('%Y-%m-%d')
    
    cursor.execute("select count(*) as total from Cliente")
    total_clientes = cursor.fetchone()['total']
    
    cursor.execute("select count(*) as total from Pet")
    total_pets = cursor.fetchone()['total']
    
    cursor.execute("select count(*) as total from Agendamento where data = %s", (data_hoje,))
    agendamentos_hoje = cursor.fetchone()['total']
    
    cursor.execute("select count(*) as total from Venda")
    total_vendas = cursor.fetchone()['total']
    
    cursor.execute("select coalesce(sum(valor_total), 0) as total from Venda where data_venda = %s", (data_hoje,))
    faturamento_dia = cursor.fetchone()['total']
    
    cursor.close()
    conexao.close()
    
    return {
        "totalClientes": total_clientes,
        "totalPets": total_pets,
        "agendamentosHoje": agendamentos_hoje,
        "totalVendas": total_vendas,
        "faturamentoDia": float(faturamento_dia)
    }