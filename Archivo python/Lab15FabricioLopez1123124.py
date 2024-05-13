#Ejercicio1
import math
def cuad(num1):
    Total=num1**2
    return Total
def trian(num1,num2):
    Total=(num1*num2)/2
    return Total
def rect(num1,num2):
    Total=num1*num2
    return Total
def circ(num1):
    Total=num1*math.pi**2
    return Total

op=0
op=int(input("Ingrese un numero para seleccionar sus opciones \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Raiz cuadrada \n 6. Potencia \n 7. Factorial \n 8. Salir"))
match op:
    case 1:
        n1=int(input("Ingrese la ultura de triangulo "))
        n2=int(input("Ingrese la base"))
        print("La resta es: "+str(trian(n1,n2)))
    case 2:
        n1=int(input("Ingrese el lado del cuadrado"))
        print("La resta es: "+str(cuad(n1)))
    case 3:
        n1=int(input("Ingrese el ancho del rectangulo"))
        n2=int(input("Ingrese la altura del rectangulo"))
        print("La resta es: "+str(rect(n1,n2)))
    case 4:
        n1=int(input("Ingrese el radio del circulo"))
        print("La multiplicacion es: "+str(circ(n1)))

#Ejercicio2
X=0
Y=0

def move(cantx,canty):
    global X, Y
    X+=cantx
    Y+=canty

op=""
while op!="a" or op!="b" or op!="c" or op!="d" or op!="e" :
    op=str(input("Ingrese un numero para seleccionar sus opciones \n a. Sube \n b. Baja \n c. Izquierda \n d. Derecha \n e. Salir \n"))
    match op:
        case "a":
            (move(0,1))
        case "b":
            (move(0,-1))
        case "c":
            (move(-1,0))
        case "d":
            (move(1,0))
        case "e":
            break
        case _:
            print("Opcion no valida intente de nuevo")

print("LAs coordenadas del personaje son: ("+str(X)+","+str(Y)+")")