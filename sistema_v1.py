from tkinter import*
import random
import time;
import datetime

root = Tk()

root.geometry("1250x650+50+50")
root.title("Projeto Auto Escola")
root.configure(background = "grey")

Tops = Frame (root, width=1350, height=100, bd=9,relief ="raise")
Tops.pack(side=TOP)

Fleft1 = Frame (root, width=900, height=650, bd=8,relief ="raise")
Fleft1.pack(side=LEFT)

Fright1 = Frame (root, width=400, height=650, bd=9,relief ="raise")
Fright1.pack(side=RIGHT)

root.mainloop()
