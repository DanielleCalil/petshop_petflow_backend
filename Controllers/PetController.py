from Services.database import get_connection

class PetController:
    # APGCMT Retorna chaves mapeadas para o React (id, nome, tipo, clienteId)
    # Controllers/PetController.py
    def listar_pets(self):
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        
        # APGCMT Mapeando id_pet para id, especie para tipo e id_cliente para clienteId
        sql = "SELECT id_pet AS id, nome, especie AS tipo, id_cliente AS clienteId FROM Pet"
        
        cursor.execute(sql)
        resultados = cursor.fetchall()
        db.close()
        return resultados

    def incluir_pet(self, pet):
        db = get_connection()
        cursor = db.cursor()
        sql = "INSERT INTO Pet (nome, especie, id_cliente) VALUES (%s, %s, %s)"
        valores = (pet.get_nome(), pet.get_especie(), pet.get_id_cliente())
        cursor.execute(sql, valores)
        db.commit()
        db.close()

    def excluir_pet(self, id_pet):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("DELETE FROM Pet WHERE id_pet = %s", (id_pet,))
        db.commit()
        db.close()