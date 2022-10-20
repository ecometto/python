# ejercicio 2-2) De la galería de productos, el usuario introducirá el código y el número de unidades del producto que desea comprar. El programa determinará el total a pagar, como una factura.
# Una variante a este ejercicio que lo haría un poco más complejo sería dar la posibilidad de seguir ingresando diferentes códigos de productos con sus respectivas cantidades, y cuando el usuario desee terminar el cálculo de la factura completa con todas sus compras. Te animas??
def factura(list):
    detRenglon=[]
    continuar=True
    existe=False

            
    while continuar==True:
        existe==False
        for prenda in list:
            print(f"{prenda[0]} - {prenda[1]}")
        
        prod=int(input("seleccione el codigo de producto de la lista (press 0 to leave): "))
        if prod == 0:
            break
        cant=int(input("ingrese la cantidad: "))
        
        for cada in list:
            
            salida=False
            # validando si ya existe en la lista 
            for item in detRenglon:
                if prod in item:
                    print("\n **El item ya fue ingresado **")
                    salida=True
            if salida == True:
                break
            else:    
                if prod in cada:
                    subtotal=cant*cada[2]
                    cada.extend((cant, subtotal))
                    detRenglon.append(cada)
                    existe=True
    
        if existe==False:
            print("\n** El codigo ingresado no es correcto **")
            break
            
        montoTotal=0
        for renglon in detRenglon:
            montoTotal+=renglon[4]

        #DETALLES DE PARCIAL:
        print("\n---------------------------")   
        print("Detalle Parcial:")
        for cada in detRenglon:
            print(cada)      
        print("---------------------------")   
        print(f"Total de productos: {len(detRenglon)}")
        print(f"Monto total de compra: {montoTotal}")
        print("---------------------------\n")   
        
        
         #confirmación de de nuevo renglon
        res=input("desea seguir agregando productos? ( 1=si  /  0=no )")
        if res == "0":
            
            #confirmación de facturación
            fact=input("Desea facturar o salir ( 1=facturar  /  0=salir )")
            if fact == "1":
                #DETALLES DE FACTURA:
                print("\n---------------------------")   
                print("DETALLE DE LA FACTURA:")
                for cada in detRenglon:
                    cod, desc, PU, cant, PT = cada
                    print ("{:<15} {:<15} {:<15} {:<15} {:<15}".format( cod, desc, PU, cant, PT))
           
                print("---------------------------")   
                print(f"Total de productos: {len(detRenglon)}")
                print(f"Monto total de compra: {montoTotal}")
                print("---------------------------\n")   
                confirmar=input("confirmar la factura: ( 1-si  /  0-no )")
                if confirmar == "1":
                    print("su factura ha sido emitida correctamente. \nMuchas Gracias")
                    continuar= False
            elif fact == "0":
                print("Su factura no será impresa. \nMuchas gracias")
                continuar= False
        else:
            continue
                
        
    
listaProductos=[
    [101, "pantalon" , 5000],
    [102, "remera" , 2000],
    [103, "calzoncillo" , 1000],
    [104, "camisa" , 4000],
    [105, "chaleco" , 3000],
    [106, "campera" , 10000]
]
    
factura(listaProductos)