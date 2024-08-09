import time

nanosegundos = int(input("insert a nanosecond value from time.time() class: "))

segundos = nanosegundos // 1e9
nanosegundos_restantes = nanosegundos % 1e9

# segundos a una estructura de tiempo (time.localtime tiempo local - time.gmtime para UTC)
tiempo_struct = time.localtime(segundos)

fecha_formateada = time.strftime("%Y-%m-%d %H:%M:%S", tiempo_struct)

# Añadir los nanosegundos restantes al final
fecha_formateada_con_nanosegundos = f"{fecha_formateada}.{int(nanosegundos_restantes):09d}"

print("Fecha formateada:", fecha_formateada_con_nanosegundos)
