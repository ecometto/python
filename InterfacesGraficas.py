from tkinter import *

raiz =Tk()
raiz.title ("Ventana Grafica de Pruebas")

#raiz.geometry("800x600")
raiz.config(bg="gray")


miFrame = Frame()
miFrame.pack(side="left", anchor="n") # posiciona al frame a la izquierda y arriba (n=norte)
miFrame.config(bg="grey")
miFrame.config(width= "800", height="800")
miFrame.config(bd=50,cursor="hand2") #tamano borde, relieve borde y cursor cuando se posiciona
miFrame.grid_propagate(False)


#miLabel = Label(miFrame)
#miLabel.place(x="20", y="20")
#miimagen = PhotoImage(file="imagenpng.png")
#miLabel.config(image =miimagen)


milabel2= Label(raiz)
milabel2.place(x="5", y="5")
milabel2.config(text="hola. bienvenidos python", bg="red", fg="yellow", font=20)

milabel3= Label(miFrame, text="Nombre y Apellido", font=14, bg="white")
milabel3.grid(row=0,column=0,padx=10, pady=10, sticky="e")

DNI= Label(miFrame, text="DNI", font=14, bg="white")
DNI.grid(row=1,column=0, padx=10, pady=10, sticky="e")

PASS = Label(miFrame, text="PASSWORD", font=14, bg="grey")
PASS.grid(row=2, column=0, padx=10, pady=10, sticky="e")

comentarios= Label(miFrame, text="COMENTARIOS", font=14, bg="grey")
comentarios.grid(row=3, column=0,padx=10, pady=10, sticky="n")


#******************************************************************************
minombre = StringVar()
cuadroNombre = Entry(miFrame, justify="center", textvariable=minombre)
cuadroNombre.grid(row=0,column=1,padx=1, pady=10)

cuadroDNI = Entry(miFrame, justify="center")
cuadroDNI.grid(row=1,column=1,padx=1, pady=10)

cuadroPASS = Entry(miFrame, justify="center")
cuadroPASS.grid(row=2, column=1, padx=1, pady=10)
cuadroPASS.config(show="*")

#******************************************************************************

cuadrotexto=Text(miFrame, bg="blue", fg= "black", width= "40", height="10")
cuadrotexto.grid(row=3, column=1, padx=1, pady=10,sticky="n")

scroll = Scrollbar(miFrame, command=cuadrotexto.yview)
scroll.grid(row=3,column =2, sticky= "nsew")
cuadrotexto.config(yscrollcommand=scroll.set)

def codigoboton():
    minombre.set("Edgardo")

boton = Button(miFrame, text="ENVIAR", command= codigoboton)
boton.grid(row=4,column =1, sticky="n")

raiz.mainloop()
