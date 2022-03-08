import sys
sys.path.append("C:/Users/Juan/Documents/VisualSpy/Biblioteca/Libreria.py")
import Libreria as Lib
from Lib import *
from tkinter import *
from tkinter import ttk
main_window = Tk()
main_window.title("Vista de árbol en Tkinter")
treeview = ttk.Treeview()
item = treeview.insert("", END, text="Elemento 1")
treeview.insert(item, END, text="Subelemento 1")
treeview.pack()
main_window.mainloop()