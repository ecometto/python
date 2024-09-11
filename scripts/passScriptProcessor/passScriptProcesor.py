import os, io, tarfile, re, zipfile


def modifySCLContent(content):
    global log
    contenido_modificado, numero_de_sustituciones = re.subn(patternDateTimeBad, replaceString, content)
    
    if numero_de_sustituciones > 0:
        print(f"\t** There were {numero_de_sustituciones} changes in this file\n")
        log += f"\t** There were {numero_de_sustituciones} changes in this file\n\n"
    else:
        print(f"\t** No changes were made\n")
        log += f"\t** No changes were made\n"
    return contenido_modificado


def replaceString(match):
    global log
    text = match.group(0)
    # print("Old Text: " ,text)
    newText = text.replace('-','/')
    newText = newText[0:-13]
    print(f"Old Text: {text} -- New Text: {newText}")
    log += f"Old Text: {text} -- New Text: {newText}\n"
    
    return newText


def SeeSCLContent(content):
    res = []
    type = re.search(pattern, content)
    if "true" in type.group():
        res.append('MAIN')
    elif "false" in type.group():
        res.append('BACKUP')
        
    aos = re.search(AOSPattern, content)
    res.append(aos.group())

    los = re.search(LOSPattern, content)
    res.append(los.group())

    newText,ttc = re.subn(TTPatern, "", content)
    res.append(ttc)
    return res


def procesar_tar_gz(archivo_tar_gz):
    buffer = io.BytesIO()
    
    global log
    log = "\n"
    log += f"FILE: '{archivo_tar_gz}\n'"
    print(f"Processing '{archivo_tar_gz}' ")
    with tarfile.open(archivo_tar_gz, 'r:gz') as tar_original:
        with tarfile.open(fileobj=buffer, mode='w:gz') as tar_modificado:
            for miembro in tar_original.getmembers():
                archivo = tar_original.extractfile(miembro)
                if archivo:
                    contenido = archivo.read()

                    #Filtrando archivo SCL para modificar
                    if miembro.name.endswith('.scl'):
                        print(f"\tEditing file '{miembro.name}'")
                        result = SeeSCLContent(contenido.decode('utf-8'))
                        print(f"\tThe current passScript Type is: {result[0]}\nAOS:{result[1]} \nLOS: {result[2]}")
                        print(f"cantidad de comandos TT: {result[3]}\n\n")
                        log +=f"{miembro.name}: \nType: {result[0]} \nAOS:{result[1]} \nLOS: {result[2]}\nTT Comands: {result[3]}\n\n"
                        
                        contenido = modifySCLContent(contenido.decode('utf-8')).encode('utf-8')

                    # Add File to .tar.gz in memory
                    info = tarfile.TarInfo(name=miembro.name)
                    info.size = len(contenido)
                    tar_modificado.addfile(info, io.BytesIO(contenido))

    # Escribir el buffer al archivo tar.gz original
    with open(archivo_tar_gz, 'wb') as archivo_final:
        archivo_final.write(buffer.getvalue())
    
    return log



# Variables / #Patterns
patternDateTimeBad = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}' # Patrón fecha incorrecta con milisegundos y zona horaria.
pattern = r'MAIN_PASS = [a-z]*;' # Patrón de definición de tipo de pasada
AOSPattern = r'AOS = \d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}' # Patrón de fecha con milisegundos y zona horaria (Ej: 2024/05/04 15:07:08)
LOSPattern = r'LOS = \d{4}\/\d{2}\/\d{2} \d{2}:\d{2}:\d{2}' # Patrón de fecha con milisegundos y zona horaria (Ej: 2024/05/04 15:07:08)
TTPatern = r'Send Time Tagged TC name'

# Variables / #paths
year = input("Type the YEAR of passScripts: ")
day = input("Type the DAY of passScripts: ")
basePath = os.getcwd() 
absPath = os.path.join(basePath,year,day)
log = ""


#EXECUTION:
listOfPassScript = os.listdir(absPath)

for passScript in listOfPassScript:
    tarGzFile = os.path.join(absPath,passScript)
    log += procesar_tar_gz(tarGzFile)
    

# WRITE LOG IN A FILE
with open(f"./log{day}.txt", 'w') as f:
    f.write(log)
