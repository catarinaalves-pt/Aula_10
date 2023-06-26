from tkinter import *
def faren(): #celsius para faren




top = Toplevel()
top.title("Função de Conversão")
top.geometry("150x150")
top.resizable(True,True)
Label(top, text='Insira um número').grid(row=0)
num = Entry(top)
num.grid(row=0, column = 1)