from Services.database import get_connection

class ClienteController:
    # APGCMT Retorna chaves mapeadas para o que o React espera (id, nome, telefone, email)
    # Controllers/ClienteController.py
    def listar_clientes(self):
        db = get_connection()
        # APGCMT O dictionary=True e essencial para o React ler as chaves
        cursor = db.cursor(dictionary=True)
        
        # APGCMT Usamos o 'AS' para renomear as colunas do banco para o nome que o React espera
        sql = "SELECT id_cliente AS id, nome, telefone, email FROM Cliente"
        
        cursor.execute(sql)
        resultados = cursor.fetchall()
        db.close()
        return resultados

    def incluir_cliente(self, cliente):
        db = get_connection()
        cursor = db.cursor()
        sql = "INSERT INTO Cliente (nome, telefone, email, cpf) VALUES (%s, %s, %s, %s)"
        valores = (cliente.get_nome(), cliente.get_telefone(), cliente.get_email(), cliente.get_cpf())
        cursor.execute(sql, valores)
        db.commit()
        db.close()

    def excluir_cliente(self, id_cliente):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM Cliente WHERE id_cliente = %s", (id_cliente,))
        db.commit()
        db.close()