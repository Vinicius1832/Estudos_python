import tkinter as tk

# Função que soma os valores digitados

def somar ():
    num1 = float(entrada1.get())  # Pega o valor do primeiro campo e converte para numero
    num2 = float(entrada2.get())
    resultado = num1 + num2
    label_resultado.config(text=f'Resultado: {resultado}')

def subtrair():
    num3 = float(entrada3.get())
    num4 = float(entrada4.get())
    resultado_subtracao = num3 - num4
    label_resultado.config(text=f'Resultado: {resultado_subtracao}')

def multiplicacao():
    num5 = float(entrada5.get())
    num6 = float(entrada6.get())
    resultado_multiplicacao = num5 * num6
    label_resultado.config(text=f'Resultado: {resultado_multiplicacao}')

def divisao():
    num7 = float(entrada7.get())
    num8 = float(entrada8.get())
    resultado_divisao = num7/num8
    label_resultado.config(text=f'Resultado:  {resultado_divisao}')

# Lógica de zerar os valores
def zerar_valorees():
    entrada1.delete(0, tk.END)
    entrada2.delete(0,tk.END)
    entrada3.delete(0,tk.END)
    entrada4.delete(0,tk.END)
    entrada5.delete(0,tk.END)
    entrada6.delete(0,tk.END)
    entrada7.delete(0,tk.END)
    entrada8.delete(0,tk.END)
    label_resultado.config(text='Resultado: ')

#-----------------------------------------------------------------

# criação da janela
janela = tk.Tk()
janela.title('Calculadora Simples')
janela.geometry('400x400')
janela.config(bg='lightblue')

#----------------------------------------------------------------

# Linha 1: Soma e Subtração

# Frame = "caixa" para agrupar widgets e controlar o layout
# (quem é filho do Frame usa ele como pai, não a janela)

frame_linha1 = tk.Frame(janela, bg='lightblue')
frame_linha1.pack(side='top',pady=10)

frame_soma = tk.Frame(frame_linha1, bg='lightblue')
frame_soma.pack(side='left',padx=20)

# Campos da soma
entrada1 = tk.Entry(frame_soma, font=('Verdana',14))
entrada1.pack(pady=5)

entrada2 = tk.Entry(frame_soma, font=('Verdana', 14))
entrada2.pack(pady=5)

botao_somar = tk.Button(frame_soma, text='Somar', command=somar )
botao_somar.pack(pady=5)

#-----------------   Campo Subtração    ---------

frame_sub = tk.Frame(frame_linha1, bg='lightblue')
frame_sub.pack(side='left',padx=20)

# Campo 3 subtração
entrada3 = tk.Entry(frame_sub, font=('Verdana',14))
entrada3.pack(pady=5)

# Campo 4 subtração
entrada4 =tk.Entry(frame_sub, font=('Verdana',14))
entrada4.pack(pady=5)

# Botão subtração
botao_subtrair = tk.Button(frame_sub, text='Subtrair', command=subtrair)
botao_subtrair.pack(pady=5)

#-----------------------------------------------------------------------

# Label que mostra o resultado no meio da tela
label_resultado = tk.Label(janela, text='Resultado: ', font=('Arial',14),bg='White')
label_resultado.pack(pady=15)

#-----------------------------------------------------------------------

# ---------- LINHA 2: Multiplicação e Divisão ----------


frame_linha2 = tk.Frame(janela, bg='lightblue')
frame_linha2.pack(side='top', pady=10)

frame_mult = tk.Frame(frame_linha2, bg='lightblue')
frame_mult.pack(side='left', padx=20)

# Campo 5 multipilcação
entrada5 = tk.Entry(frame_mult, font=('Verdana',14))
entrada5.pack(pady=5)

# Campo 6 multiplicação
entrada6 = tk.Entry(frame_mult, font=('Verdana',14))
entrada6.pack(pady=5)

# Botão Multiplicação
botao_multiplicacao = tk.Button(frame_mult, text='multiplicação', command=multiplicacao)
botao_multiplicacao.pack(pady=5)

#-----------------------------------------------------------------------

frame_div = tk.Frame(frame_linha2, bg='lightblue')
frame_div.pack(side='left',padx=20)

# Campo 7 Divisão
entrada7 = tk.Entry(frame_div, font=('Verdana',14))
entrada7.pack(pady=5)

# Campo 8 Divisão
entrada8 = tk.Entry(frame_div, font=('Verdana',14))
entrada8.pack(pady=5)

# Botão Multiplicação
botao_divisao = tk.Button(frame_div, text='Divisão', command=divisao)
botao_divisao.pack(pady=5)

#--------------------------------------------------------------------

# Campo de zerar os valores
botao_valores = tk.Button(janela, text='Limpar', command=zerar_valorees)
botao_valores.pack(pady=10)

janela.mainloop()