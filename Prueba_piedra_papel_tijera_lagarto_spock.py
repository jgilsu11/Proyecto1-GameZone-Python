

import random
import os

class Piedra_papel_tijera:
    def __init__(self):
        self.victorias_jugador = 0
        self.victorias_maquina = 0
        self.rondas_para_ganar = 3

    def limpiar_terminal(self):
        """Limpia la terminal
        """
        os.system('cls' if os.name == 'nt' else 'clear')

    def obtener_opciones_y_resultados(self, modo):
        """Función que simplemente define las opciones y resultados posibles
        """
        if modo == "clasico":
            opciones = ["piedra", "papel", "tijera"]
            resultados = {
                "piedra": ["tijera"],
                "papel": ["piedra"],
                "tijera": ["papel"]
            }
        else:
            opciones = ["piedra", "papel", "tijera", "lagarto", "spock"]
            resultados = {
                "piedra": ["tijera", "lagarto"],
                "papel": ["piedra", "spock"],
                "tijera": ["papel", "lagarto"],
                "lagarto": ["spock", "papel"],
                "spock": ["tijera", "piedra"]
            }
        return opciones, resultados

    def obtener_opcion_jugador(self, opciones):
        """Muestra las opciones a elegir al usuario y comprueba que su respuesta sea válida
        """
        while True:
            print("\nElige una opción:")
            for i, opcion in enumerate(opciones, 1):
                print(f"{i}. {opcion.capitalize()}")
            eleccion = input("Tu elección: ").strip()
            if eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
                return opciones[int(eleccion) - 1]
            else:
                print("Opción no válida. Intenta de nuevo.")

    def obtener_opcion_maquina(self, opciones):
        """Elección aleatoria de la máquina entre las opciones
        """
        return random.choice(opciones)

    def determinar_ganador(self, jugador, maquina, resultados):
        """Comprueba si se llega a un empate o determina quien gana
        """
        if jugador == maquina:
            return "empate"
        elif maquina in resultados[jugador]:
            return "jugador"
        else:
            return "maquina"

    def jugar_ronda(self, opciones, resultados):
        """Esta función lleva la lógica del juego con la correspondiente distribución de puntos, es decir, lo que sucede cada ronda
        """
        jugador = self.obtener_opcion_jugador(opciones)
        maquina = self.obtener_opcion_maquina(opciones)
        print(f"\nTú elegiste: {jugador.capitalize()}")
        print(f"La máquina eligió: {maquina.capitalize()}")

        ganador = self.determinar_ganador(jugador, maquina, resultados)
        if ganador == "jugador":
            print("¡Ganaste esta ronda!")
            self.victorias_jugador += 1
        elif ganador == "maquina":
            print("La máquina ganó esta ronda.")
            self.victorias_maquina += 1
        else:
            print("Esta ronda es un empate.")

        print(f"\nVictorias - Jugador: {self.victorias_jugador}, Máquina: {self.victorias_maquina}")

    def opciones_despues_del_juego(self):
        """Opciones que se muestran al usuario al terminar la partida donde se le permite
           volver a jugar, cambiar de modalidad (menú principal), ir al menú de otros juegos o salir
        """
        while True:
            print("\n¿Qué te gustaría hacer ahora?")
            print("1. Volver a jugar")
            print("2. Ir al menú principal")
            print("3. Ir al menú de juegos")
            print("4. Terminar")
            opcion = input("Elige una opción (1, 2, 3 o 4): ").strip()

            if opcion == "1":
                return "reiniciar"
            elif opcion == "2":
                print("Cargando menú principal ...")
                return "menu_principal"
            elif opcion == "3":
                print("Cargando menú de juegos ... (Próximamente disponible)")
                exit()
            elif opcion == "4":
                print("¡Gracias por jugar! Hasta la próxima.")
                exit()
            else:
                print("Opción no válida. Por favor, elige 1, 2, 3 o 4.")

    def jugar(self, modo):
        """Es la función donde se ordenan el resto de funciones con todo lo necesario para que se ejecute el juego
        """
        self.limpiar_terminal()
        opciones, resultados = self.obtener_opciones_y_resultados(modo)
        self.victorias_jugador = 0
        self.victorias_maquina = 0

        print(f"¡Bienvenido a Piedra, Papel, Tijera{' , Lagarto, Spock' if modo == 'extendido' else ''}!")
        while self.victorias_jugador < self.rondas_para_ganar and self.victorias_maquina < self.rondas_para_ganar:
            self.jugar_ronda(opciones, resultados)

        if self.victorias_jugador == self.rondas_para_ganar:
            print("\n¡Felicidades! Has ganado el juego.")
        else:
            print("\nLa máquina ha ganado el juego. Mejor suerte la próxima vez.")

        return self.opciones_despues_del_juego()

    def main_menu(self):
        """Muestra las opciones de modalidad de juego (clásica o extendida) y la opción de terminar
        """
        while True:
            print("Menú Principal")
            print("1. Jugar Piedra, Papel, Tijera, Lagarto, Spock")
            print("2. Jugar Piedra, Papel, Tijera clásico")
            print("3. Salir")
            choice = input("Selecciona una opción: ")
            if choice == '1':
                resultado = self.jugar(modo="extendido")
                if resultado == "reiniciar":
                    self.jugar(modo="extendido")
            elif choice == '2':
                resultado = self.jugar(modo="clasico")
                if resultado == "reiniciar":
                    self.jugar(modo="clasico")
            elif choice == '3':
                print("¡Gracias por jugar!")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    juego = Piedra_papel_tijera()
    juego.main_menu()
