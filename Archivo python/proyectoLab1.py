import turtle

#Ejemplo de teleport para mover la torguga
turtle.teleport(-100,100)

#Ejemplo de dibujar un cuadrado utilizando el ciclo for
for x in range(0, 4):
    turtle.forward(50)
    turtle.left(90)

#Escribir un texto en la ventana del cuento
turtle.write("Prueba.... asdfas", False)

#REGRESAR A CONSOLA 
#imprimir y responder pregunta del cuento
respuesta = int(input("cual era el nombre del conejo \n 1. Juan \n 2. pepito"))
print(respuesta)

#Validar respuesta correcta...
 
#si es correcta,  limpiar pantalla y dibujar la siguiente escena. En caso contrario repetir pregunta hasta que sea correcta
turtle.clearscreen()

#ejemplo estrella
grados = 0
turtle.speed(15)
for x in range(1, 40):
    for x in range(0, 4):
        turtle.forward(50)
        turtle.left(90)
    turtle.left(grados + 10)

#finalizar
turtle.done()