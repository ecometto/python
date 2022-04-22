
#LOS MODULOS DEBEN ESTAR EN EL MISMO DIRECTORIO  (PARA QUE FUNCIONEN DESDE CUALQUIER UBICACION DEBE SER "PAQUETES"
import a2_modulos # aca va el nombre del archivo donde estan las funciones guardadas

#esta es otra orma de importar (para no tener que poner primero el nombre del archivo con el punto para llamarlo)
from a2_modulos import * #aca importa todas las funciones que estan en el archivo modulo


print(a2_modulos.sumar(2,8))
print(a2_modulos.restar(12,8))
print(a2_modulos.multiplicar(2,8))
print(30*"*")


print(sumar(2,3))
print(restar(12,7))
print(multiplicar(2,8))
