class funcionario:
    listaFuncionario = []
    def __init__(self, nome, idade, cpf, codigo_Funcionario):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.codigo_Funcionario = codigo_Funcionario

    def __str__(self):
        return f'Nome: {self.nome}  Idade: {self.idade}  CPF: {self.cpf}  Código: {self.codigo_Funcionario}'

    def adicionar3(self):
        self.listaFuncionario.append(self)

    def mostra3(self):
        return self.listaFuncionario