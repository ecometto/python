from calendar import c
import json
from math import prod
from sre_constants import CATEGORY_NOT_LINEBREAK
from time import monotonic

# ----------- FUNCIONES -----------------------
def createProduct():
    ultimo=len(productList)
    while True:
        cod=input("ingrese un codigo interno personalizado: ")   
        description=input("ingrese la descripción del producto: ")
        price=float(input("ingrese el precio del articulo: "))
        product={
                    "id": ultimo+1,
                    "cod":cod, 
                    "description": description,
                    "price": price
                }
        productList.append(product)
        saveList()
        # downloadList()
        print("\nArtículo ingresado correctamente")
        continuar=int(input("Continuar Agregando articulos? ( 1-si  /  0- no ) "))
        if continuar==0:
            break
    
    
def saveList():
    with open("./repaso/DDBB.json", "w") as f:
        data['products']=productList
        data['sales']=salesList
        json.dump(data, f, indent=4)
        
        
def downloadLists():
    with open("./repaso/DDBB.json", "r") as f:
        data=json.load(f)
        # productList=data['products']
        # for prod in productList:
        #     print("{:<15} {:<30} {:<15}".format(f"{prod['cod']}" , f"{prod['description']}" , f"{prod['price']}"))
        return data 
    
    
def readProductList():
    if len(productList) == 0:
        print("\n---------------------------------")
        print("     **** NO HAY DATOS PARA MOSTRAR ****     ")
        print("---------------------------------")
    else:
        print("---------------------------------")
        print("\n     **** LISTA DE PRODUCTOS ****     ")
        print("---------------------------------")
        print("{:<10} {:<15}{:<35} {:<15}".format("ID","COD", "DESCRIPCION", "PRECIO"))
        print("{:<10} {:<15}{:<35} {:<15}".format("--", "----","-----------", "------"))
        
        for item in productList:
            print("{:<10}{:<15} {:<35} {:<15}".format(f"{item['id']}", f"{item['cod']}", f"{item['description']}", f"{item['price']}"))
        input("Presione cualquier tecla para continuar..")    


def sales():
    detalle=[]
    lineaDetalle=[]
    exit=1
    
    while exit != 0:
        cod=input("* Ingrese el 'ID'  del producto . (Si no lo conoce presione 'B'): ")
        
        while (cod == "b" or cod == "B"):
            readProductList()
            cod=input("* Ingrese el 'ID'  del producto . (Si no lo conoce presione 'B'): ")
        
        atras=False
        for cada in detalle:
            if int(cod) == cada[0]:
                print("\nEl item ya está cargado en esta compra\n")
                atras=True
                break
        if atras == True:
            continue   

        existe=False
        for item in productList:
            if int(cod) == item['id']:
                lineaDetalle=[]
                idLineaDetalle=item['id']
                descripcionLineaDetalle= item['description']
                precioLineaDetalle= item['price']
                cantLineaDetalle= int(input("ingrese la cantidad: "))
                totalLineaDetalle= precioLineaDetalle * cantLineaDetalle
                lineaDetalle = [idLineaDetalle, descripcionLineaDetalle, precioLineaDetalle, cantLineaDetalle, totalLineaDetalle]
                detalle.append(lineaDetalle)
                print(detalle)
                existe=True
                
        if existe==False:
            print("el codigo ingresado no es valido")
            
        exit=int(input("Carga un nuevo Item? ( 1-si  /  0-no )"))
        if exit == 0:
            print("\nDetalle de la compra:")
            print("-----------------------\n")
            print("{:>10} {:>35} {:>10} {:>10} {:>10}".format("ID","DESCRIPCION","$.UNIT","CANT","$TOTAL"))
            mTotal=0
            for i in detalle:
                mTotal+=i[4]
                print("{:>10} {:>35} {:>10} {:>10} {:>10}".format(f"{i[0]}",f"{i[1]}",f"{i[2]}",f"{i[3]}",f"{i[4]}"))
            print("\MONTO TOTAL: ", mTotal, "\n")
        
            facturar= int(input("desea facturar el detalle ( 1-si  /  0-no )"))
            if facturar == 1:
                print("\n .... PROCESO DE FACTURACIÓN EN MARCHA ...")
                sale={
                        "idVenta": len(salesList)+1,
                        "fecha": f"{now.date()}",
                        "montoTotal": mTotal,
                        "detalle":detalle
                    }
                salesList.append(sale)
                saveList()
                input(" \n Venta registrada correctamente. \nPresione cualquier tecla para continuar ")
                
            if facturar == 0:
                print("saliendo")
        
        
def readSales():
    if len(salesList) == 0:
        print("\n---------------------------------")
        print("     **** NO HAY DATOS PARA MOSTRAR ****     ")
        print("---------------------------------")
    else:
        print("----------------------------------------------------------")
        print("\n               **** LISTA DE VENTAS ****                ")
        print("----------------------------------------------------------")
        
        for item in salesList:
            print("{:<10} {:<15} {:<15}".format("ID","FECHA", "MONTO"))
            print("{:<10} {:<15} {:<15}".format(f"{item['idVenta']}", f"{item['fecha']}", f"{item['montoTotal']}\n"))
            print(" {:<35} {:<15} {:<15}".format("DECRIPCION", "CANT", "SUBTOTAL"))
            for col in item['detalle']:
                print(" {:<35} {:<15} {:<15}".format( f"{col[1]}", f"{col[3]}", f"{col[4]}"))
            
            print("---------------------------------------------------------------------")
            
        input("Presione cualquier tecla para continuar..")    
                
                
def sistema():
    while True:
        print("\nSISTEMA DE VENTAS DE ARTICULOS")
        print("---------------------------------")
        accion=int(input(''' seleccione la opción deseada:
            1- registrar una venta 
            2- Agregar articulos a la Lista de Articulos 
            3- Listar Articulos 
            4- Listar Ventas
            0- SALIR
            Opcion elegida: .. '''))
        if accion == 0:
            salir=int(input("seguro que desea salir? ( 1-PERMANECER  /  0-SALIR )"))
            if salir == 0:
                exit()

        if accion == 1:
            sales()
        elif accion == 2:
            createProduct()
        elif accion == 3:
            readProductList()
        elif accion == 4:
            readSales()


# -------------------------- SISTEMA -----------------------
#VARIABLES GLOBALES ---------
from datetime import datetime
salir=1
data= dict(downloadLists())
productList = list(data['products'])
salesList=list(data['sales'])
print(salesList)
now = datetime.now()



while salir != 0:
    sistema()
print("\nGRACIAS POR OPERAR CON SISTEMAS CED-SISTEMS..\n")
saveList()





#mejoras:
#agregar "status" a los archivos
#agregar los articulos como objetos de clases
#ir guardando "parcialmente" con apertura archivo modo "a"
 