# prueba con modulos en otro directorio 
# forma 1 de importar solo las funciones necesarias 
# from prueba.modulos import suma, resta 
# print(suma(3,5))
# print(resta(9,2))

# forma 2: importar todo el modulo 
import prueba.modulos as modulo
print(modulo.suma(1, 8))
print(modulo.resta(8,3))