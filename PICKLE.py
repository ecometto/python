# class Persona():
#     def __init__(self, nombre, apellido, edad, mail):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.mail = mail


# class Acciones():
#     listaPersonas = []

#     def agregar(self, persona):
#         self.listaPersonas.append(persona)

#     def mostrarLista(self):
#         for p in self.listaPersonas:
#             print(p.nombre)

# p1 = Persona('Edgardo', 'Cometto', 44, 'ecom@ecom')

# # genero nuevo objeto
# accion = Acciones()

# accion.agregar(p1)

# print(accion.mostrarLista())


from hashlib import new
import pickle

# # # generando archivo y volcándole datos
# enMemoria = open('aaa', 'wb')
# data = []
# dato = ['Edgardo', 'cometto']
# data.append(dato)
# pickle.dump(data, enMemoria)
# enMemoria.close()

# # leyendo archivo a+
# def AbrirParaLeeryModificar():
#     file = open('aaa', 'ab+')
#     file.seek(0)
#     data = pickle.load(file)
#     file.close()
#     return data


# data = AbrirParaLeeryModificar()
# dato2 = ['nombre2', 'apellido2']
# data.append(dato2)


# file = open('aaa', 'wb')
# pickle.dump(data, file)
# file.close()

# data = AbrirParaLeeryModificar()
# for dato in data:
#     print(dato)

def registrar():
    continuar = True
    while continuar:
        nombre= input("ingrese un nombre: ")
        apellido=input("ingrese un apellido: ")
        guardar=input(f"Desea guardar los cambios? \nNombre: {nombre} - Apellido: {apellido} \n 1=SI / 0=NO ")
        if guardar == "1":
            newRecord=[nombre, apellido]
            datos.append(newRecord)
        print(datos)
        res=input("Desea continuar ingresando (1=SI / 0=NO)")
        if res == "0":
            continuar = False
            
            

file = open("pickle", "rb+")
datos = pickle.load(file) #descarga el contenido del archivo en un objeto (lista o diccionario s/ se haya cargado)
print(datos)
file.close()

registrar()

with open("pickle", "wb") as f:
    pickle.dump(datos, f) #carga el contenido del objeto en el archivo (suobreecribe)

with open("pickle", "rb") as file:
    leer = pickle.load(file) #vuelve a descargar el contenido del objeto para leerlo (modo Read)
    item=1
    for cada in leer:
        print(f"{item} - Nombre: {cada[0]}, Apellido: {cada[1]}")
        item+=1
    