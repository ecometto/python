# FORMAS DE CREAR UN DICCIONARIO:
#opcion 1:
dicCliente=dict()
dicCliente['nombre']="Cliente numero 1"
dicCliente['direccion']= "las tejas 442. Cordoba"
dicCliente['email']= "maildelcliente@gmail.com"
print(f"* Cliente: {dicCliente['nombre']} - Direccion: {dicCliente['direccion']}. \n  Mail: {dicCliente['direccion']}")  

# opcion 2
dict2=dict(nombre="Juan", edad=30, direccion="las colmenas", casado=True)
print(f"El Sr. {dict2['nombre']} tiene {dict2['edad']}. Vive en {dict2['direccion']} y es {'casado' if dict2['casado'] else 'soltero'}")

# opcion 3:
dictNotas={"edy": 95, "romulo": 40, "Ceci":90, "Lila": 83}

#CORMAS DE ITERAR DICCIONARIOS:
for claves in dictNotas.keys(): # si no se especifica, itera las claves (KEYS)    
    print(f"Alumno {claves}: {dictNotas[claves]}")

for valores in dictNotas.values(): 
    print(f"Notas: {valores}")
    
for cada in dictNotas.items(): # aqui toma "cada" como una tupla "clave-valor"
    print(f"\n Alumno: {cada[0]} - Nota: {cada[1]}")
    print(cada)

#(el ordenamiento por defecto es POR CLAVE. y muestra solo la clave)
print("--------")
print(dict2)

#ordenando por CLAVE y mostrando ambos (clave y valor) se agrega .items()
print("-------- SORTED")
print(sorted(dict2.items(), reverse=False))

# si se quiere pordenar POR VALOR mostrando ambos, entonces se debe importar MODULO OPERATOR.
# PARA ESTE CASO, no se podrá ordenar por valor, ya que son de distintos tipos. Se ordenará por clave (itemgetter(0))
import operator
print(sorted(dict2.items(), key=operator.itemgetter(0)))
#VER EJERCICIOS 4