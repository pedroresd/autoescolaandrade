from tkinter import*
import random
import time;
import datetime
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

class mainwindow():

    def __init__(self):
    # ================ FRAME
        self.root = Tk()
        self.root.geometry("1250x650+50+50")
        self.root.resizable(False,False)
        self.root.protocol("WM_DELETE_WINDOW")
        self.root.iconbitmap("")
        self.root.title("Projeto Auto Escola")
        self.root.configure(background = 'white')

        self.root.mainloop()
try:
    mainwindow()
except:
    raise Exception("Formulario não pode ser criado")
