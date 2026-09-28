import tkinter as tk

# Ao aperta no botão muda o olá mundo que estava para a frase abaixo
def dizer_ola():
    texto.config(text="Você clicou no botão")


def verificar():
    if opcao.get() == 1:
        label_status.config(text="Você aceitou os termos!")
    else:
        label_status.config(text="Você NÃO aceitou os termos.")



# Cria a janela principal da aplicação
janela = tk.Tk()

# Titulo da janela
janela.title("Minha primeira janela")

# Tamanho da janela: altura-> 400 x largura-> 300 + esquerda-> 50 + direita-> 50
janela.geometry("400x300+50+50")

# Cor de Fundo
janela.config(bg="lightgreen")

# Adicionando texto com Label
texto = tk.Label(
    janela,
    text="Olá Mundo!",
    font=("Arial", 16),       # fonte e tamanho
    fg= "lightblue",          # Cor do texto (fg = foreground)
    bg="purple"               # Cor de fundo do próprio Label
)

# Faz com que mostra o texto acima na janela
texto.pack()

# Espaço para o usuário digitar
entrada = tk.Entry(janela)
entrada.pack()

# Retorna com uma mensagem para o usuário
valor = entrada.get()

# Se fosse para entrar numero, teria q utilizar float ou int
# numero = float(entrada.get())


botao = tk.Button(janela, text="Primeiro botão", command=dizer_ola)
botao.pack()


#botao.pack(side='bottom')  # de cima para baixo
#botao.pack(side='right')   # da direita para a esqueda
botao.pack(side='top')     # de cima para baixo (é o padrão)
#botao.pack(side='left')    # da esquerda para direita

botao.pack(pady=25)   # espaço vertical (acima/abaixo) de 10 pixels
botao.pack(padx=250)   # espaço horizontal (esquerda/direita) de 20 pixels


# FRAME = uma "caixa" invisível usada para AGRUPAR outros widgets dentro da janela.
# Serve para organizar o layout em blocos (ex: colocar coisas lado a lado
# sem bagunçar o resto da tela).
#
# Como usar:
# 1) Cria o Frame, dizendo quem é o "pai" dele (a janela ou outro Frame):
#       frame_x = tk.Frame(janela, bg='lightblue')
#       frame_x.pack(side='left', padx=20)   # posiciona o Frame na tela
#
# 2) Todo widget que deve ficar DENTRO desse Frame usa ele como pai
#    (primeiro parâmetro), em vez da janela:
#       entrada = tk.Entry(frame_x, ...)
#       botao = tk.Button(frame_x, ...)
#
# Dá pra ter Frame dentro de Frame, permitindo montar layouts em
# "linhas e colunas" (ex: side='top' para empilhar linhas,
# side='left' dentro de cada linha para colocar blocos lado a lado).


opcao = tk.IntVar()   # variável que vai guardar 0 ou 1


# Criando o botão de marcar e para desmarcar
check1 = tk.Checkbutton(janela, text="Aceito os termos", variable=opcao)
check1.pack(pady=10)

botao = tk.Button(janela, text="Verificar", command=verificar)
botao.pack(pady=5)

label_status = tk.Label(janela, text="")
label_status.pack(pady=5)



# Mantém a janela aberta, esperando ações do usuário
janela.mainloop()

