import Cliente

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf , endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

pf = PessoaFisica("Ronaldo","20-09","1","RUA X")


print(pf.cpf)