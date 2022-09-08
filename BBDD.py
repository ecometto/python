import _sqlite3



'''
miconexion = _sqlite3.connect("DB1_ART.db")
micursor = miconexion.cursor()

# CRUD: CREATE, READ, UPDATE, DELETE (COMANDOS: INSERT INTO, SELECT, UPDATE, DELETE)
#CREATE - SE CREA LA TABLA (LUEGO HAY QUE COMENTARLA XQ DARA ERROR). TAMBIEN SE PUEDE "MANEJAR" EL ERROR

micursor.execute( CREATE TABLE ARTICULOS 
                 ('ID' INTEGER PRIMARY KEY AUTOINCREMENT,
                 'RUBRO' VARCHAR (50),
                 'SUBRUBRO' VARCHAR (50),
                 'DESCRIPCION' VARCHAR (200),
                 'MARCA' VARCHAR (50),
                 'UNIDAD_MEDIDA' VARCHAR (50),
                 'STOCK_ALERTA' INTEGER,
                 'PROVEEDOR_HABITUAL' VARCHAR (50),
                 'DETALLE_UBICACION' VARCHAR (50)))
'''

'''
# CARGAR DATOS EN LA TABLA (2 FORMAS)
# INDIVIDUALMENTE
micursor.execute("INSERT INTO STUDENTS values(1,'PEDRO','SISTEMAS',2)")
# VARIOS A LA VEZ CON UNA LISTA/TUPLA
milista = [
    ("MICAELA","SISTEMAS"),
    ("ESTEBAN","SISTEMAS"),
    ("ALEJANDRO","ELECTRICA")
]
micursor.executemany("insert into ESTUDIANTES values(NULL,?,?)", milista)
miconexion.commit()'''

'''


# READ
micursor.execute("select * from ESTUDIANTES where CARRERA = 'SISTEMAS'") #TAMBIEN SE PUEDE TRAER "TODA" LA BASE Y SE FILTRA DESPUES
datos = micursor.fetchall()
for i in datos:
    print(i)

# UPDATE (SIEMPRE AL CARGAR, MODIFICAR O ELIMINAR DATOS SE DEBE "ACTUALIZAR" CON COMMIT
micursor.execute("update ESTUDIANTES SET NOMBRE = 'MARIANA' where ID = 1")

micursor.execute("delete from ESTUDIANTES where ID = 4")

miconexion.commit()


micursor.execute("select * from ESTUDIANTES")
datos = micursor.fetchall()
print(datos)

'''
miconexion.close()


