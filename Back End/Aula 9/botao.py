from tkinter import *

gui = Tk(className ='Create button!')
gui.geometry('400x400')

botao = Button(gui, text='Botão Incial', width=30, height=4, bg='#000', fg='#fff', activebackground='#0052cc', activeforeground='#000000')
botao.pack()

gui.state('zoomed')

gui.mainloop()

