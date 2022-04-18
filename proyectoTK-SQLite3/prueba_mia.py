from tkinter import *

# guardando como .pyw se abre directamente
raiz = Tk()
raiz.title("FORMULARIO INICIO DE SESION")
raiz.geometry("800x800")
raiz.resizable(1,1)
raiz.config(bg = "white", bd="10", relief="raised")
raiz.iconbitmap("logo.ico")

miframe1 = Frame()
miframe1.pack()
miframe1.config(width="700", height="50")
imagen = PhotoImage(file="imagen1.png")
lblimagen = Label(miframe1, image=imagen).pack(pady='10')

miframe = Frame()
miframe.pack()
miframe.config(width="700", height="700", bd="2", relief="solid", bg = "gray")

label1 = Label(miframe, text="Numero de Socio", width="20", anchor='e').grid( row="0", column="0", padx='5', pady='5')
entry1 = Entry(miframe, width="50", justify="right").grid(row="0", column="1")
label2 = Label(miframe, text="Disciplina", width="20", anchor='e').grid( row="1", column="0", padx='5', pady='5')
entry2 = Entry(miframe, width="50", justify="right").grid(row="1", column="1")
label3 = Label(miframe, text="Mes de pago", width="20", anchor='e').grid( row="2", column="0", padx='5', pady='5')
entry3 = Entry(miframe, width="50", justify="right").grid(row="2", column="1")
label4 = Label(miframe, text="Importe", width="20", anchor='e').grid( row="3", column="0", padx='5', pady='5')
entry4 = Entry(miframe, width="50", justify="right").grid(row="3", column="1")





mainloop()