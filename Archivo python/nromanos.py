cardinal=int(input("numero cardInal: "))
 
if 1<=cardinal<=999:
    centenas= cardinal//100
    decenas=cardinal%100//10
    unidades=cardinal%100%10
   
else: 
    print("numero no valido")

match centenas: 
    case 1: romano = "C"
    case 2: romano = "CC"
    case 3: romano = "CCC"
    case 4: romano = "CD"
    case 5: romano = "D"
    case 6: romano = "DC"
    case 7: romano = "DCC"
    case 8: romano ="DCCC"
    case 9: romano = "CM"
    case _: romano = ""

match decenas: 
    case 1: romano += "X"
    case 2: romano += "XX"
    case 3: romano += "XXX"
    case 4: romano += "XL"
    case 5: romano += "L"
    case 6: romano += "LX"
    case 7: romano += "LXX"
    case 8: romano +="LXXX"
    case 9: romano += "XC"
    case _: romano = ""

match unidades: 
    case 1: romano += "I"
    case 2: romano += "II"
    case 3: romano += "III"
    case 4: romano += "IV"
    case 5: romano += "V"
    case 6: romano += "VI"
    case 7: romano += "VII"
    case 8: romano +="VIII"
    case 9: romano += "IV"
    case _: romano = ""

print("el numero romano es  "+ romano)

