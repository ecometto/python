import os.path
import subprocess, time, os, shutil
from datetime import datetime


def downloadDataFromNFS():
    year = input("Type the YEAR of passScripts: ")
    day = input("Type the DAY of passScripts: ")
    NFSpath = f"administrator@192.168.65.110:/home/administrator/{year}/{day}/"
#    NFSpath = f"administrator@192.168.65.110:/kubernetes/products-manager/products-repo/PRODUCT/SB1/PassScript/{year}/{day}/"
    currentPath = os.getcwd()
    backupPath = os.path.join(currentPath, 'backup')
    finalLocalPath = os.path.join(currentPath, year)
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    
    if os.path.exists(finalLocalPath):
        shutil.rmtree(finalLocalPath)
        print("directory structure updated")
    
    os.makedirs(finalLocalPath)

    try:    
        subprocess.run([ "scp", "-r", NFSpath, finalLocalPath ] , check=True)
        print("\n** Archivo(s) copiado(s) exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"\n** Error al copiar los archivos: {e}") 

    try:    
        subprocess.run([ "cp", "-r", finalLocalPath, backupPath ] , check=True)
        print("\n** BackUp realizado\n")
    except subprocess.CalledProcessError as e:
        print(f"\n** Error al realizar backup: {e}") 





def uploadDataToNFS():
    year = input("Type the YEAR of passScripts: ")
    day = input("Type the DAY of passScripts: ")
    NFSpath = f"administrator@192.168.65.110:/home/administrator/{year}"
    # NFSpath = f"administrator@192.168.65.110:/kubernetes/products-manager/products-repo/PRODUCT/SB1/PassScript/{year}/{day}/"
    currentPath = os.getcwd()
    originPath=os.path.join(currentPath,year,day)
    
    comando_scp = [
        "scp", 
        "-r", 
        originPath,
        NFSpath
    ]


    try:
        subprocess.run(comando_scp, check=True)
        print("Archivo(s) copiado(s) exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al copiar los archivos: {e}")
    
    
 
print("\n\t *** DATA MANAGER *** \n")
res = input("Type: \n- 1 for DOWNLOAD passScripts data or \n- 2 for UPLOAD processed passScript:   ")

if res == "1":
    print("Downloading data")
    time.sleep(1)
    downloadDataFromNFS()
elif res =="2":
    print("Uploading data")
    time.sleep(1)
    uploadDataToNFS()
else:
    print("Request coud not be processed. Try again in other moment.")

