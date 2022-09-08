import random

nombres = ['juan', 'jose', 'pedro','paco', 'diego', 'danilo', 'damian', 'matias', 'laura', 'maria', 'ester', 'romina', 'lucia', 'graciela']

apellidos = ['lopez', 'perez', 'juarez', 'rodriguez', 'affani', 'groetzner', 'aguirre', 'chaves', 'cometto', 'ricciutti', 'ibarlucea', 'bilardo', 'cuffia', 'recalde']


nombre = nombres[random.randint(0, len(nombres))]
apellido = apellidos[random.randint(0, len(apellidos))]

print(nombre)
print(apellido)

mails = ['gmail', 'hotmail', 'yahoo', 'outlook']
mail = nombre + '@' + random.choice(mails) + '.com'

print(mail)
