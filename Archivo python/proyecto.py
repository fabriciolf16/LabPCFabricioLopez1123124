# Importar la biblioteca turtle
import turtle

# Función para dibujar un árbol con turtle
def dibujar_arbol(tamaño, niveles):
    if niveles == 0:
        return
    turtle.forward(tamaño)
    turtle.left(45)
    dibujar_arbol(0.6 * tamaño, niveles-1)
    turtle.right(90)
    dibujar_arbol(0.6 * tamaño, niveles-1)
    turtle.left(45)
    turtle.backward(tamaño)

# Función para ingresar la información del niño
def ingresar_informacion_niño():
    nombre = input("Ingresa el nombre del niño: ")
    edad = int(input("Ingresa la edad del niño: "))
    print("Elige el color favorito del niño:")
    print("1. Rojo")
    print("2. Azul")
    print("3. Verde")
    print("4. Amarillo")
    print("5. Rosa")
    opcion_color = int(input("Selecciona un número de opción: "))
    colores = ["rojo", "azul", "verde", "amarillo", "rosa"]
    color_favorito = colores[opcion_color - 1]
    return nombre, edad, color_favorito

# Función para mostrar cada secuencia del cuento
def mostrar_secuencia(titulo, narrativa, color_favorito):
    print("----------------------")
    print("Título:", titulo)
    print("Narrativa:")
    print(narrativa)
    print("Panel:")
    dibujar_arbol(100, 5)

# Llamada a la función principal para ejecutar el programa
if __name__ == "__main__":
    # Ingresar información del niño
    nombre, edad, color_favorito = ingresar_informacion_niño()  
    
    # Secuencias del cuento
    secuencias = [
        {
            "titulo": "Ivernia: un pueblo mágico",
            "narrativa": f"En el tranquilo pueblo de Ivernia, donde los pinos se erguían majestuosos como guardianes del valle, y las casitas de colores como galletas se acomodaban junto al lago congelado, vivía {nombre}, un niño de {edad} años cuyo color favorito era el {color_favorito}."
        },
        {
            "titulo": "La aventura de los tres amigos",
            "narrativa": f"{nombre} y sus amigos, Pablo y María, decidieron explorar el misterioso bosque cercano a su casa. Con sus mochilas llenas de provisiones y un mapa dibujado por {nombre}, se adentraron en el bosque, listos para cualquier aventura. Descubrieron un río cristalino donde jugaron durante horas y encontraron un claro lleno de flores de todos los colores."
        },
        # Puedes agregar más secuencias aquí
    ]
    
    # Mostrar las secuencias del cuento
    for secuencia in secuencias:
        mostrar_secuencia(secuencia["titulo"], secuencia["narrativa"], color_favorito)
