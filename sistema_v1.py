from tkinter import*
import random
import time;
import datetime
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class loginwindow:
    def __init__(self):

        self.login_window = Toplevel()
        self.login_window.title("Login")
        self.login_window.geometry("342x400+450+150")
        self.login_window.resizable(False, False)
        self.login_window.iconbitmap("")
        self.login_window.configure(background='white')

        Label(self.login_window, text="Faça o Login para entrar ao sistema", font="Arial, 10 bold", foreground='black',background="white").grid(row=0, column=2, sticky=W, pady=10)
        Label(self.login_window, text="Usuário: ", font="Arial, 10 bold", foreground='#FFB900',background="white").grid(row=2, column=1)
        Label(self.login_window, text="Senha: ", font="Arial, 10 bold", foreground='#FFB900',background="white").grid(row=4, column=1)

        self.username = Entry(self.login_window, font="Arial, 10", foreground='black',background="white").grid(row=2, column=2)
        self.password = Entry(self.login_window, font="Arial, 10", foreground='black',background="white", show='*').grid(row=4, column=2)

        self.but = Button(self.login_window, text="Entrar", font="Arial, 15 bold")
        self.but.configure(width=14, height=1, foreground='black', background='#FFB900')
        self.but.grid(row=6, column=2, columnspan=3, sticky='N', pady=30)

        self.login_window.mainloop()


class mainwindow():

    def create_login(self):
        try:
            loginwindow()
        except:
            raise Exception("Não foi possivel abrir este formulario")

    def __init__(self):
    # ================ FRAME
        self.root = Tk()
        self.root.geometry("342x400+450+150")
        self.root.resizable(False,False)
        self.root.protocol("WM_DELETE_WINDOW")
        self.root.iconbitmap("")
        self.root.title("Projeto Auto Escola")
        self.root.configure(background = 'white')

        Label(self.root,text="Sistema de Gestão Auto Escola", font="Arial, 10 bold", foreground='#FFB900', background="white").grid(row=1, column=0, sticky=W+E)
        Label(self.root, text="Cadastro de Clientes", font="Arial, 20", foreground='black', background="white").grid(row=2, column=0, sticky=W + E)
        Label(self.root, text="Desenvolvido por Pedro Resende - pedroresd1@gmail.com", font="Arial, 10", foreground='black', background="white").grid(row=3, column=0, sticky=W + E)
        Label(self.root, text="Faça o Login para Iniciar o sistema", font="Arial, 10 bold", foreground='black', background="white").grid(row=4, column=0, sticky=W + E, pady=5)

        self.but = Button(self.root, text="Login", font="Arial, 15 bold", command = self.create_login)
        self.but.configure(width=14, height=1, foreground='black', background='#FFB900')
        self.but.grid(row=5, column=0, columnspan=1, sticky='N', pady=30)

        self.menu_bar = Menu(self.root)
        self.menu_bar.add_separator()

        self.file_menu = Menu(self.menu_bar, tearoff = 0)
        self.file_menu.add_command(label="Entrar")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Esqueci a Senha")
        self.menu_bar.add_cascade(label="Sair")

        self.menu_bar.add_separator()

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Ajuda")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Sobre")
        self.menu_bar.add_cascade(label="Contato")

        self.root.configure(menu=self.menu_bar)
        self.root.mainloop()

        self.root.mainloop()
try:
    mainwindow()
except:
    raise Exception("Formulario não pode ser criado")
