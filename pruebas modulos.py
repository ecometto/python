
#LOS MODULOS DEBEN ESTAR EN EL MISMO DIRECTORIO  (PARA QUE FUNCIONEN DESDE CUALQUIER UBICACION DEBE SER "PAQUETES"
import modulos # aca va el nombre del archivo donde estan las funciones guardadas

modulos.sumar(2,8)
modulos.restar(12,8)
modulos.multiplicar(2,8)

print("*"*30)
#esta es otra orma de importar (para no tener que poner primero el nombre del archivo con el punto para llamarlo)
from modulos import * #aca importa todas las funciones que estan en el archivo modulo

sumar(2,3)
restar(12,7)
multiplicar(2,8)

from clasesyobjetos import *
micoche = Vehiculos("chevrolet","prisma")
micoche.estado() #aca va a traer todo el archivo que contiene otras cosas...