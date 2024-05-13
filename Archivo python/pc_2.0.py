nota= int(input("ingrese la nota del examen: "))
if nota<0 or nota> 100:
 print("La nota no es valida")
 
else:

 if nota>65:
   print("Apobro el curso con la nota de: ", nota)
 
 else: 
  print("Reprobo el curso con la nota de: ", nota)