import tkinter as tk

# para contar quantas vezes o botao foi clicado
contador = 0


def contador_cliques():
    global contador               # para a variavel serve usada em outros lugares além daqui
    contador = contador + 1       # toda vez que clicar no botão vai somar mais 1
    texto.config(text=f"Cliques: {contador}")    # chamando a variavel contador para somar

def zerar_cliques():
    global contador
    contador = 0            # toda vez que clicar em zerar, contador volta a ter o valor 0
    texto.config(text=f"Zerar: {contador}")

def diminuir_cliques():
    global contador
    contador = contador -1  # quando for clicado no botao diminuir, vai diminuir sempre -1 do valor que tiver em contador
    texto.config(text=f'Diminuir: {contador}')


# Configurações da janela, cor, tamanho, fonte
janela = tk.Tk()
janela.title('Contagem de Cliques')
janela.geometry("300x200")
janela.config(bg='lightblue')

texto = tk.Label(janela,text='Cliques: 0',font=('Arial',16), bg='lightgreen')
texto.pack()



# Criando e configurando os botaões
botao = tk.Button(janela, text='Clique aqui', command=contador_cliques)
botao.pack(side='left', padx=2)

botao1 = tk.Button(janela, text='Zerar', command=zerar_cliques)
botao1.pack(side='left', padx=2)

botao2 = tk.Button(janela, text='Diminuir clique', command=diminuir_cliques)
botao2.pack(side='left', padx=2)


# Janela fica aberta infinitamente
janela.mainloop()