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


import pickle

# # generando archivo y volcándole datos
enMemoria = open('aaa', 'wb')
data = []
dato = ['Edgardo', 'cometto']
data.append(dato)
pickle.dump(data, enMemoria)
enMemoria.close()

# leyendo archivo a+


def AbrirParaLeeryModificar():
    file = open('aaa', 'ab+')
    file.seek(0)
    data = pickle.load(file)
    file.close()
    return data


data = AbrirParaLeeryModificar()
dato2 = ['nombre2', 'apellido2']
data.append(dato2)


file = open('aaa', 'wb')
pickle.dump(data, file)
file.close()

data = AbrirParaLeeryModificar()
for dato in data:
    print(dato)
