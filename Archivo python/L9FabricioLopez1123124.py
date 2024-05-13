print("Ejercicio 1: operaciones aritmeticas")

numero1 = int(input("ingrese un primer numero: "))
numero2 = int(input("ingrese un segundo numero: "))

divisionReal = numero1 / numero2
divisionEntera = numero1 // numero2
mod= numero1 % numero2

print(numero1, "/", numero2, "=", divisionReal)
print(numero1, "//", numero2, "=", divisionEntera )
print(numero1, "%", numero2, "=", mod)

print("ejercicio 2: operaciones booleanas")

igualdad = numero1 == numero2
diferente = numero1 != numero2

print(numero1, "==", numero2, "=", igualdad)
print(numero1, "!=", numero2, "=", diferente)

print("actividad 3")

metros1= int(input("ingrese metros: "))
km = metros1/ 1000 
print(f"km = {km}")

numero3= int(input("ingrese numero de metros: "))

yardas1 = numero3 // 0.9144
yardas2 = numero3 % 0.9144

feet1= yardas2//0.333333
feet2= yardas2 % 0.33333

inches1= feet2//0.083333


print(f"numero de yardas es:{yardas1} " f"numero de pies es: {feet1} " f"numero de inches es : {inches1}")