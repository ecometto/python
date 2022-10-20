
from random import choice, randint, shuffle

# Ejercicio 1
# Diseñar un sistema de puntos para el juego El reino del dragón:
# Dejo el enlace por si alguien no lo vio.
# La idea es la siguiente: mientras el jugador vaya ganando, ira acumulando puntos.
# Ejemplo: Si el jugador entra en la primera cueva y gana el tesoro, se le acreditan 100 puntos, entra en la segunda cueva y gana el tesoro, se le acreditan otros 100 puntos. Si el jugador pierde, saldrá en pantalla el total de los puntos que realizo y la opción de empezar de nuevo.

# ---------------- no se entiende la consigna ---------------------


# Ejercicio 2
# Escribe un programa que te permita jugar a una versión simplificada del juego Master Mind. El juego consistirá en adivinar una cadena de números distintos. 
# #Al principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras). Después el programa debe ir pidiendo que intentes adivinar la cadena de números. En cada intento, el programa informará de cuántos números han sido acertados (el programa considerará que se ha acertado un número si coincide el valor y la posición)

# Ejemplo:
# Dime la longitud de la cadena: 4
# Intenta adivinar la cadena: 1234
# Con 1234 has adivinado 1 valores. Intenta adivinar
# la cadena: 1243
# Con 1243 has adivinado 0 valores. Intenta adivinar
# la cadena: 1432
# Con 1432 has adivinado 2 valores. Intenta adivinar
# la cadena: 2431
# Con 2431 has adivinado 4 valores. Felicitaciones
def adivinaNum1():
    cifras=int(input("\nIngrese cantidad de cifras:.."))
    hasta=(10**cifras)-1
    numero=randint(1,hasta)
    print("numero: ", numero)
    match=False
    coincidencias=0
    while match != True:
        userNum=input(f"Intente adivinar el númer de {cifras} cifras:.. (press 0 to leave)")
        if userNum == 0:
            exit
        coincidencias=0
        for i in range(0,cifras):
            print(str(numero)[i])
            print(str(userNum)[i])
            if str(numero)[i] == str(userNum)[i]:
                coincidencias+=1
        
        if coincidencias < cifras:
            print(f"Tiene {coincidencias} coincidencias")
            print("Intente con un nuevo numnero")
        else:
            print("HA ENCONTRADO EL NUMERO.. FELICITACIONES")
            match = True

# adivinaNum1()
        
    
    

# Ejercicio 3
# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
def rimas():
    p1=input("ingrese una palabra para comparar si rima:..")
    p2=input("ingrese otra palabra:..")
    coincide2=False
    coincide3=False
    for i in -2,-3:
        if p1[i] == p2[i]:
            if i==-2:
                coincide2=True
            if i==-3:
                coincide3=True
    if coincide2==True and coincide3==True:
        print("RIMA..")
    if coincide2==True and coincide3==False:
        print("RIMA MEDIO POCO..")
    if coincide2==False and coincide3==False:
        print("NO RIMAN NADA..")

# rimafloat
    




# Ejercicio 4
# Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada año se aplica la tasa de interés introducida.
# Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en C * (1 + x/100)elevado a n (años). Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de interés anual se convierte en 24117.14 dolares al cabo de 20 años.
def calcRendimiento():
    monto=float(input("ingrese el importe: "))
    interes=float(input("ingrese el interes anual: "))
    plazo=float(input("ingrese el plazo en años: "))

    montoFinal= (monto)*(1+(interes/100))**plazo
    print(round(montoFinal,2))

# calcRendimiento()





# Ejercicio 5
# Has un programa que te solicite la cantidad de cifras de un número RANDOM a adivinar. vas ingresando opciones por teclado.
def adivinaNum():
    match = False;  userNums = [];   cantCifras = int(input("ingrese la cantidad de cifras:.. "))
    hasta = (10**cantCifras)-1; num = randint(1, hasta);   num=str(num)
    print(num)
    while match == False:
        user = input(f"ingrese un numero de {cantCifras} cifras:.. ")
        userNums.append(user)
        #for n in num:
        if num != user:
            if int(num) > int(user):
                print("numero incorrecto. (Intente con un numero mayor)")
                print(f"Numeros hasta el momento: {userNums} \n")
            else:
                print("numero incorrecto. (Intente con un numero menor)")
                print(f"Numeros hasta el momento: {userNums} \n")
        else:
            print("\n---------------------------")
            print(f"encontrado en {len(userNums)} intentos")
            print("---------------------------\n")
            match = True

# adivinaNum()


# ejercicio 1-1) Este programa pide primeramente la cantidad total de compras de una persona. Si la cantidad es inferior a $100.00, el programa dirá que el cliente no aplica a la promoción. Pero si la persona ingresa una cantidad en compras igual o superior a $100.00, el programa genera de forma aleatoria un número entero del cero al cinco. Cada número corresponderá a un color diferente de cinco colores de bolas que hay para determinar el descuento que el cliente recibirá como premio. Si la bola aleatoria es color blanco, no hay descuento, pero si es uno de los otros cuatro colores, sí se aplicará un descuento determinado según la tabla que  aparecerá, y ese descuento se aplicará sobre el total de compra que introdujo inicialmente el usuario, de manera que el programa mostrará un nuevo valor a pagar luego de haber aplicado el descuento.






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
                    print(cada)    
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

# duscado=int(input("ingrese codigo"))
# for prod in listaProductos:
#     if duscado in prod:
#         print("encontrado")







# jercicio 2-2) Este programa muestra primero el listado de categorías de películas y pide al usuario que introduzca el código de la categoría de la película y posterior a ello pide que el usuario introduzca el número de días de atraso, y así se muestra al final el total a pagar.