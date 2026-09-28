class aluno:
    listaAluno = []
    def __init__(self,nome, cpf, email, matricula, curso):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.matricula = matricula
        self.curso = curso

    def __str__(self):
        return (f'Nome do aluno: {self.nome}.  CPF: {self.cpf}.  Email: {self.email}. '
                f'Matricula: {self.matricula}.  Curso: {self.curso}')

    def adicionar(self):
        self.listaAluno.append(self)

    def mostrar2(self):
        return self.listaAluno
