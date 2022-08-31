print("hola mundo")

def evaluacion(nota):

    valoracion = "aprobado"

    if nota<5:
        valoracion = "suspenso"
    return valoracion

print (evaluacion(4))


print ("")

print("programa de evaluacion de alumnos")

def evaluacion2(nota):
nota_alumno = input()

    if nota<5:
        valoracion = "suspenso"
    return valoracion


print (evaluacion2)
