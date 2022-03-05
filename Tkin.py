import sys
sys.path.append("C:/Users/Juan/Documents/VisualSpy/Biblioteca/Libreria.py")
import Libreria as Lib
from Lib import *
from tkinter import *
from tkinter import ttk

root= Tk()
root.resizable(1,1)
tree=ttk.Treeview(root,columns=("#1","#2"))
tree.pack()
tree.heading("#0",text="ID")
tree.insert("",END,text=Lib.raiz)
root.mainloop()