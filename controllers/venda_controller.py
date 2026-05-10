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
            c.nome as cliente,
            sum(iv.quantidade) as qtd_itens,
            group_concat(p.nome separator ', ') as lista_produtos
        from Venda v
        join Cliente c on v.id_cliente = c.id_cliente
        left join Itens_Venda iv on v.id_venda = iv.id_venda
        left join Produto p on iv.id_produto = p.id_produto
        group by v.id_venda
    """
    cursor.execute(comando)
    resultados = cursor.fetchall()
    for r in resultados:
        if r['data']: 
            r['data'] = str(r['data'])
        r['qtd_itens'] = int(r['qtd_itens']) if r['qtd_itens'] is not None else 0
    cursor.close()
    conexao.close()
    return resultados

def select_venda_por_id(id_venda):
    conexao = conecta_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("select id_venda as id, id_cliente, valor_total as totalVenda from Venda where id_venda = %s", (id_venda,))
    venda = cursor.fetchone()
    if venda:
        cursor.execute("""
            select p.nome as produto, iv.quantidade, iv.subtotal 
            from Itens_Venda iv 
            join Produto p on iv.id_produto = p.id_produto 
            where iv.id_venda = %s
        """, (id_venda,))
        venda['produtos'] = cursor.fetchall()
    cursor.close()
    conexao.close()
    return venda

def insert_venda(dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    nome_cliente = dados.get('cliente', '').strip()
    cursor.execute("select id_cliente from Cliente where lower(nome) = lower(%s)", (nome_cliente,))
    res_cli = cursor.fetchone()
    id_cli = res_cli[0] if res_cli else None
    data_hoje = datetime.now().strftime('%Y-%m-%d')
    cursor.execute("insert into Venda (data_venda, valor_total, id_cliente) values (%s, 0, %s)", (data_hoje, id_cli))
    id_venda = cursor.lastrowid
    total_geral = 0
    
    for item in dados.get('produtos', []):
        nome_prod = item.get('produto', '').strip()
        cursor.execute("select id_produto, preco from Produto where lower(nome) = lower(%s)", (nome_prod,))
        res_p = cursor.fetchone()
        if res_p:
            id_p, preco_db = res_p
            qtd = int(item.get('quantidade') or 1)
            sub = qtd * float(preco_db)
            total_geral += sub
            cursor.execute("insert into Itens_Venda (id_venda, id_produto, quantidade, preco_unitario, subtotal) values (%s, %s, %s, %s, %s)", (id_venda, id_p, qtd, preco_db, sub))
            cursor.execute("update Produto set estoque = estoque - %s where id_produto = %s", (qtd, id_p))
            
    cursor.execute("update Venda set valor_total = %s where id_venda = %s", (total_geral, id_venda))
    conexao.commit()
    cursor.close()
    conexao.close()

def update_venda(id_venda, dados):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    cursor.execute("select id_produto, quantidade from Itens_Venda where id_venda = %s", (id_venda,))
    itens_antigos = cursor.fetchall()
    
    for id_p, qtd in itens_antigos:
        cursor.execute("update Produto set estoque = estoque + %s where id_produto = %s", (qtd, id_p))
        
    cursor.execute("delete from Itens_Venda where id_venda = %s", (id_venda,))
    nome_cliente = dados.get('cliente', '').strip()
    cursor.execute("select id_cliente from Cliente where lower(nome) = lower(%s)", (nome_cliente,))
    res_cli = cursor.fetchone()
    id_cli = res_cli[0] if res_cli else None
    total_geral = 0
    
    for item in dados.get('produtos', []):
        nome_prod = item.get('produto', '').strip()
        cursor.execute("select id_produto, preco from Produto where lower(nome) = lower(%s)", (nome_prod,))
        res_p = cursor.fetchone()
        if res_p:
            id_p, preco_db = res_p
            qtd = int(item.get('quantidade') or 1)
            sub = qtd * float(preco_db)
            total_geral += sub
            cursor.execute("insert into Itens_Venda (id_venda, id_produto, quantidade, preco_unitario, subtotal) values (%s, %s, %s, %s, %s)", (id_venda, id_p, qtd, preco_db, sub))
            cursor.execute("update Produto set estoque = estoque - %s where id_produto = %s", (qtd, id_p))
            
    cursor.execute("update Venda set valor_total = %s, id_cliente = %s where id_venda = %s", (total_geral, id_cli, id_venda))
    conexao.commit()
    cursor.close()
    conexao.close()

def delete_venda(id_venda):
    conexao = conecta_banco()
    cursor = conexao.cursor()
    cursor.execute("select id_produto, quantidade from Itens_Venda where id_venda = %s", (id_venda,))
    itens = cursor.fetchall()
    
    for id_p, qtd in itens:
        cursor.execute("update Produto set estoque = estoque + %s where id_produto = %s", (qtd, id_p))
        
    cursor.execute("delete from Venda where id_venda = %s", (id_venda,))
    conexao.commit()
    cursor.close()
    conexao.close()