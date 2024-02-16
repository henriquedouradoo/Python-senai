import tkinter as tk
from tkinter import font

#criando a janela

window = tk.Tk()
window.geometry('500x300')
window.title('Treinando com Tkinter')
window['bg'] = 'Grey'

def atualizar_janela():
    window.update()
    window.update_idletasks()
    print(f'Acompanhando o Deload da janela')

label = tk.Label(window, text='Clicar no botão de atualizar')

label.pack()

botao = tk.Button(window, text='Atualizar', command=atualizar_janela)

botao.pack()

window.mainloop()