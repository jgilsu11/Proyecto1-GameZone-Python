
import random



def obtener_palabra_aleatoria():
    palabras_ahorcado = [
     "gato", "perro", "casa", "sol", "luna", "arbol", "flor", "mar", "rio", "pez",
     "nube", "cielo", "mesa", "silla", "libro", "lapiz", "papel", "coche", "tren", "avion",
     "barco", "playa", "camion", "bosque", "campo", "ciudad", "calle", "puente", "parque", "jardin",
     "escuela", "maestro", "alumno", "amigo", "familia", "comida", "fruta", "verdura", "musica", "cancion","puerta"
    ]
    palabra_aleatoria= random.choice(palabras_ahorcado) 
    return palabra_aleatoria


def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero= ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra
        else:
            tablero += "_ " 

    print(tablero)
def dibujar_ahorcado(intentos_restantes):
    partes = [
        "  O  ",  
        "  |  ",  
        " / \ ",     
        "  | ",   
        " / \ ",     
        "/   \ "    
    ]
    dibujo = [" "] * 6   
    for i in range(6 - intentos_restantes): 
        dibujo[i] = partes[i]
    print("\n".join(dibujo)) 

def jugar_ahorcado():
    palabra_oculta= obtener_palabra_aleatoria()
    letras_adivinadas= []
    intentos_restantes= 6 
    letras_usadas= []  
    while intentos_restantes > 0:
        mostrar_tablero(palabra_oculta, letras_adivinadas)
        print(f"Letras usadas: {', '.join(letras_usadas)}") 
        letra_usuario= input("Escribe tu siguiente letra: ").lower().strip()
         
        if letra_usuario in letras_usadas:
            print("Esta letra ya la has usado, prueba con otra")
            continue
        letras_usadas.append(letra_usuario)            
        if letra_usuario in palabra_oculta:  
            letras_adivinadas.append(letra_usuario)
            if set(letras_adivinadas) == set(palabra_oculta):  
                print("¡¡Felicidades has adivinado la palabra!!")
                break
        else:
            intentos_restantes -= 1
            dibujar_ahorcado(intentos_restantes)
            if intentos_restantes > 0:
                print(f"Lo siento, esa letra no está en la palabra, prueba otra vez que te quedan {intentos_restantes} intentos")
    if intentos_restantes == 0:
        print(f"Lo lamento no has conseguido adivinar la palabra. La palabra era {palabra_oculta}. Me temo que la ganadora ha sido ¡¡MAQUINA!!")
    while True:
        print("\n¿Qué te gustaría hacer ahora?")
        print("1. Volver a jugar")
        print("2. Volver al menú principal")
        print("3. Salir")
        opcion = input("Elige una opción (1, 2, 3): ").strip()  


        if opcion == "1":
            jugar_ahorcado()
            break
        elif opcion == "2":
            print("Volviendo al menú principal... (aún por implementar)")
            break
        elif opcion == "3":
            print("¡Gracias por jugar! Hasta la próxima.")
            exit()
        else:
            print("Opción no válida. Por favor, elige 1, 2 o 3.")
jugar_ahorcado()