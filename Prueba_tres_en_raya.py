class JuegoTresEnRaya:
    def __init__(self):
        self.juego_activo = True

    
    class TresEnRaya:                    
        def __init__(self):
            self.tablero = [[" " for _ in range(3)] for _ in range(3)]  
            self.turno_jugador = True  
            self.juego_activo = True

        def imprimir_tablero(self):
            """Imprime el tablero
            """
            for fila in self.tablero:
                print("|".join(fila))   
                print("-" * 5)

        def verificar_victoria(self, jugador):
            """Verifica si hay algún tres en raya en
               filas, columnas y diagonales
            """
            for i in range(3):
                if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] == jugador:  
                    return True
                if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] == jugador:  
                    return True
            if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] == jugador:      
                return True
            if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] == jugador:      
                return True
            return False

        def tablero_lleno(self):
            """Comprueba si el tablero está lleno y por ende habría empate
            """
            for fila in self.tablero:
                if " " in fila:
                    return False
            return True         

        def turno_jugador_humano(self, jugador):
            """Muestra al jugador que tiene que elegir fila y columna comprobando que la que elija
               esté vacía y que haya metido un número dentro de rango
            """
            while True:         
                try:
                    fila = int(input(f"Jugador {jugador}, elige fila (1-3): ")) - 1   
                    columna = int(input(f"Jugador {jugador}, elige columna (1-3): ")) - 1
                    if self.tablero[fila][columna] == " ":
                        self.tablero[fila][columna] = jugador
                        break
                    else:
                        print("Esa posición ya está ocupada, elige otra.")
                except:
                    print("Por favor, introduce valores válidos entre 1 y 3.")

        def jugar_ronda(self):
            """Todo lo que se tiene que ejecutar en cada ronda
            """
            while self.juego_activo:
                self.imprimir_tablero()
                jugador_actual = "X" if self.turno_jugador else "O"    
                self.turno_jugador_humano(jugador_actual)

                if self.verificar_victoria(jugador_actual):
                    self.imprimir_tablero()
                    ganador = "Jugador 1" if self.turno_jugador else "Jugador 2"   
                    print(f"¡{ganador} ha ganado la partida!")
                    self.juego_activo = False
                    break

                if self.tablero_lleno():
                    self.imprimir_tablero()
                    print("¡Es un empate!")
                    self.juego_activo = False
                    break
                else:
                    self.turno_jugador = not self.turno_jugador  

    def iniciar_tres_en_raya(self):
        while self.juego_activo:
            juego = self.TresEnRaya()
            juego.jugar_ronda()

            while True:
                print("\n¿Qué te gustaría hacer ahora?")
                print("1. Volver a jugar")
                print("2. Volver al menú de otros juegos")
                print("3. Terminar")
                eleccion_final = input("Elige una opción: ")

                if eleccion_final == "1":
                    break                  
                elif eleccion_final == "2":
                    print("Redirigiendo al menú de otros juegos... (próximamente)")
                    
                    self.juego_activo = False
                    exit()
                elif eleccion_final == "3":
                    print("¡Gracias por jugar! Hasta luego.")
                    self.juego_activo = False
                    exit()
                else:
                    print("Opción no válida, elige nuevamente.")

if __name__ == "__main__":
    juego = JuegoTresEnRaya()
    juego.iniciar_tres_en_raya()
