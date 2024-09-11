import os, io, tarfile, re
# from dataManager import downloadDataFromNFS



def modifySCLContent(content):
    # textDate, coincidenciasDate = re.subn(patternDateBad, replaceDate, content)
    # textTime, coincidenciasDate = re.subn(patternTimeBad, replaceTime, content)

    text, coincidences = re.subn(pattern, replace, content) 

def replace(match):
    text = match.group(0)
    newText = text.replace('-','/')
    newText2 = newText[:22]
    print(text, " ---> ", newText2)
    return newText

def replaceDate(match):
    text = match.group(0)
    newText = text.replace('-','/')
    print(text, " ---> ", newText)
    return newText

def replaceTime(match):
    text = match.group(0)
    newText = text[:8]
    print(text, " ---> ", newText)
    return newText


def procesar_tar_gz(archivo_tar_gz):
    buffer = io.BytesIO()
    
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
                        # result = SeeSCLContent(contenido.decode('utf-8'))                     
                        res = modifySCLContent(contenido.decode('utf-8'))



#sme.ttcmd.begin(8, 2024/08/24 01:52:39.000000+00:00, SM);
#sme.ttcmd.begin(92, 2024-08-24 08:33:25+00:00, SM);
#pattern = r'\d{4}[-\/]\d{2}[-\/]\d{2} \d{2}:\d{2}:\d{2}(\.\d+[^,]*|\+[^,]*)'

# Variables / #Patterns

#patternDateBad = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2}' # Patrón de fecha con milisegundos y zona horaria (Ej: 2024/05/04 15:07:08)
patternDateBad = r'\d{4}-\d{2}-\d{2}' # Patrón de fecha con milisegundos y zona horaria (Ej: 2024/05/04 15:07:08)
patternTimeBad = r'\d{2}:\d{2}:\d{2}\.+[^,]*|\d{2}:\d{2}:\d{2}\+[^,]*' # Patrón de fecha con milisegundos y zona horaria (Ej: 2024/05/04 15:07:08)
#\d{2}:\d{2}:\d{2}\.\d+[^,]*
pattern = r'\d{4}[-\/]\d{2}[-\/]\d{2} \d{2}:\d{2}:\d{2}(\.\d+[^,]*|\+[^,]*)'

# Variables / #paths
year = "2024"
day = "232"


procesar_tar_gz('C:/xampp/htdocs/programacion/python/scripts/fullPassScriptProcessor/2024/232/SB1_PassScript_11020240823121134_20240819T180526.tar.gz')
    
