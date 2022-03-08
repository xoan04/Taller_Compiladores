import xml.etree.ElementTree as ET
from Lib import *
from tkinter import *
from tkinter import ttk
xml = 'biblioteca.xml'
xmlParse=ET.parse(xml)
raiz = xmlParse.getroot()
ET.dump(xmlParse)

class VentanaPrincipal(ttk.Frame):
    def __init__(self,main_window):
        super().__init__(main_window)
        main_window.title("Biblioteca")
        main_window.geometry("500x500")
        self.treeview=ttk.Treeview(self)
    for child in raiz:
        print(child.tag, child.text)
        
for Libro in raiz.findall('Libro'):
 genero = Libro.find('Genero').text
 titulo= Libro.get('Titulo')
 print("\n")
 print(titulo,"\n",genero)
        
        





















root=Tk()
ventana=VentanaPrincipal(root)
ventana.mainloop()
