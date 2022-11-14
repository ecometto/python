import pandas as pd

lista = [
    {"id": 1,
     "cod": "101",
            "description": "pantalon",
            "price": 10000.0
     },
    {
        "id": 2,
        "cod": "102",
        "description": "camisa lisa",
        "price": 4000.0
    },
    {
        "id": 3,
        "cod": "103",
        "description": "camisa rayada",
        "price": 4150.0
    },
    {
        "id": 4,
        "cod": "104",
        "description": "remera Manga corta blanca",
        "price": 3550.99
    },
    {
        "id": 5,
        "cod": "105",
        "description": "remera Manga larga",
        "price": 3850.99
    },
    {
        "id": 6,
        "cod": "106",
        "description": "medias cortas",
        "price": 999.0
    },
    {
        "id": 7,
        "cod": "107",
        "description": "medias largas de algodon",
        "price": 1200.0
    },
    {
        "id": 8,
        "cod": "cod2",
        "description": "gorro de lana negro",
        "price": 850.0
    },
    {
        "id": 9,
        "cod": "cod01",
        "description": "pijamas para hombres",
        "price": 5000.0
    },
    {
        "id": 10,
        "cod": "codxx",
        "description": "gorra de algodon",
        "price": 300.0
    },
    {
        "id": 10,
        "cod": "cdzap",
        "description": "zapato de cuero",
        "price": 11000.0
    },
    {
        "id": 12,
        "cod": "bla",
        "description": "remera de algodon blanca y negra",
        "price": 1800.0
    },
    {
        "id": 12,
        "cod": "cdsa",
        "description": "otro mas",
        "price": 1420.0
    },
    {
        "id": 14,
        "cod": "mouse001",
        "description": "mouse inalambrico genius g22",
        "price": 200.0
    }
]

personas = pd.DataFrame(lista)

print(personas)
#imprime datos generales del dataFrame
# print(personas.info())

# print("cantidad de datos", personas.size)
# print("los primeros 2 registros son", personas.head(2))
# print("-----------------------------------\n")
# print("los ultimos 2 registros son", personas.tail(2))


#imprime los datos de una columna en particular
# print(personas['price'])

#imprime una localización específica (a traves indices o a traves de nombre columna).
print(personas.iloc[ 2 , 1 ])
print(personas.loc[4 , 'cod' ] )

#devuelve nuevo dataframe de los datos de una fila
# print(personas.iloc[2])



