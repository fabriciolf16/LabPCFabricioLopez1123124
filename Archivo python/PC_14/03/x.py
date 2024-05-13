
pers=int(input("Ingrese cuantas personas colocarán su edad: "))

for i in range (1,pers+1):
    edad=int(input("Ingrese un número: "))
    
    if edad<0 or edad>120:
        print("Edad no válida")
    else:
        if edad>=17: 
            print("La persona es tiene mas de 17")
        else:
            print("La perona es menor de edad")