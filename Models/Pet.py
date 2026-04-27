class Pet:
    # APGCMT Estrutura baseada no DER. O campo 'tipo' do frontend equivale a 'especie' no DER.
    def __init__(self, id_pet, nome, especie, id_cliente, raca=None, idade=None, peso=None):
        self._id_pet = id_pet
        self._nome = nome
        self._especie = especie
        self._id_cliente = id_cliente
        self._raca = raca
        self._idade = idade
        self._peso = peso

    def get_id_pet(self): return self._id_pet
    def set_id_pet(self, id_pet): self._id_pet = id_pet
    
    def get_nome(self): return self._nome
    def set_nome(self, nome): self._nome = nome
    
    def get_especie(self): return self._especie
    def set_especie(self, especie): self._especie = especie
    
    def get_id_cliente(self): return self._id_cliente
    def set_id_cliente(self, id_cliente): self._id_cliente = id_cliente