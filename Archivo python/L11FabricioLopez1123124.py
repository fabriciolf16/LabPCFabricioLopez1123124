print("semana No. 11, Eejercicio 1")

n= int(input("ingrese un numero mayor a 0"))
if(n<=0):
    print("numero no valido")

#definicion de variables
    a=0
    b=1
    c=0
    i=2
    resultado=""
if(n>0):
    resultado= str(a)
    if(n>1):

        resultado += " , " + str(b)

    while(i<n):
        c= a + b 
        resultado += " , " + str(c)

        a=b
        b=c
        i= i+1

        print(resultado)

else:
    print(resultado)


print("Semana No11, ejercicio 1")

n2= int(input("ingrese un numero mayor a 0"))

if(n2<=0):
    print("error en el numero")


#inciso A
    resultadoA=0
    for x in range(1, n2 +1):
        resultadoA= 1/x

        print("inciso A:", resultadoA)