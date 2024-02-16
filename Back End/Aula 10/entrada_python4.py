import tkinter as tk

janela = tk.Tk()
janela.title('Inserindo textos no Label')
janela.state('zoomed')

label = tk.Label(janela, text='Coloque uma informação')
label.pack()

default_text = 'White'
entry = tk.Entry(janela)
entry.insert(0, default_text)
entry.pack()

janela.mainloop()