
import random




class Ahorcados:
    def __init__(self):
        self.palabra_oculta = self.obtener_palabra_aleatoria()
        self.letras_adivinadas = []
        self.intentos_restantes = 6
        self.letras_usadas = []

    def obtener_palabra_aleatoria(self):
        palabras_ahorcado = [
            "gato", "perro", "casa", "sol", "luna", "arbol", "flor", "mar", "rio", "pez",
            "nube", "cielo", "mesa", "silla", "libro", "lapiz", "papel", "coche", "tren", "avion",
            "barco", "playa", "camion", "bosque", "campo", "ciudad", "calle", "puente", "parque", "jardin",
            "escuela", "maestro", "alumno", "amigo", "familia", "comida", "fruta", "verdura", "musica", "cancion", "puerta"
        ]
        return random.choice(palabras_ahorcado)

    def mostrar_tablero(self):
        tablero = ""
        for letra in self.palabra_oculta:
            if letra in self.letras_adivinadas:
                tablero += letra
            else:
                tablero += "_ "
        print(tablero)

    def dibujar_ahorcado(self):
        partes = [
            "  O  ",  
            "  |  ",  
            " / \ ",     
            "  | ",   
            " / \ ",     
            "/   \ "    
        ]
        dibujo = [" "] * 6   
        for i in range(6 - self.intentos_restantes): 
            dibujo[i] = partes[i]
        print("\n".join(dibujo))

    def jugar(self):
        while self.intentos_restantes > 0:
            self.mostrar_tablero()
            print(f"Letras usadas: {', '.join(self.letras_usadas)}") 
            letra_usuario = input("Escribe tu siguiente letra: ").lower().strip()
            
            if letra_usuario in self.letras_usadas:
                print("Esta letra ya la has usado, prueba con otra")
                continue
            self.letras_usadas.append(letra_usuario)            
            if letra_usuario in self.palabra_oculta:  
                self.letras_adivinadas.append(letra_usuario)
                if set(self.letras_adivinadas) == set(self.palabra_oculta):  
                    print("¡¡Felicidades has adivinado la palabra!!")
                    break
            else:
                self.intentos_restantes -= 1
                self.dibujar_ahorcado()
                if self.intentos_restantes > 0:
                    print(f"Lo siento, esa letra no está en la palabra, prueba otra vez que te quedan {self.intentos_restantes} intentos")
        if self.intentos_restantes == 0:
            print(f"Lo lamento no has conseguido adivinar la palabra. La palabra era {self.palabra_oculta}. Me temo que la ganadora ha sido ¡¡MAQUINA!!")
        self.opciones_post()

    def opciones_post(self):
        while True:
            print("\n¿Qué te gustaría hacer ahora?")
            print("1. Volver a jugar")
            print("2. Volver al menú de juegos")
            print("3. Salir")
            opcion = input("Elige una opción (1, 2, 3): ").strip()  

            if opcion == "1":
                self.__init__()
                self.jugar()
                break
            elif opcion == "2":
                print("Volviendo al menú de juegos... (aún por implementar)")
                break
            elif opcion == "3":
                print("¡Gracias por jugar! Hasta la próxima.")
                exit()
            else:
                print("Opción no válida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":     
    juego = Ahorcados()
    juego.jugar()
