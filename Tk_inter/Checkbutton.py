import tkinter as tk

from Calculadora import label_resultado


def verificacao():
    if opcao.get() ==1:
        label_resultado.config(text='Você gosta do python')
    else:
        label_resultado.config(text=' Se não clicar você não gosta do python')

def verficacao2():
    if opcao2.get() == 1:
        label_resultado.config(text='Gosto de café')
    else:
        label_resultado.config(text='Você não gosta de café')


janela = tk.Tk()
janela.title('Aprendendo sobre Checkbutton')
janela.geometry('300x150')

opcao = tk.IntVar()

verificar = tk.Checkbutton(janela, text='SEI LA', variable=opcao)
verificar.pack()

botao1 = tk.Button(janela, text='Verificar', command=verficacao2)
botao1.pack()

opcao2 = tk.IntVar()

verificar2 = tk.Checkbutton(janela, text='SLA', variable= opcao2)
verificar2.pack()

botao2 = tk.Button(janela, text='Verificar', command=verificacao)
botao2.pack()

label_resultado = tk.Label(janela, text='')
label_resultado.pack(pady=10)





janela.mainloop()
