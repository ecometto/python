# PROGRAMA PARA CONTAR NUMEROS PARES E IMPARES 

from tkinter import *
from tkinter.ttk import *
import time

############ FUNCIONES ################333
def imprimir_mensaje():
    etiqueta.config(text="Welcome to: "+ cuadro_texto.get())
    cuadro_texto.delete(0,END)
    cuadro_texto.focus

def funcion_combo(seleccion):
    cuadro_texto.insert(0, "ud selecciono: "+ str(Vcombo))
    



################## VARIABLES ################
vcuadro = StringVar()
vcombo = StringVar()

diccionario = {1:"Pyton", 2:"Java", 3: "otros"}


miRaiz = Tk()

miRaiz.title("hola a todos")
miRaiz.geometry("550x500")
#miRaiz.maxsize(550, 500) #tama;o maximo que puede tomar

combo = Combobox(miRaiz)
combo.grid(row=1, column=0, ipadx=10, ipady=10, textvariable = vcombo)
combo["values"]= list(diccionario.keys())
combo.current(0)
combo.bind("<<ComboboxSelected>>", funcion_combo)


etiqueta = Label(miRaiz, text="Welcome to the Jungle ", font=("Arial", 20))
etiqueta.grid(row=0, column=0)

cuadro_texto = Entry(textvariable = vcuadro)
cuadro_texto.grid(row=0, column=1)


boton = Button(miRaiz, text="press here", command = imprimir_mensaje)
boton.grid(row=0, column=2)


#bad option "-width": must be -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
#para borrar: Delete(0, END)

vcuadro = cuadro_texto.get()
vcombo = combo.get()



miRaiz.mainloop()


def contarPeI():
    numero = input("ingrese un numero")
    contar_pares = 0
    contar_impares = 0

    for i in numero:
        if int(i) % 2==0:
            contar_pares +=1
        else:
            contar_impares +=1

    print("pares: {}, impares: {}".format(contar_pares, contar_impares))



