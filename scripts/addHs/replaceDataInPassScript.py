import os, io, tarfile, re

#AUX FUNCTIONS
def modifySCLContent(content):
    badTimePattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}' # Patrón de fecha con milisegundos y zona horaria (Ej: 2024/05/04 15:07:08)
    AOSPattern = r'AOS = \d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}' # Patrón de fecha con milisegundos y zona horaria (Ej: 2024/05/04 15:07:08)
    LOSPattern = r'LOS = \d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}' # Patrón de fecha con milisegundos y zona horaria (Ej: 2024/05/04 15:07:08)
    AOS_modificado = re.sub(AOSPattern, replaceStringAOS, content)
    LOS_modificado = re.sub(LOSPattern, replaceStringLOS, AOS_modificado)
    contenido_modificado, numero_de_sustituciones = re.subn(badTimePattern, replaceString, LOS_modificado)
    
    if numero_de_sustituciones > 0:
        print(f"\t** Se realizaron {numero_de_sustituciones} modificaciones de formato de hora\n")
    else:
        print("\t** No se realizaron modificaciones.\n")
        
    return contenido_modificado  

def replaceStringAOS(match):
    patternF = r'\d{4}\/\d{2}\/\d{2}'
    patternH = r'\d{2}:\d{2}:\d{2}'
    text = match.group(0)
    newText = re.sub(patternF, AOSDate, text)
    finalText = re.sub(patternH, AOShour, newText)
    return finalText

def replaceStringLOS(match):
    patternF = r'\d{4}\/\d{2}\/\d{2}'
    patternH = r'\d{2}:\d{2}:\d{2}'
    text = match.group(0)
    newText = re.sub(patternF, LOSDate, text)
    finalText = re.sub(patternH, LOShour, newText)
    return finalText

def replaceString(match):
    text = match.group(0)
    newText = text.replace('-','/')
    newText = newText[0:-13]
    return newText


#MAIN FUNCTIONS
def procesar_tar_gz(archivo_tar_gz):
    buffer = io.BytesIO()
    
    print(f"Processing '{archivo_tar_gz}' ")
    with tarfile.open(archivo_tar_gz, 'r:gz') as tar_original:
        with tarfile.open(fileobj=buffer, mode='w:gz') as tar_modificado:
            for miembro in tar_original.getmembers():
                archivo = tar_original.extractfile(miembro)
                if archivo:
                    # Si es un archivo SCL, modificar su contenido
                    if miembro.name.endswith('.scl'):
                        contenido = archivo.read()
                        print(f"\tEditing file '{miembro.name}'")  # Imprime el nombre del archivo SCL
                        contenido = modifySCLContent(contenido.decode('utf-8')).encode('utf-8')
                    else:
                        contenido = archivo.read()  # Si no es un archivo SCL, solo lee el contenido
                    
                    # Escribir el archivo (modificado o no) en el nuevo tar.gz
                    info = tarfile.TarInfo(name=miembro.name)
                    info.size = len(contenido)
                    tar_modificado.addfile(info, io.BytesIO(contenido))

    # Escribir el buffer al archivo tar.gz original
    with open(archivo_tar_gz, 'wb') as archivo_final:
        archivo_final.write(buffer.getvalue())


#variables
basePath = os.getcwd()
print("\n *** ATENTTION *** \nRespect the indicated format \n(in case of error while typing, press 'CRTL+C')  \n")
passScriptName = input("type the passScript to modify (ej: SB1_PassScript_10020240630024045_20240628T192757.tar): ")
absPath = os.path.join(basePath, passScriptName)
AOSDate = input("Type AOS date: (Ej: '2022/10/31'): ")
AOShour = input("Type AOS hour (Format 24hs Ej: '21:50:00': ")
LOSDate = input("Type LOS date: (Ej: '2022/10/31'): ")
LOShour = input("Type LOS hour (Format 24hs Ej: '21:50:00': ")

# Uso del código
procesar_tar_gz(absPath)
