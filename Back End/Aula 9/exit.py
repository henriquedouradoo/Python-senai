import tkinter as tk
from tkinter import font

#criando a janela

window = tk.Tk()
window.geometry('500x300')
window.title('Treinando com Tkinter')
window['bg'] = 'Grey'


label = tk.Label(window, text='Pressionando a tecla ESC(ape) para fechar uma janela')

label.pack()

window.bind('<Escape>', lambda e, w=window: w.destroy())

def botao_clique():
    window.destroy()

botao = tk.Button(window, text='Exit Page', command=botao_clique)
botao.pack()

window.state('zoomed')
window.mainloop()