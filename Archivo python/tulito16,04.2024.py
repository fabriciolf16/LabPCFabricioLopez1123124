n=int(input("Cuantos datos quieres ingresar: "))
lista=[]
cantidad=0

while cantidad<n:
    valor = int(input("ingrese un numero"))
    if(valor>0):
       lista.append(valor)
       cantidad = cantidad+1
    else: 
       print("Numero no es validom intentelo de nuevo")

mayor=0
for i in lista:
   if (i>mayor):
      mayor = i
      print("el numero mayor es" + str(mayor))






    