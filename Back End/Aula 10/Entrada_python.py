from tkinter import *
from functools import partial

def imprimirDetalhes(usuarioDigitado):
    usuarioTexto = usuarioDigitado.get()
    print('Usuario digitado: ', usuarioTexto)
    return

tkTela = Tk()
tkTela.geometry('400x200')
tkTela.title('Exemplos de entrada de Usuários')

usuarioLabel = Label(tkTela, text='Digite o nome do Usuário')

usuarioDigitado = Entry(tkTela)

imprimirDetalhesMostrado = partial(imprimirDetalhes, usuarioDigitado)

botaoEnviar = Button(tkTela, text='Enviar', command=imprimirDetalhesMostrado)

usuarioLabel.grid(row=0, column=0)
usuarioDigitado.grid(row=0, column=1)
botaoEnviar.grid(row=1, column=1)

tkTela.mainloop()