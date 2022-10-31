# EJEMPLO DE CLASES Y OBJETOS
class Estudiantes:
    def __init__(self, apellido, nombre, DNI, direccion, ciudad):
        self.apellido = apellido
        self.nombre = nombre
        self.DNI = DNI
        self.direccion = direccion
        self.ciudad = ciudad

bebo = Estudiantes("Cometto","Cecilia", "43770588", "peredo 1067", "Cordoba")
papa = Estudiantes("Cometto","Edgardo", "27461985", "peredo 1067 A", "Esperanza")
mama = Estudiantes("Garcia","Patricia", "28657403", "peredo 1067 B", "CBA City")

print("papa:", papa.direccion, "- mama:", mama.direccion, "- bebo:", bebo.direccion)


# EJEMPLOS DE HERENCIA (superclase y subclase)
class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.arrancar = False
        self.acelerar=False
        self.frenar =False

    def arranca(self,arranco):
        self.arrancar = arranco
        if self.arrancar:
            return "el auto arranco"
        else:
            return "el auto esta apagado"

    def acelera(self):
        acelerar=True

    def frena(self):
        frenar=True

    def estado(self):
        print("marca: ", self.marca, "modelo: ", self.modelo, "\nArranca: ", self.arrancar, "\nAcelerar", self.acelerar,
              "\nFrenar: ", self.frenar)

class Moto(Vehiculos):
    hcaballito = "nada"
    def caballito(self):
        self.hcaballito = "voy haciendo willi"

    def estado(self):
        print("marca: ", self.marca, "modelo: ", self.modelo, "\nArranca: ", self.arrancar, "\nAcelerar", self.acelerar,
              "\nFrenar: ", self.frenar, "\ncaballito: ", self.hcaballito)

class Furgoneta(Vehiculos):
    cargado ="sin carga"
    def cargar(self):
        print("estoy cargado")


auto1 = Vehiculos("BMW","301 clk")
moto1= Moto("honda","CBR600")

#moto1.caballito()

print("*"*30)
print(auto1.estado(), "\n",auto1.arranca(False))
moto1.estado()

# POLIMORFISMO (MAS DE UNA FORMA)
print("*"*30)
class PAuto():
    def movimiento(self):
        print("movimiento en 4 ruedas")
class PCamion():
    def movimiento(self):
        print("movimiento en 6 ruedas")
class PMoto():
    def movimiento(self):
        print("movimiento en 2 ruedas")

def mimovimiento(tipo): #ESTA ES LA FUNCION QUE PERMITE QUE CAMBIANDO SOLO EL TIPO DE OBJETO SE REDIRECCIONE A LA FUNCNION
    tipo.movimiento()

mivehiculo = PCamion()
mivehiculo2 = PAuto()

print("*"*30)
print(mimovimiento(mivehiculo))
print(mimovimiento(mivehiculo2))

# CADENAS DE TEXTO (lower, upper, capitalize, split (separa por palabras usando espacios), isdigit(true/false),
# find (indice), # isalum (alfanumerico), isalpha(alfabetico), strip(borra espacios inicio y final), replace (reemplaza)
NombreUsuario = input("ingrese un nombre: ")
Edad = input("introduce tu edad: ")

print("el nombre de usuario es: ", NombreUsuario.lower())
print("el nombre de usuario es: ", NombreUsuario.upper())
print("el nombre de usuario es: ", NombreUsuario.isalpha())

while Edad.isdigit()!= True:
    print("Por favor introduce nuevamente tu edad")
    Edad = int(input("introduce tu edad: "))
print("Edad cargada correctamente")

if int(Edad) <18:
    print("lo sentimos", NombreUsuario, "Este sitio es solo para mayores de 18")
else:
    print("bienvenido", NombreUsuario)




