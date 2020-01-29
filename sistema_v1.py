from tkinter import*
import random
import time;
import datetime
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class mainwindow():

    def create_signin(self):
        try:
            signinwindow()
        except:
            raise Exception("Não foi possivel abrir este formulario")

    def create_login(self):
        try:
            loginwindow()
        except:
            raise Exception("Não foi possivel abrir este formulario")

    def quit_window(self):
        if messagebox.askokcancel("Sair","Deseja realmente sair?"):
            self.root.destroy()

    def __init__(self):
    # ================ FRAME
        self.root = Tk()
        self.root.geometry("342x260+450+150")
        self.root.resizable(False,False)
        self.root.protocol("WM_DELETE_WINDOW",self.quit_window)
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
        self.file_menu.add_command(label="Cadastro", command = self.create_signin)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Esqueci a Senha")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Sair", command = self.quit_window)
        self.menu_bar.add_cascade(label="Cadastrar", menu = self.file_menu)

        self.menu_bar.add_separator()

        self.help_menu = Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Contato")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Ajuda")
        self.menu_bar.add_cascade(label="Sobre", menu = self.help_menu)

        self.root.configure(menu=self.menu_bar)
        self.root.mainloop()

        self.root.mainloop()


class loginwindow:
    def __init__(self):

        self.login_window = Toplevel()
        self.login_window.title("Login")
        self.login_window.geometry("342x260+450+150")
        self.login_window.resizable(False, False)
        self.login_window.iconbitmap("")
        self.login_window.configure(background='white')

        Label(self.login_window, text="Faça o Login para entrar ao sistema", font="Arial, 10 bold", foreground='black',background="white").grid(row=0, column=2, sticky=W, pady=10)
        Label(self.login_window, text="Usuário: ", font="Arial, 10 bold", foreground='#FFB900',background="white").grid(row=2, column=1)
        Label(self.login_window, text="Senha: ", font="Arial, 10 bold", foreground='#FFB900',background="white").grid(row=4, column=1)

        self.username = Entry(self.login_window, font="Arial, 15", foreground='black',background="white").grid(row=2, column=2)
        self.password = Entry(self.login_window, font="Arial, 15", foreground='black',background="white", show='*').grid(row=4, column=2)

        self.but = Button(self.login_window, text="Entrar", font="Arial, 15 bold")
        self.but.configure(width=14, height=1, foreground='black', background='#FFB900')
        self.but.grid(row=6, column=2, columnspan=3, sticky='N', pady=30)

        self.but = Button(self.login_window, text="", font="Arial, 7 bold")
        self.but.configure(width=1, height=1, foreground='black', background='#FFB900')
        self.but.grid(row=4, column=3, columnspan=1, sticky='N', pady=10)

        self.login_window.mainloop()

class signinwindow:
    def __init__(self):

        self.signin_window = Toplevel()
        self.signin_window.title("Cadastro")
        self.signin_window.geometry("342x260+450+150")
        self.signin_window.resizable(False, False)
        self.signin_window.iconbitmap("")
        self.signin_window.configure(background='white')

        Label(self.signin_window, text="Faça o seu cadastro!", font="Arial, 13 bold", foreground='black',background="white").grid(row=0, column=3, sticky=W, pady=10)
        Label(self.signin_window, text="Usuário: ", font="Arial, 12 bold", foreground='#FFB900',background="white").grid(row=2, column=2)
        Label(self.signin_window, text="Senha: ", font="Arial, 12 bold", foreground='#FFB900',background="white").grid(row=4, column=2)
        Label(self.signin_window, text="Email: ", font="Arial, 12 bold", foreground='#FFB900', background="white").grid(row=6, column=2)

        self.username = Entry(self.signin_window, font="Arial, 15", foreground='black',background="white").grid(row=2, column=3)
        self.password = Entry(self.signin_window, font="Arial, 15", foreground='black',background="white").grid(row=4, column=3)
        self.email = Entry(self.signin_window, font="Arial, 15", foreground='black',background="white").grid(row=6, column=3)

        self.user_add = Button(self.signin_window, text="Cadastrar", font="Arial, 15 bold")
        self.user_add.configure(width=14, height=1, foreground='black', background='#FFB900')
        self.user_add.grid(row=8, column=3, columnspan=1, sticky='N', pady=30)

        self.but_singin = Button(self.signin_window, text="", font="Arial, 7 bold")
        self.but_singin.configure(width=1, height=1, foreground='black', background='#FFB900')
        self.but_singin.grid(row=4, column=4, columnspan=1, sticky='N', pady=10)

        self.signin_window.mainloop()
try:
    mainwindow()
except:
    raise Exception("Formulario não pode ser criado")

