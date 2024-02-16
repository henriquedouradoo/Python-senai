from tkinter import *

tkWindow = Tk()
tkWindow.geometry('400x250')
tkWindow.title('Trocando as Propriedades dos botões')

def mudarTexto():
    button['text'] = 'Enviado'

button = Button(tkWindow, text='Enviar', command=mudarTexto)
button.pack()

tkWindow.mainloop()

