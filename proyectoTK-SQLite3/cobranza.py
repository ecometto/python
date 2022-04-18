import pickle
from tkinter import *


########## definiendo variables ##############3
class Deportistas():
    def __init__(self, num_socio, apellido_y_nombre, dni):
        self.num_socio = num_socio
        self.apellido_y_nombre = apellido_y_nombre
        self.dni = dni




def abrir_archivo(archivo):
    m = open(archivo, "rb")
    v = pickle.load(m)
    m.close()
    return v

def guardar_archivo(archivo, v):
    m = open(archivo, "wb")
    pickle.dump(v,m)
    m.close()

def guardar_deportista(archivo, v, num1, ape1, dni1):
        deportista = Deportistas(num1, ape1, dni1)
        v.append(deportista)
        guardar_archivo(archivo, v)
        mostrar_deportistas(v)
        num.set("")
        ape.set("")
        dni.set("")

        return v


def mostrar_deportistas(v):
    lista.delete(0,END)
    sep = "--------------------"
    for fila in v:
        filax  = (fila.num_socio+"\t\t"+fila.apellido_y_nombre+"\t\t"+fila.dni)
        lista.insert(INSERT, filax)


# def validar_num(num, v):
#         while fila.num_socio == num1:
#             print("Error. Registro duplicado")
#             num = int(input("Ingrese el numero de socio: "))
#
#     return num





############## construyendo la interface grafica ###############33333
ventana = Tk()
cabecera = Label(ventana, text="", width=100, bg="blue").pack()

frame = Frame(ventana)
frame.pack(padx=10, pady=10)

num = IntVar()
e_num = Label(frame, text="Numero de Socio").grid(row=0, column =0, padx=10, pady=10)
NUM = Entry(frame, textvariable=num).grid(row=0, column =1)

ape = StringVar()
e_nombre = Label(frame, text="Apellido y Nombre").grid(row=1, column =0, padx=10, pady=10)
APE = Entry(frame, textvariable=ape).grid(row=1, column =1)

dni = IntVar()
e_DNI = Label(frame, text="DNI Numero:").grid(row=2, column =0, padx=10, pady=10)
DNI = Entry(frame, textvariable=dni).grid(row=2, column =1)

boton = Button(frame, text="Guardar", command=lambda: guardar_deportista(archivo, v, num.get(), ape.get(), dni.get())).grid(row=3, column =0, columnspan = 2, padx=10, pady=10)

frame1 = Frame(ventana)
frame1.pack()
label = Label(frame1, width=100).pack()
lista=Listbox(frame1, width=80)
lista.pack()



 ########################################################################
archivo = "BBDD.dat"
v = abrir_archivo(archivo)

for fila in v:
    filax = (str(fila.num_socio)+"-------"+str(fila.apellido_y_nombre)+"-------S"+str(fila.dni))
    lista.insert(END, filax)

guardar_archivo(archivo, v)


mainloop()
