from tkinter import *

raiz = Tk()
raiz.title("Calculadora de Pruebas")
miframe = Frame(raiz)
miframe.config(width=600, height=400)
miframe.pack()

#------------- VARIABLES GLOBALES -------------
operacion = ""
resultado_parcial = 0
ultimo_signo = ""

#-------------PANTALLA---------------
numeropantalla=StringVar()
pantalla=Entry(miframe, textvariable=numeropantalla)
pantalla.grid(row=0, column=0, padx=10, pady=10, columnspan=4)
pantalla.config(bg="#4F3F3C", fg="white", justify="right")

#------FUNCIONES DE BOTONES de OPERACIONES -------------
def suma():
    global operacion
    global ultimo_signo
    global resultado_parcial
    global numeropantalla
    operacion = "suma"
    ultimo_signo = "+"

def resta():
    global operacion
    global ultimo_signo
    global resultado_parcial
    operacion = "resta"
    ultimo_signo = "-"

def multiplicacion():
    global operacion
    global ultimo_signo
    global resultado_parcial
    operacion = "multiplicacion"
    ultimo_signo = "*"

def division():
    global operacion
    global ultimo_signo
    global resultado_parcial
    operacion = "division"
    ultimo_signo = "/"

def numeropulsado(num):
    global operacion
    global resultado_parcial

    if operacion=="total":
        resultado_parcial = 0
        numeropantalla.set(num)
        operacion=""
    else:
        if operacion == "":
            numeropantalla.set(numeropantalla.get()+num) #esta fila es para concatenar cada numero pulsado
        else:
            if operacion == "suma":
                resultado_parcial = resultado_parcial + float(numeropantalla.get())
                numeropantalla.set(num)
                print(resultado_parcial)
                operacion = ""
            elif operacion == "resta":
                if resultado_parcial == 0:
                    resultado_parcial = float(numeropantalla.get())
                    numeropantalla.set(num)
                    print(resultado_parcial)
                    operacion = ""
                else:
                    resultado_parcial = resultado_parcial-float(numeropantalla.get())
                    numeropantalla.set(num)
                    print(resultado_parcial)
                    operacion = ""
            elif operacion == "multiplicacion":
                if resultado_parcial == 0:
                    resultado_parcial = float(numeropantalla.get())
                    numeropantalla.set(num)
                    print(resultado_parcial)
                    operacion = ""
                else:
                    resultado_parcial = resultado_parcial*float(numeropantalla.get())
                    numeropantalla.set(num)
                    print(resultado_parcial)
                    operacion = ""
            elif operacion == "division":
                if resultado_parcial == 0:
                    resultado_parcial = float(numeropantalla.get())
                    numeropantalla.set(num)
                    print(resultado_parcial)
                    operacion = ""
                else:
                    resultado_parcial = resultado_parcial/float(numeropantalla.get())
                    numeropantalla.set(num)
                    print(resultado_parcial)
                    operacion = ""

def igual():
    global resultado_parcial
    global operacion
    if ultimo_signo == "+":
        numeropantalla.set(int(numeropantalla.get()) + resultado_parcial)
        operacion = "total"
        resultado_parcial=0

    elif ultimo_signo == "-":
        numeropantalla.set(resultado_parcial-int(numeropantalla.get()))
        operacion = "total"
        resultado_parcial=0

    elif ultimo_signo == "*":
        numeropantalla.set(resultado_parcial * int(numeropantalla.get()))
        operacion = "total"
        resultado_parcial = 0

    elif ultimo_signo == "/":
        numeropantalla.set(resultado_parcial / int(numeropantalla.get()))
        operacion = "total"
        resultado_parcial = 0






#------------BOTONES-------------------
#***** primera fila*********
boton7 = Button(miframe, text="7", width=3, command=lambda:numeropulsado("7"))
boton7.grid(row=1,column=0)
boton8 = Button(miframe, text="8", width=3, command=lambda:numeropulsado("8"))
boton8.grid(row=1,column=1)
boton9 = Button(miframe, text="9", width=3, command=lambda:numeropulsado("9"))
boton9.grid(row=1,column=2)
botonsuma = Button(miframe, text="+", width=3, command=lambda:suma())
botonsuma.grid(row=1,column=3)

#***** segunda fila*********
boton4 = Button(miframe, text="4", width=3, command=lambda:numeropulsado("4"))
boton4.grid(row=2,column=0)
boton5 = Button(miframe, text="5", width=3, command=lambda:numeropulsado("5"))
boton5.grid(row=2,column=1)
boton6 = Button(miframe, text="6", width=3, command=lambda:numeropulsado("6"))
boton6.grid(row=2,column=2)
botonresta = Button(miframe, text="-", width=3, command=lambda:resta())
botonresta.grid(row=2,column=3)

#***** tercera fila*********
boton1 = Button(miframe, text="1", width=3, command=lambda:numeropulsado("1"))
boton1.grid(row=3,column=0)
boton2 = Button(miframe, text="2", width=3, command=lambda:numeropulsado("2"))
boton2.grid(row=3,column=1)
boton3 = Button(miframe, text="3", width=3, command=lambda:numeropulsado("3"))
boton3.grid(row=3,column=2)
botonmultiplica = Button(miframe, text="*", width=3, command=lambda:multiplicacion())
botonmultiplica.grid(row=3,column=3)

#***** ultima fila*********
boton0 = Button(miframe, text="0", width=3, command=lambda:numeropulsado("0"))
boton0.grid(row=4,column=0)
botonpunto = Button(miframe, text=".", width=3, command=lambda:numeropulsado("."))
botonpunto.grid(row=4,column=1)

botonigual = Button(miframe, text="=", width=3, command=lambda: igual())
botonigual.grid(row=4,column=2)
botondivide = Button(miframe, text="/", width=3, command= lambda:division())
botondivide.grid(row=4,column=3)


#botonborrarU=Button(miframe, text="C", width=9)
#botonborrarU.grid(row=5,column=0, columnspan=2)

#botonborrar=Button(miframe, text="CE", width=9)
#botonborrar.grid(row=5,column=2, columnspan=2)




raiz.mainloop()