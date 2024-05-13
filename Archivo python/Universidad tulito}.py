x= int(input("Ingrese la edad que desea: "))

lista = []

edades = int(input("Ingrese la cantidad de edades que desea: "))

cantidad = 0 

if x <= 0: 
    print("ERROR, la edad ingresada no es válida")
else:
    for i in range (1, edades+1):
        valor = int(input("Ingrese sus edades : "))
        lista.append(valor)
    sumatoria = 0

    for i in lista:
        if i > x: 
            cantidad += 1 
print("Las edades mayor a su edad deseada son: " + str(cantidad))