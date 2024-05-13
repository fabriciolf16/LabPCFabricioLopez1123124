print("semana  No.10: Ejercicio 1")

mesentrada=int(input("ingrese un numero del 1-12: "))
messalida=  " "

match mesentrada: 
    case 1: 
        mesalida= "Enero"
    case 2: 
        mesalida= "Febrero"
    case 3: 
        mesalida= "Marzo"
    case 4: 
        mesalida= "Abril"
    case 5: 
        mesalida= "Mayo"
    case 6: 
        mesalida= "Junio"
    case 7: 
        mesalida= "Julio"
    case 8: 
        mesalida= "Agosto"
    case 9: 
        mesalida= "Septiembre"
    case 10: 
        mesalida= "Octubre"
    case 11:
        mesalida= "Noviembre"
    case 12: 
        mesalida= "Diciembre"

print(f"Mes: {mesalida}")
         

#Actividad2

print("Semana No.10: Ejercicio 2")

a=int(input("ingrese un primer numero mayor a 0: "))
b=int(input("ingrese un segundo numero mayor a 0: "))
c=int(input("ingrese un tercer numero mayor a 0: "))

if(a<=0 or b<=0 or c<=0):
    print("Error")

if(a>b):
    if(a>c):
        print("A es el mayor")
    else: 
        if(a == c):
            print("A es mayor a B,A es igual a C ")
        else: 
            print("A es mayor a B y menor que C")
elif (a==b):
    if(a>c): 
        print("A es igual que B y mayor que C")