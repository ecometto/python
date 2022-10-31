
def sayHello():
    name = input ("escriba sunombre")
    age = input ("escriba su edad")
    hello(name, age)
    # print(f"Hola, como estás {name}? Tienes {age} años. Bienvenido al curso de python")
    
def hello(name, age):
    # print("hello")
    print(f"Hola, como estás {name}? Tienes {age} años. Bienvenido al curso de python")
    
persona = {
    "1": 22,
    "2": "Edy",
    "3": "arg",
}

numero = input ("ingrese un numero a traducir")

print(persona[numero])