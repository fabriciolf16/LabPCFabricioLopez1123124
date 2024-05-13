try:
    numero = int(input("ingrese un número: "))

    if numero%2==0:
        print("El numero es par")
    else: 
        print("El numero es impar")
except ValueError: 
    print("Por favor ingrese un valor válido")