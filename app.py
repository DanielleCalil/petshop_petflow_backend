from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers import (
    cliente_controller, pet_controller, agendamento_controller,
    produto_controller, servico_controller, venda_controller, usuario_controller, dashboard_controller
)

app = Flask(__name__)
CORS(app)

@app.route('/api/vendas/<int:id>', methods=['PUT'])
def app_update_venda(id):
    venda_controller.update_venda(id, request.get_json())
    return jsonify({"message": "sucesso"}), 200

@app.route('/api/vendas/<int:id>', methods=['GET'])
def app_get_venda(id):
    return jsonify(venda_controller.select_venda_por_id(id))

@app.route('/api/dashboard', methods=['GET'])
def app_dashboard():
    return jsonify(dashboard_controller.get_stats())

@app.route('/api/usuariosLogar', methods=['POST'])
def app_login_legacy():
    dados = request.get_json()
    usuario = usuario_controller.autenticar_usuario(dados)
    if usuario:
        return jsonify({"sucesso": True, "dados": usuario}), 200
    return jsonify({"sucesso": False, "message": "Erro de login"}), 401

@app.route('/api/clientes', methods=['GET'])
def app_select_clientes():
    return jsonify(cliente_controller.select_clientes())

@app.route('/api/clientes', methods=['POST'])
def app_insert_cliente():
    cliente_controller.insert_cliente(request.get_json())
    return jsonify({"message": "sucesso"}), 201

@app.route('/api/clientes/<int:id>', methods=['PUT'])
def app_update_cliente(id):
    cliente_controller.update_cliente(id, request.get_json())
    return jsonify({"message": "sucesso"}), 200

@app.route('/api/clientes/<int:id>', methods=['DELETE'])
def app_delete_cliente(id):
    cliente_controller.delete_cliente(id)
    return jsonify({"message": "sucesso"}), 200

@app.route('/api/pets', methods=['GET'])
def app_select_pets():
    return jsonify(pet_controller.select_pets())

@app.route('/api/pets', methods=['POST'])
def app_insert_pet():
    pet_controller.insert_pet(request.get_json())
    return jsonify({"message": "sucesso"}), 201

@app.route('/api/pets/<int:id>', methods=['PUT'])
def app_update_pet(id):
    pet_controller.update_pet(id, request.get_json())
    return jsonify({"message": "sucesso"}), 200

@app.route('/api/pets/<int:id>', methods=['DELETE'])
def app_delete_pet(id):
    pet_controller.delete_pet(id)
    return jsonify({"message": "sucesso"}), 200

@app.route('/api/agendamentos', methods=['GET'])
def app_select_agendamentos():
    return jsonify(agendamento_controller.select_agendamentos())

@app.route('/api/agendamentos', methods=['POST'])
def app_insert_agendamento():
    agendamento_controller.insert_agendamento(request.get_json())
    return jsonify({"message": "sucesso"}), 201

@app.route('/api/agendamentos/<int:id>', methods=['PUT'])
def app_update_agendamento(id):
    agendamento_controller.update_agendamento(id, request.get_json())
    return jsonify({"message": "sucesso"}), 200

@app.route('/api/agendamentos/<int:id>', methods=['DELETE'])
def app_delete_agendamento(id):
    agendamento_controller.delete_agendamento(id)
    return jsonify({"message": "sucesso"}), 200

@app.route('/api/produtos', methods=['GET'])
def app_select_produtos():
    return jsonify(produto_controller.select_produtos())

@app.route('/api/produtos', methods=['POST'])
def app_insert_produto():
    produto_controller.insert_produto(request.get_json())
    return jsonify({"message": "sucesso"}), 201

@app.route('/api/produtos/<int:id>', methods=['PUT'])
def app_update_produto(id):
    produto_controller.update_produto(id, request.get_json())
    return jsonify({"message": "sucesso"}), 200

@app.route('/api/produtos/<int:id>', methods=['DELETE'])
def app_delete_produto(id):
    produto_controller.delete_produto(id)
    return jsonify({"message": "sucesso"}), 200

@app.route('/api/servicos', methods=['GET'])
def app_select_servicos():
    return jsonify(servico_controller.select_servicos())

@app.route('/api/servicos', methods=['POST'])
def app_insert_servico():
    servico_controller.insert_servico(request.get_json())
    return jsonify({"message": "sucesso"}), 201

@app.route('/api/servicos/<int:id>', methods=['PUT'])
def app_update_servico(id):
    servico_controller.update_servico(id, request.get_json())
    return jsonify({"message": "sucesso"}), 200

@app.route('/api/servicos/<int:id>', methods=['DELETE'])
def app_delete_servico(id):
    servico_controller.delete_servico(id)
    return jsonify({"message": "sucesso"}), 200

@app.route('/api/vendas', methods=['GET'])
def app_select_vendas():
    return jsonify(venda_controller.select_vendas())

@app.route('/api/vendas', methods=['POST'])
def app_insert_venda():
    venda_controller.insert_venda(request.get_json())
    return jsonify({"message": "sucesso"}), 201

@app.route('/api/vendas/<int:id>', methods=['DELETE'])
def app_delete_venda(id):
    venda_controller.delete_venda(id)
    return jsonify({"message": "sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)