from tkinter import *
from sqlite3 import *
import sqlite3

# DEFINICION DE FUNCIONES Y VARIABLES
color = "#F9E79F"

def login():  # Funcion login ... Nos permitira comprobar 'usuario' y 'contraseña' con la base de datos
    usuario = caja1.get()  # Obtenemos el valor de la 'caja1' (usuario)
    contr = caja2.get()  # Obtenemos el valor de la 'caja2' (contraseña)
    c.execute('SELECT * FROM usuarios WHERE Usuario = ? AND Pass = ?',
              (usuario, contr))  # Seleccionamos datos '(usuario,contr)'
    if c.fetchall():
        mb.showinfo(title="Login Correcto", message="Usuario y contraseña correctos")  # Mostramos 'Login Correcto'
    else:
        mb.showerror(title="Login incorrecto",
                     message="Usuario o contraseña incorrecto")  # Mostramos 'Login incorrecto'


# c.close()

# CONFIGURACION DE LA INTERFACE
raiz = Tk()
raiz.title("FORMULARIO INICIO DE SESION")
raiz.geometry("600x600")
raiz.config(bg = "white", bd="10", relief="raised")
raiz.iconbitmap('logo.ico')

miframe = Frame(raiz)
miframe.pack()
miframe.config(width="700", height="50", bg=color)
imagen = PhotoImage(file="imagen1.png")
lbl1 = Label(miframe, image=imagen).pack(pady = '20', padx = '20')

miframe1 = Frame(raiz)
miframe1.pack()
miframe1.config(width="700", height="500", bg='white')

lblUsuario = Label(miframe1, text="Ingrese su Usuario", font=('arial', 15), fg='grey').grid(row="0", column="0", sticky="e" , pady='5')
caja1 = Entry(miframe1, relief='solid').grid(row='0', column='1')
lblclave = Label(miframe1, text="Ingrese su Contraseña", font=('arial', 15), fg='grey').grid(row="1", column="0", sticky="e", pady='5')
caja2 = Entry(miframe1, relief='solid').grid(row='1', column='1')
boton = Button(miframe1, text="Aceptar - Ingresar", command=login).grid(row='2', column='0', sticky="e", pady='5')
boton1 = Button(miframe1, text="No tiene Usuario? Registrarse aqui.", bg='white').grid(row='3', column='0', sticky="e", pady='5')

miframe2 = Frame(raiz)
miframe2.pack()
miframe2.config(width="700", height="100", bg='white')
lblcopy = Label(miframe2, text='All right reserved - CEDdevelopment').place(x=0,y=80)

#CONEXION CON LA BASE DE DATOS (BBDD: login.db) Y TABLA YA CREADA (usuarios: Nombre, Apellido, Usuario, Pass)
db = sqlite3.connect('login.db')  # Nos conectamos a nuestra base de datos 'login.db'
c = db.cursor()  # Establecemos un cursor




mainloop()