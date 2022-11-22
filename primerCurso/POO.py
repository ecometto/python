
class ninjas():
    def __init__(self, nombre, hp, vidas):
        self.nombre = nombre
        self.hp = hp
        self.vidas = vidas

    def saltar(self):
        self.hp -= 1
        if self.hp<98 :
            print("estas a punto de morir")

ninja1 = ninjas("sakaxhama",100,3)
ninja2 = ninjas("tukusaky", 50, 3)

print(ninja1.hp)

ninja1.saltar()
ninja1.saltar()
ninja1.saltar()

print(ninja1.hp)

class Alumnos():
    universidad = "UTN"                                     # Atributo fuera del init para que no sea "editable". se autogenera al crear el objeto
    def __init__(self, apellido, nombre, curso, materias):  #Atributo dentro del INIT para que sean incluidos al momento de cargar.
        self.apellido = apellido
        self.nombre = nombre
        self.curso = curso
        self.materias = []

    def mostrar_datos(self):
        print("el apellido del alumno es: ", self.apellido)
        print("el nombre del alumno es: ", self.nombre)
        print("el curso del alumno es: ", self.curso)
        print("Las materias del alumno es: ", self.materias)

al1 = Alumnos("Garcia", "pedro",2, "ninguna")
al1.materias.append("ingles")                                   #se agrega solo un item a la lista
al1.materias.extend(["ciencias","geografia", "mat", "lengua"])  #se agregan varios items a la lista

print(f" las materias son: .............. , {al1.materias}")
print(f" Mostrando datos: \n {Alumnos.mostrar_datos(al1)}")


al1.materias.remove("mat")

print(al1.materias)
print(al1.universidad)

print("***************************")

# class AlumnosVisita(Alumnos):
#     universidad = "OTRAS"
#     def __init__(self, apellido, nombre, curso, materias, procedencia):
#         self.procedencia = procedencia
#         super().__init__(apellido, nombre, curso, materias)

#     def mostrar_datos(self):
#         super().mostrar_datos()
#         print("la procedencia del alumno es: ", self.procedencia)

# al2 = AlumnosVisita("Correa", "rafael", 5,[], "Alemania")
# al3 = AlumnosVisita("juarez", "pedri", 4,["mat"], "noruega")
# al4 = AlumnosVisita("rodriguez", "raaul", 3,["lengua","idiomas"], "espana")

# print("el alumno ", al2.apellido,
#       "proviene de la Universidad", al2.universidad, "y viene de "
#       , al2.procedencia) #ver que imprime la universidad por defecto para la subclase, agrega la procedencia y hereda los demas atributos.
# print("--------------------")
# al2.mostrar_datos()
# print("--------------------")
# al3.mostrar_datos()

# # POLIMORFISMO.................. UN OBJETO PUEDE TOMAR MAS DE UNA FORMA
# class Coche():
#     def desplazamiento(self):
#         print("me desplazo en cuatro ruedas")
# class Moto():
#     def desplazamiento(self):
#         print("me desplazo en dos ruedas")
# class Camion():
#     def desplazamiento(self):
#         print("me desplazo en ocho ruedas")
# miVehiculo = Moto()
# #mi_vehiculo.desplazamiento()
# miVehiculo2 = Coche()
# miVehiculo3 = Camion()

# #Se crea una funcion (metodo) que englobara los 3 metodos anteriores
# def desplazamiento_vehiculos(vehiculo):
#     vehiculo.desplazamiento()

# desplazamiento_vehiculos(miVehiculo)
# desplazamiento_vehiculos(miVehiculo2)
# desplazamiento_vehiculos(miVehiculo3)