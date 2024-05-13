valor= int(input("ingrese un numero: "))
contador=0
if (valor<=0): 
    print("error no valido")

else: 
    for i in range (1, valor+1):
        if(valor%i==0):
            contador=contador+1
    if contador==2 or contador==1:
        print("el numero es primo")
    else: 
        print("el numero no es primo")
        