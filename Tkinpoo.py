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
        "invocamos la raiz con el ET parse y el getroot()"
        self.tree = ET.parse('biblioteca.xml')
        self.raiz = self.tree.getroot()
        "aqui insertamos el primer tag y lo guardamos como referencia para insertar lo demas"
        self.nodo_principal = self.treeview.insert("", END, None, text=self.raiz.tag)
        "esa raiz se la pasamos a la funcion que dibujara el arbol"
        self.insert_treeview(self.raiz, parent=self.nodo_principal)
        "opciones para visualizar mejor el treeview"
        self.treeview.pack(fill = BOTH, expand = True)
        self.pack(fill = BOTH, expand = True)
    
    def insert_treeview(self, raiz, parent=""):
        "recorremos la raiz"
        for child in raiz:
            node_name = child.tag
            item = self.treeview.insert(parent, END, None, text=node_name)
            if len(child) > 0:
                "si tiene hijos volvemos a invocar"
                self.insert_treeview(child, parent=item)
            else:
                """si no tiene hijos solo insertamos pero con el text
                se supone que el ultimo nivel es donde se guardan los valores en el
                campo de texto"""
                if(child.text != None):
                    self.treeview.insert(item, END, None, text=child.text)

root = Tk()
app = Application(root)
app.mainloop()