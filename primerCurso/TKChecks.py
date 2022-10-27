from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("practica de checks")
root.geometry("600x600")

#-------------funciones de MENU ------------------
def infoLicencia():
    messagebox.showinfo("Informacion de Licencia", "Esta licencia gratuita caducara en 2022")

def cerrarArchivo():
    valor = messagebox.askyesno("pulsado Archivo-Cerrar", "Esta seguro que desea cerrar?")
    if valor == True:
        root.destroy()
    else:
        messagebox.showinfo("titulo 2", "bienvenido nuevamente")

def abre_archivos():
    filedialog.askopenfilename(title="abrir archivos", initialdir="C:", filetypes=(("ArchivosExcel","*.xls"),("todos los archivos", "*.*")))
    


#-----------BARRA DE MENU-------------
barra_menu = Menu(root)
root.config(menu=barra_menu, bg="#4F3F3C")

menuArchivo = Menu(barra_menu, tearoff=0) #aca se define el nombre "interno". Tearoff son unas lineas que aparecen (asi se borran)

menuArchivo.add_command(label="Open")
menuArchivo.add_separator() # separa "grupos de elementos"
menuArchivo.add_command(label="New")
menuArchivo.add_command(label="Cerrar", command=cerrarArchivo)

menuEdicion = Menu(barra_menu, tearoff=0)
menuEdicion.add_command(label="Copiar")
menuEdicion.add_command(label="Pegar")

menuAyuda = Menu(barra_menu, tearoff=0)
menuAyuda.add_command(label="acerca de..")
menuAyuda.add_command(label="licencia", command=infoLicencia)


barra_menu.add_cascade(label="Archivo", menu=menuArchivo) # aca se define el nombre que se mostrara...
barra_menu.add_cascade(label="Edicion",menu=menuEdicion)
barra_menu.add_cascade(label="Ayuda", menu=menuAyuda)


#-----------TITULO-------------------
titulo = Label(root, text="FORMULARIO DE CONSULTA", width=50, bg="black", fg="white", font=24)
titulo.pack()

#--------VARIABLES------------
seleccion = IntVar()
viajes = IntVar()
deportes=IntVar()
shopping=IntVar()


#----------FUNCIONES ----------------
def ImprimirSeleccion():
    if seleccion.get() ==1:
        etiquetaSexo.config(text="Ud ha seleccionado: \n  Masculino")
    elif seleccion.get() == 2:
        etiquetaSexo.config(text="Ud ha seleccionado: \n  Femenino")
    elif seleccion.get() == 3:
        etiquetaSexo.config(text="Ud ha seleccionado: \n  Otras Opciones")
    elif seleccion.get() == 4:
        etiquetaSexo.config(text="Ud ha seleccionado: \n NUEVAS")

def hobbies():
    textohobbie = "Ud ha elegido: "
    if viajes.get() == 1:
        textohobbie += " Viajes"
    if deportes.get() == 1:
        textohobbie += " Deportes"
    if shopping.get() == 1:
        textohobbie += " Shopping"

    etiquetaHobbies.config(text= textohobbie)

#-----------SUBTITULO 1-------------------
frame = Frame(root, bg="white")
frame.pack()

Label(frame, text="INGRESE SU SEXO", width=30, fg="black", font = 18).pack()

Radiobutton(frame, text="masculino", width=20, padx=10, pady=10,  variable=seleccion, value=1, command= ImprimirSeleccion).pack()
Radiobutton(frame, text=" femenino ", width = 20, padx=10, pady=10, variable=seleccion, value=2, command= ImprimirSeleccion).pack()
Radiobutton(frame, text= " Otras Opciones ", width = 20, padx=10, pady=10, variable=seleccion, value=3, command=ImprimirSeleccion).pack()
Radiobutton(frame, text=" nuevas... ", width = 20, padx=10, pady=10, variable=seleccion, value=4, command= ImprimirSeleccion).pack()

etiquetaSexo= Label(root, width = 24, padx=5, pady=20, bg="blue", text="Resultado de la seleccion:")
etiquetaSexo.pack()

#------------------------------------------------------------------------------
Label(root, text="", width=30, bg="#4F3F3C", fg="black", font = 18).pack()
#------------------------------------------------------------------------------

foto = PhotoImage(file="imagenpng.png")
Label(root, image=foto, width=60, height=60).pack()

#-----------SUBTITULO 2-------------------
frame2 = Frame(root, bg="white")
frame2.pack()
Label(frame2, text="INGRESE SU HOBBIE?", width=30, font = 18).pack()

Checkbutton(frame2, text="Viajes", width=20, padx=10, pady=10, variable = viajes, onvalue=1, offvalue=0,  command=hobbies).pack()
Checkbutton(frame2, text="deportes", width=20, padx=10, pady=10,variable = deportes, onvalue=1, offvalue=0,  command=hobbies).pack()
Checkbutton(frame2, text="shopping", width=20, padx=10, pady=10,variable = shopping, onvalue=1, offvalue=0,  command=hobbies).pack()

etiquetaHobbies=Label(frame2)
etiquetaHobbies.pack()

Button(root, text="Abrir Archivos", command= abre_archivos ).pack()


root.mainloop()