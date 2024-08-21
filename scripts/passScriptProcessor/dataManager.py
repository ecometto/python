import subprocess, time, os, shutil, datetime
from datetime import datetime


def downloadDataFromNFS():
    year = input("Type the YEAR of passScripts: ")
    day = input("Type the DAY of passScripts: ")
    basePath = f"./2024-original/{year}/{day}/"
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    
    try:    
    
        subprocess.run([ "scp", "-r", basePath, "./passScript/" ] , check=True)
        subprocess.run([ "scp", "-r", basePath, "./backup/" ] , check=True)
        print("Archivo(s) copiado(s) exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al copiar los archivos: {e}") 


    return [year, day]
        

downloadDataFromNFS()



        



def uploadDataToNFS():
    comando_scp = [
        "scp", 
        "-r", 
        "./2024-modified",
        "administrator@192.168.65.110:/kubernetes/products-manager/products-repo/PRODUCT/SB1/PassScript/2024/"
    ]

    try:
        subprocess.run(comando_scp, check=True)
        print("Archivo(s) copiado(s) exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al copiar los archivos: {e}")
    
# downloadDataFromNFS()
# time.sleep(2) 
# uploadDataToNFS()