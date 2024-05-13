n=int(input("Cuantos datos quieres ingresar: "))
lista=[]
f=0
mayor=0


for i in range (0,n):
    f=int(input("Dato: "))
    if(i<=0):
        int(input("numero erroneo, ingreselo nuevamente: "))

promedio= (lista/n)
print("el promedio es de" + str(promedio))