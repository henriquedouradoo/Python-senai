import tkinter as tk

def pegar_password():
    senha = entry.get()
    retorne.config(text=f'A senha é: {senha}')  

tela = tk.Tk()
tela.title('Capturar senhas digitadas')
tela.geometry('450x300')

entry = tk.Entry(tela, show='*')
entry.pack()

botao = tk.Button(tela, text='Mostrar senha', command=pegar_password)
botao.pack()

retorne = tk.Label(tela, text='')
retorne.pack()

tela.mainloop()
