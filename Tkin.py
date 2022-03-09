from tkinter import *
from tkinter import ttk, messagebox
import xml.etree.ElementTree as ET



main_window = Tk()
main_window.title("Vista de árbol en Tkinter")
main_window.geometry("400x400")

tree = ET.parse("biblioteca.xml")
root = tree.getroot()
treeview = ttk.Treeview()
token_root_iid = 210
token_libro_iid = 1
libros = []

treeview.insert("", END, text="biblioteca", iid=token_root_iid)
"primer nivel"
for item in root.findall("./"): 
    libros.append(item.attrib)

for item in libros:
    treeview.insert(token_root_iid, END, text="libros", iid=token_libro_iid)
    token_libro_iid += 1

"segundo nivel"
token_libros_atrib_iid = 1
dic_genero = {}
dic_publicacion = {}
dic_autor = {}
for item in root.findall("./Libro/"):
    match item.tag:
        case "Genero":
            dic_genero[item.tag] = item.text
        case "Publicacion":
            dic_publicacion[item.tag] = item.text
        case "Autor":
            dic_autor[item.tag] = item.text
        case _:
            print("error?")

cantidad_libros = len(libros)
for item in range(cantidad_libros):
    treeview.insert((item + 1), END, text="genero", iid=None)
    treeview.insert((item + 1), END, text="publicacion", iid=None)
    treeview.insert((item + 1), END, text="autor", iid=None)



treeview.pack(fill = BOTH, expand = True)
main_window.mainloop()