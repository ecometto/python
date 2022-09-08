import random
import pickle


class persona():
    def __init__(self, nombre, apellido, dni, mail):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.mail = mail


class AccionesDeListaPersonas():
    def setpersona():
        continuar = ""
        while continuar != "0":
            nombre = input('Ingrese Nombre de la persona: ')
            apellido = input('Ingrese apellido de la persona: ')
            DNI = input('Ingrese DNI de la persona: ')
            mail = input('Ingrese mail de la persona: ')
            p = persona(nombre, apellido, DNI, mail)
            listaPersonas.append(p)
            continuar = input(
                'Guardado correctamente. (press 0 para salir o 1 para agregar nuevo)')

    def borrarlista(self):
        vaciarArchivo()

    def setRandomPerson(self):
        continuar = ""
        while continuar != "0":
            nombre = self.ramdonPersonaNombre()
            apellido = self.ramdonPersonaApe()
            DNI = random.randint(1000000, 40000000)
            mail = self.ramdonPersonaMail()

            p = persona(nombre, apellido, DNI, mail)
            listaPersonas.append(p)

            continuar = input(
                'Guardado correctamente. (press 0 para salir o 1 para agregar nuevo)')

    def ramdonPersonaNombre(self):
        nombres = ['juan', 'jose', 'pedro', 'paco', 'diego', 'danilo', 'damian',
                   'matias', 'laura', 'maria', 'ester', 'romina', 'lucia', 'graciela']
        nombre = random.choice(nombres)
        return nombre

    def ramdonPersonaApe(self):
        apellidos = ['lopez', 'perez', 'juarez', 'rodriguez', 'affani', 'groetzner', 'aguirre',
                     'chaves', 'cometto', 'ricciutti', 'ibarlucea', 'bilardo', 'cuffia', 'recalde']
        apellido = random.choice(apellidos)
        return apellido

    def ramdonPersonaMail(self):
        ape = self.ramdonPersonaApe()
        mails = ['gmail', 'hotmail', 'yahoo', 'outlook']
        mail = ape + '@' + random.choice(mails) + '.com'
        return mail

    def listarPersonas():
        print('*' * 20)
        if len(listaPersonas)>0:
            for i in listaPersonas:
                print(
                    f"Nombre y Apellido: {i.nombre} {i.apellido} - DNI: {i.dni} mail: {i.mail}")
            print('*' * 20)
        else:
            print('NO SE ENCONTRARON DATOS PARA LISTAR ..\n')


def AbrirParaLeeryModificar():
    try:
        file = open('aaPickle', 'ab+')
        file.seek(0)
        data = pickle.load(file)
        file.close()
        return data
    except:
        data = []
        return data


def GuardarArchivo():
    file = open('aaPickle', 'wb')
    pickle.dump(listaPersonas, file)
    file.close
    
def vaciarArchivo():
    vacio = []
    file = open('aaPickle', 'wb')
    pickle.dump(vacio, file)
    file.close
    listaPersonas.clear()


#  **************************************************
# SISTEMA
listaPersonas = []
listaPersonas = AbrirParaLeeryModificar()

print('Bienvenido al sistema \n')
opciones = ""
while opciones != 4:
    opciones = int(input(
        'Ingrese la opcion deseada \n1- Ingresar Persona \n2- Listar personas \n3- Borrar lista completa \n4-Salir del sistema \n'))

    if opciones == 1:
        ran = int(input('1- generar random?? - 2-generacion manual'))
        if ran == 1:
            alp = AccionesDeListaPersonas()
            alp.setRandomPerson()
        else:
            alp = AccionesDeListaPersonas.setpersona()
    elif opciones == 2:
        alp = AccionesDeListaPersonas.listarPersonas()
        input('press ENTER to continue')
    elif opciones == 3:
        continuar = int(input ('está seguro que quiere borrar todo? \n(Opciones: 1= si  / 0 = no) '))
        if continuar==1:
            res = AccionesDeListaPersonas()
            res.borrarlista()
            # vaciarArchivo()
    elif opciones == 4:
        GuardarArchivo()
