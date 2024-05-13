num = int(input("ingrese un numero admirado: "))
factorial=0
if(num<=0):
    print("numero incorrecto")
else:
    for n in range(1, num+1):
        if n==1:
            factorial=1
        else: 
            factorial*=n

    print("la respuesta es: " + str(factorial))