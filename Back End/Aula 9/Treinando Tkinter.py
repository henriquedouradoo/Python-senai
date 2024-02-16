import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk

#criando a janela

window = tk.Tk()
window.geometry('500x300')
window.title('Treinando com Tkinter')
window['bg'] = 'Grey'

window['padx'] = 100

window['pady'] = 50

label_font = font.Font(size=30)
label = tk.Label(window, wraplength=300, font=label_font, text=' enquanto eu faço deload eu furo os olhos do meu parceiro! 🤤 ')

tkimage = ImageTk.PhotoImage(Image.open('fb.jpg'))
tk.Label(window, image=tkimage).pack()

def janela_redimensao(event):
    largura = event.width
    altura = event.height
    print(f'A janela foi redimensionada em {largura}x{altura}')

window.bind('<Configure>', janela_redimensao)
label.pack()

window.mainloop()