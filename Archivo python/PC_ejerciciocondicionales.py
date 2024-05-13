
compra=int(input("Ingrese el valor de la compra: "))

if compra<0:
     print("error monto no valido")

if compra<400: 
    print("no hay descuento")
else:
    if compra>=401 and compra<=1000:
        descuento1=compra*93/100
        print("el total con el descuento aplicado es de: ", descuento1)
    else:
        if compra>=1001 and compra<=5000:
            descuento2=compra*90/100
            print("el total con el descuento aplicado es de: ", descuento2)
        else:
            if compra>=5001 and compra<=15000:
                descuento3=compra*85/100
                print("el total con el descuento aplicado es de: ", descuento3)
            else:    
                if compra>15000:
                        descuento4= compra*75/100
                        print("el total con el descuento aplicado es de: ", descuento4)

res= input("tiene un codifo de descuento (s/n) ")
if(res=="si") or res=="sí" or res == "s":
 
    if 0.05:
        valor1=descuento1*0.05
    print("el total de su compra con el descuento y su cupon es de: ", valor1)
valor2=descuento2*0.05
print("el total de su compra con el descuento y su cupon es de: ", valor2)
valor3=descuento3*0.05
print("el total de su compra con el descuento y su cupon es de: ", valor3)
valor4=descuento4*0.05
print("el total de su compra con el descuento y su cupon es de: ", valor4)





print("EJERCICIO 2")

print("¿Como desea su envio, motocicleta o carro? ")

motocicleta=1
carro =2

distancia1=int(input("ingrese la cantidad de kilometros"))

cobrofijo=int(20)
if 2: 
            if distancia1>=0 and distancia1<=5:
                envio= cobrofijo*2*distancia1
                print("el total de su envio es de:", envio)
elif distancia1>=5 and distancia1<=10:
    envio2= cobrofijo*5*distancia1
    print("el total de su envio es de:", envio2)
elif distancia1>10:
    envio3=cobrofijo*4*distancia1
    print("el total de su envio es de:", envio3)    

