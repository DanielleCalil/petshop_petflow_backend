class Cliente:
    # APGCMT Estrutura baseada no DER. CPF omitido na interface atual, definido como opcional.
    def __init__(self, id_cliente, nome, telefone, email, cpf=None):
        self._id_cliente = id_cliente
        self._nome = nome
        self._telefone = telefone
        self._email = email
        self._cpf = cpf

    def get_id_cliente(self): return self._id_cliente
    def set_id_cliente(self, id_cliente): self._id_cliente = id_cliente

    def get_nome(self): return self._nome
    def set_nome(self, nome): self._nome = nome

    def get_telefone(self): return self._telefone
    def set_telefone(self, telefone): self._telefone = telefone

    def get_email(self): return self._email
    def set_email(self, email): self._email = email

    def get_cpf(self): return self._cpf
    def set_cpf(self, cpf): self._cpf = cpf