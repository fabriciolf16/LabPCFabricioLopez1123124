numA=int(input("Ingrese un primer numero: "))
numB= int(input("Ingrese un segundo numero: "))

if (numA and numB <=0):
    print("numero invalido")
else: 
    suma=0
    suma1=0
    for i in range(1,numA):
        if numA % i==0:
         suma+= i
    for i in range(1,numB):
        if numB % i==0:
            suma1+=i

    if(suma==numA and suma1==numB):
        print("el numero es amigo")
    

    