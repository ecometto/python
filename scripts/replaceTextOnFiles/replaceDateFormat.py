import os, io, tarfile, re


def modifySCLContent(content):
    
    print("Original content snippet:", content[:100])  # Muestra los primeros 100 caracteres del contenido original
    contenido_modificado, numero_de_sustituciones = re.subn(pattern, replaceString, content)
    print("Modified content snippet:", contenido_modificado[:100])  # Muestra los primeros 100 caracteres del contenido modificado
    
    if numero_de_sustituciones > 0:
        print(f"\t** There were {numero_de_sustituciones} changes in this file\n")
    else:
        print(f"\t** No changes were made\n")
    return contenido_modificado


def replaceString(match):
    text = match.group(0)
    newText = text.replace('-','/')
    newText = newText[0:-13]
    return newText


def procesar_tar_gz(archivo_tar_gz):
    buffer = io.BytesIO()
    
    print(f"Procesing '${archivo_tar_gz}' ")
    with tarfile.open(archivo_tar_gz, 'r:gz') as tar_original:
        with tarfile.open(fileobj=buffer, mode='w:gz') as tar_modificado:
            for miembro in tar_original.getmembers():
                archivo = tar_original.extractfile(miembro)
                if archivo:
                    # Si es un archivo SCL, modificar su contenido
                    if miembro.name.endswith('.scl'):
                        contenido = archivo.read()
                        print(f"\tEditing file '{archivo.name}'")
                        contenido = modifySCLContent(contenido.decode('utf-8')).encode('utf-8')
                    # Escribir el archivo (modificado o no) en el nuevo tar.gz
                    info = tarfile.TarInfo(name=miembro.name)
                    info.size = len(contenido)
                    tar_modificado.addfile(info, io.BytesIO(contenido))

    # Escribir el buffer al archivo tar.gz original
    with open(archivo_tar_gz, 'wb') as archivo_final:
        archivo_final.write(buffer.getvalue())


#variables
#2024-07-01 01:52:39.300000+00:00
pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}' # Patrón de fecha con milisegundos y zona horaria (Ej: 2024/05/04 15:07:08)
patternOK = r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}' # Patrón con barra en la fecha, sin milisegundos ni zona horaria (Ej: 2024/05/04 15:07:08)
directoryYear = input("Type the 'year' directory: ")
directoryDay = input("Type the 'Ordinal/Julian Day' directory (number of day of the year): ")
basePath = 'C:/xampp/htdocs/programacion/python/scripts/replaceTextOnFiles/'
absPath = f'{basePath}{directoryYear}/{directoryDay}/'


# Uso del código
listOfPassScript = os.listdir(absPath)

for passScript in listOfPassScript:
    tarGzFile = absPath+passScript
    procesar_tar_gz(tarGzFile)
