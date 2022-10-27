
from operator import truediv


class auto():
    def __init__(self, marca, modelo, color, anio):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.anio = anio
        self.__encendido = False

    def getEncendido(self):
        if self.__encendido:
            return f'el vehículo {self.marca}-{self.modelo} está ENCENDIDO'
        else:
            return f'el vehículo {self.marca}-{self.modelo} está APAGADO'
 
    
    def setArrancarParar(self):
        if self.verificar():
            self.__encendido = not self.__encendido
        else:
            print('El auto tuvo problemas durante la verificación. No se puede arrancar')
            
    
    def verificar(self):
        nafta = True
        aceite = True
        otros = False
        if nafta and aceite and otros:
            return True
        else:
            return False
    

a1 = auto('fiat', 'duna', 'rojo', 1985)


class moto(auto):
    pass

moto1 = moto('honda', 'blazer', 'negro', 2005)

print(moto1.getEncendido())