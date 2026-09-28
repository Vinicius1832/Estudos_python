from Aluno import aluno
from Funcionario import funcionario
from livraria import livros

cont = ' '

while cont:
    opcao = input(' [1] Adicionar aluno \n[2] Adicionar Funcionario \n[3]Adiconar Livros \n[4]Sair')
    match opcao:

        case '1':

            print('==== Cadastro de aluno ==== ')
            dado1 = input('Informe seu nome: ')
            dado2 = int(input('Informe seu cpf: '))
            dado3 = input('Email: ')
            dado4 = int(input('Matrícula: '))
            dado5 = input('Curso: ')
            a = aluno(dado1,dado2,dado3,dado4,dado5)
            print(a)


