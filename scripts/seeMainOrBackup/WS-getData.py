import subprocess

def getDataFromNFS():
    comando_scp = [
        "scp", 
        "-r", 
        "administrator@192.168.65.110:/kubernetes/products-manager/products-repo/PRODUCT/SB1/PassScript/2024/", 
        "./"
    ]

    try:
        subprocess.run(comando_scp, check=True)
        print("Archivo(s) copiado(s) exitosamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al copiar los archivos: {e}")


