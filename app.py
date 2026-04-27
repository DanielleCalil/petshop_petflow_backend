from flask import Flask, request, jsonify
from flask_cors import CORS
from Models.Cliente import Cliente
from Models.Pet import Pet
from Controllers.ClienteController import ClienteController
from Controllers.PetController import PetController

app = Flask(__name__)
CORS(app)

controller_cliente = ClienteController()
controller_pet = PetController()

# APGCMT Endpoints para Clientes
@app.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = controller_cliente.listar_clientes()
    return jsonify(clientes)

@app.route('/clientes', methods=['POST'])
def post_cliente():
    dados = request.json
    novo_cliente = Cliente(
        id_cliente=None,
        nome=dados.get('nome'),
        telefone=dados.get('telefone'),
        email=dados.get('email')
    )
    controller_cliente.incluir_cliente(novo_cliente)
    return jsonify({"sucesso": True}), 201

@app.route('/clientes/<int:id_cliente>', methods=['DELETE'])
def delete_cliente(id_cliente):
    controller_cliente.excluir_cliente(id_cliente)
    return jsonify({"sucesso": True}), 200

# APGCMT Endpoints para Pets
@app.route('/pets', methods=['GET'])
def get_pets():
    pets = controller_pet.listar_pets()
    return jsonify(pets)

@app.route('/pets', methods=['POST'])
def post_pet():
    dados = request.json
    novo_pet = Pet(
        id_pet=None,
        nome=dados.get('nome'),
        especie=dados.get('tipo'), # APGCMT Mapeia 'tipo' do frontend para 'especie' do banco
        id_cliente=dados.get('clienteId')
    )
    controller_pet.incluir_pet(novo_pet)
    return jsonify({"sucesso": True}), 201

@app.route('/pets/<int:id_pet>', methods=['DELETE'])
def delete_pet(id_pet):
    controller_pet.excluir_pet(id_pet)
    return jsonify({"sucesso": True}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True) # APGCMT Ex: 5000