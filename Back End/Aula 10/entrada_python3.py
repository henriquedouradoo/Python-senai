import tkinter as tk

janela = tk.Tk()
janela.title('Inserindo textos no Label')
janela.geometry('300x300')

label = tk.Label(janela, text='Coloque uma informação')
label.pack()

def inserir_valor_entry():
    entry.insert(0, ' informação ')

entry = tk.Entry(janela)
entry.pack()

botao = tk.Button(janela, text='Inserir',command=inserir_valor_entry)
botao.pack()

janela.mainloop()