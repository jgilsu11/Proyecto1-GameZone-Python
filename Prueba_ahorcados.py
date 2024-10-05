#Prueba ahorcados.py
import random



def obtener_palabra_aleatoria():
    palabras_ahorcado = [
    "gato", "perro", "casa", "sol", "luna", "arbol", "flor", "mar", "rio", "pez",
    "nube", "cielo", "mesa", "silla", "libro", "lapiz", "papel", "coche", "tren", "avion",
    "barco", "playa", "camion", "bosque", "campo", "ciudad", "calle", "puente", "parque", "jardin",
    "escuela", "maestro", "alumno", "amigo", "familia", "comida", "fruta", "verdura", "musica", "cancion","puerta"
]
    palabra_aleatoria= random.choice(palabras_ahorcado) #.self habría que añadir creo cuando haga clases
    return palabra_aleatoria


def mostrar_tablero(palabra_secreta, letras_guessed):
    for letra in palabra_secreta:
        tablero= ""
        if letra in letras_guessed:
            tablero+= letra
        else:
            tablero+= " _ "

    print(tablero)

def jugar_ahorcado():
    palabra_oculta= obtener_palabra_aleatoria()
    letras_adivinadas= []
    intentos_restantes= 6 
    while intentos_restantes > 0:
        mostrar_tablero(palabra_oculta, letras_adivinadas)
        letra_usuario= str(input("Escribe tu siguiente letra: ")).lower().strip()
        if letra_usuario in letras_adivinadas:
            print("Esta letra ya la has usado, prueba con otra")
            continue
        elif letra_usuario in palabra_oculta: #palabra oculta ya es un string y con el in ya sirve no hace falta split 
            letras_adivinadas.append(letra_usuario)
            if set(letras_adivinadas) == set(palabra_oculta):  #Utilizamos set porque así se eliminan duplicados
                print("¡¡Felicidades has adivinado la palabra!!")
                break
        else:
            intentos_restantes -= 1
            print(f"Lo siento, esa letra no está en la palabra, prueba otra vez que te quedan {intentos_restantes} intentos")
    if intentos_restantes == 0:
        print(f"Lo lamento no has conseguido adivinar la palabra. La palabra era {palabra_oculta}")

jugar_ahorcado()