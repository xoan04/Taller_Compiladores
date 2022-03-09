from inspect import Attribute
from tkinter import *
from tkinter import ttk, messagebox
import xml.etree.ElementTree as ET

class  Application(ttk.Frame):

    def __init__(self, main_window):
        
        super().__init__(main_window)
        main_window.title("XML viewer")
        main_window.geometry("500x500")
        self.treeview = ttk.Treeview(self)
        self.tree = ET.parse('biblioteca.xml')
        self.raiz = self.tree.getroot()

        "Raiz o Primer Tag"
        self.nodo_principal = self.treeview.insert("", END, None, text=self.raiz.tag)
        "La mandamos a que se dibuje en el arbol"
        self.insert_treeview(self.raiz, padre=self.nodo_principal)
        self.treeview.pack(fill = BOTH, expand = True)
        self.pack(fill = BOTH, expand = True)
    
    def insert_treeview(self, raiz, padre=""):
        "Recorrido"
        for hijo in raiz:
            node_name = hijo.tag
            item = self.treeview.insert(padre, END, None, text=node_name)
            if len(hijo) > 0:
                "Si encuentra hijos insertamos el padre"
                self.insert_treeview(hijo, padre=item)
            else:
                """Sino seria ultimo nivel e insertamos valores de texto"""
                if(hijo.text != None):
                    self.treeview.insert(item, END, None, text=hijo.text)

root = Tk()
app = Application(root)
app.mainloop()