numero=int(input("ingrese el numero: "))
if (numero<=0): 
    print("error en el numero")
else: 
    suma=0
    for i in range(1, numero): 
        if numero % i==0:
         suma += i
    if suma == numero:
       print("el numero es perfecto")
    else: 
       print("el numero no es perfecto")