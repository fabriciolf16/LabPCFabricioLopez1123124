import random

jugador1 = input("Ingrese nombre: ")
jugador2 = input("Ingrese nombre: ")

secreto = random. randint (1,100)
Ganador= False
Turnos=0
TurnosJug1=0
TurnosJug2=0

while not Ganador: 
    ingresado= int(input("ingrese un numero (1, 100): "))
    Turnos= Turnos+1
    if (Turnos%2==0):
        TurnosJug2=TurnosJug2+1
    else: 
        TurnosJug1=TurnosJug1+1
    if ingresado == secreto: 
        print("Ganaste milobe")
        Ganador = True
        if(Turnos%2==0):
            print("el ganador es ", jugador1)
            print("Tomo"+ str(TurnosJug1)+"turnos")
    else: 
        print("Kellogs, segui intentando")
        if ingresado<secreto:
            print("el numero ingresado es menor")
        else: 
            print("el numero ingresado es mayor")

