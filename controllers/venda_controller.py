from database import conecta_banco
from datetime import datetime

def select_vendas():
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    comando = """
        select 
            v.id_venda as id, 
            v.data_venda as data, 
            v.valor_total as totalVenda, 
            c.nome as cliente 
        from Venda v
        join Cliente c on v.id_cliente = c.id_cliente
    """
    cursor.execute(comando)
    resultados = cursor.fetchall()
    
    for r in resultados:
        if r['data']:
            r['data'] = str(r['data'])
            
    cursor.close()
    conexao.close()
    return resultados

def insert_venda(dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    
    nome_cliente = dados.get('cliente', '').strip()
    cursor.execute("select id_cliente from Cliente where LOWER(nome) = LOWER(%s)", (nome_cliente,))
    res_cliente = cursor.fetchone()
    id_cliente = res_cliente[0] if res_cliente else None

    data_hoje = datetime.now().strftime('%Y-%m-%d')
    lista_produtos = dados.get('produtos', [])
    valor_total = sum(float(p.get('subtotal') or 0) for p in lista_produtos)
    
    if valor_total == 0:
        valor_total = float(dados.get('totalVenda', 0))

    cursor.execute("insert into Venda (data_venda, valor_total, id_cliente) values (%s, %s, %s)", 
                   (data_hoje, valor_total, id_cliente))
    
    id_venda = cursor.lastrowid

    for item in lista_produtos:
        nome_produto = item.get('produto', '').strip()
        cursor.execute("select id_produto from Produto where LOWER(nome) = LOWER(%s)", (nome_produto,))
        res_prod = cursor.fetchone()
        
        if res_prod:
            id_produto = res_prod[0]
            qtd = int(item.get('quantidade') or 1)
            sub = float(item.get('subtotal') or 0)
            preco_uni = sub / qtd if qtd > 0 else 0

            cursor.execute("""
                insert into Itens_Venda (id_venda, id_produto, quantidade, preco_unitario, subtotal) 
                values (%s, %s, %s, %s, %s)
            """, (id_venda, id_produto, qtd, preco_uni, sub))

    conexao.commit()
    cursor.close()
    conexao.close()

def delete_venda(id_venda):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    comando = "delete from Venda where id_venda=%s"
    valores = (id_venda,)
    cursor.execute(comando, valores)
    conexao.commit()
    cursor.close()
    conexao.close()