

#PREGUNTADOS 




import random


geografia = {
    "pregunta1": ("¿Cuál es la capital de Francia?", "paris", ["londres", "berlin", "madrid"]),
    "pregunta2": ("¿Qué país tiene la mayor cantidad de habitantes?", "china", ["india", "estados unidos", "indonesia"]),
    "pregunta3": ("¿En qué continente se encuentra Egipto?", "africa", ["asia", "europa", "américa"]),
    "pregunta4": ("¿Cuál es el río más largo del mundo?", "nilo", ["amazonas", "yangtze", "mississippi"]),
    "pregunta5": ("¿Cuál es el desierto más grande del mundo?", "sahara", ["gobi", "kalahari", "arabia"]),
    "pregunta6": ("¿Cuál es el país más pequeño del mundo?", "vaticano", ["monaco", "san marino", "liechtenstein"]),
    "pregunta7": ("¿En qué país se encuentra la Torre Eiffel?", "francia", ["italia", "españa", "alemania"])
}

ciencia = {
    "pregunta1": ("¿Qué gas es fundamental para la respiración humana?", "oxigeno", ["hidrogeno", "dioxido de carbono", "nitrógeno"]),
    "pregunta2": ("¿Cuál es la fórmula química del agua?", "h2o", ["co2", "h2so4", "ch4"]),
    "pregunta3": ("¿Qué tipo de animal es una ballena?", "mamifero", ["pez", "reptil", "anfibio"]),
    "pregunta4": ("¿Cuántos planetas tiene el sistema solar?", "8", ["7", "9", "10"]),
    "pregunta5": ("¿Qué planeta es conocido como el planeta rojo?", "marte", ["venus", "jupiter", "saturno"]),
    "pregunta6": ("¿Cuál es el metal más abundante en la corteza terrestre?", "aluminio", ["hierro", "cobre", "plata"]),
    "pregunta7": ("¿Cuál es la unidad de medida de la corriente eléctrica?", "amperio", ["voltio", "ohmio", "watt"])
}

historia = {
    "pregunta1": ("¿En qué año se descubrió América?", "1492", ["1776", "1800", "1607"]),
    "pregunta2": ("¿Quién fue el primer presidente de los Estados Unidos?", "george washington", ["abraham lincoln", "thomas jefferson", "john adams"]),
    "pregunta3": ("¿Cuál fue el conflicto armado que tuvo lugar entre 1939 y 1945?", "segunda guerra mundial", ["primera guerra mundial", "guerra civil americana", "guerra de corea"]),
    "pregunta4": ("¿Qué revolucionario cubano nació en Argentina?", "che guevara", ["fidel castro", "camilo cienfuegos", "raul castro"]),
    "pregunta5": ("¿En qué año cayó el Muro de Berlín?", "1989", ["1990", "1988", "1991"]),
    "pregunta6": ("¿Qué imperio construyó la Gran Muralla China?", "chino", ["romano", "otomano", "persa"]),
    "pregunta7": ("¿Quién fue el emperador de Francia durante el siglo XIX?", "napoleon", ["luis xiv", "carlos magno", "luis xvi"])
}

cultura_general = {
    "pregunta1": ("¿Cuál es el planeta más cercano al Sol?", "mercurio", ["venus", "tierra", "marte"]),
    "pregunta2": ("¿Cuál es el idioma más hablado en el mundo?", "mandarin", ["ingles", "español", "hindi"]),
    "pregunta3": ("¿Qué invento se le atribuye a Alexander Graham Bell?", "telefono", ["radio", "television", "computadora"]),
    "pregunta4": ("¿Cuál es el océano más grande?", "pacifico", ["atlantico", "indico", "artico"]),
    "pregunta5": ("¿Cuál es la moneda oficial de Japón?", "yen", ["dolar", "euro", "won"]),
    "pregunta6": ("¿En qué ciudad se encuentra la Estatua de la Libertad?", "nueva york", ["los angeles", "chicago", "washington"]),
    "pregunta7": ("¿En qué país se originaron los Juegos Olímpicos?", "grecia", ["italia", "francia", "egipto"])
}


class Preguntados:
    def __init__(self):
        """Es el constructor de la clase
        """
        
        self.categorias = {
            "geografia": geografia.copy(),
            "ciencia": ciencia.copy(),
            "historia": historia.copy(),
            "cultura_general": cultura_general.copy()
        }
        self.categorias_disponibles = list(self.categorias.keys())  
        self.correctas = 0  
        self.incorrectas = 0  

    def seleccionar_categoria(self):
        """Selecciona una categoría al azar entre las disponibles
        """
        if self.categorias_disponibles:  
            self.categoria_actual = random.choice(self.categorias_disponibles)
            print(f"\nCategoría seleccionada: {self.categoria_actual.capitalize()}")
            return True
        else:
            print("\n¡No quedan más categorías disponibles!")
            return False  

    def seleccionar_pregunta(self):
        """Selecciona una pregunta aleatoria de la categoría actual
        """
        preguntas_disponibles = list(self.categorias[self.categoria_actual].values())
        
        if preguntas_disponibles:
            pregunta_completa = random.choice(preguntas_disponibles)  
            self.pregunta, self.respuesta_correcta, self.respuestas_incorrectas = pregunta_completa  
            
            pregunta_key = list(self.categorias[self.categoria_actual].keys())[preguntas_disponibles.index(pregunta_completa)]
            del self.categorias[self.categoria_actual][pregunta_key]  
            print(f"Pregunta: {self.pregunta}")
            self.generar_opciones_respuesta()
        else:
            
            print(f"\nNo quedan más preguntas en la categoría {self.categoria_actual.capitalize()}.")
            self.categorias_disponibles.remove(self.categoria_actual)

    def generar_opciones_respuesta(self):
        """Genera opciones de respuesta plausibles
        """
        opciones = [self.respuesta_correcta] + self.respuestas_incorrectas
        random.shuffle(opciones)                 
        self.opciones = {"a": opciones[0], "b": opciones[1], "c": opciones[2], "d": opciones[3]}  
        for clave, valor in self.opciones.items():
            print(f"{clave}: {valor}")

    def verificar_respuesta(self, respuesta_usuario):
        """Verifica si la respuesta del usuario es correcta
        """
        if self.opciones.get(respuesta_usuario.lower().strip()) == self.respuesta_correcta:   
            print("¡Correcto!")
            self.correctas += 1  
            if self.correctas == 10:
                print("¡Felicidades! Has ganado el juego.")
                self.mostrar_resultados()
                return True                
        else:
            print(f"Incorrecto. La respuesta correcta era: {self.respuesta_correcta}")
            self.incorrectas += 1  
            print("Has perdido el juego.")
            self.mostrar_resultados()
            return True
        return False               

    def jugar_preguntados(self):
        """Inicia el juego con 15 rondas por defecto
        """
        print("¡Bienvenido a Preguntados!")
        rondas = 15  
        
        for ronda in range(1, rondas + 1):
            if not self.seleccionar_categoria():
                break  
            else:
                print(f"\n--- Ronda {ronda}/{rondas} ---")
                self.seleccionar_pregunta()
                respuesta_usuario = input("Escribe tu respuesta (a, b, c, d): ")
                if self.verificar_respuesta(respuesta_usuario):
                    break

        
        self.mostrar_resultados()

    def mostrar_resultados(self):
        """Muestra los resultados al final del juego y pregunta qué quiere hacer el usuario
        """
        print("\n--- Fin del juego ---")
        print(f"Respuestas correctas: {self.correctas}")
        print(f"Respuestas incorrectas: {self.incorrectas}")
        print("\n--- Espero que lo hayas disfrutado ---")

        
        self.opciones_post_juego()

    def opciones_post_juego(self):
        """Presenta opciones después del juego: jugar de nuevo, ir al menú o terminar
        """
        while True:
            print("\n¿Qué te gustaría hacer ahora?")
            print("1. Volver a jugar")
            print("2. Volver al menú juegos")
            print("3. Salir")
            opcion = input("Elige una opción (1, 2, 3): ").strip()

            if opcion == "1":
                self.reiniciar_juego()
                self.jugar_preguntados()
                break
            elif opcion == "2":
                print("Volviendo al menú juegos... (aún por implementar)")
                exit()
            elif opcion == "3":
                print("¡Gracias por jugar! Hasta la próxima.")
                exit()
            else:
                print("Opción no válida. Por favor, elige 1, 2 o 3.")

    def reiniciar_juego(self):
        """Reinicia las variables para un nuevo juego
        """
        self.correctas = 0
        self.incorrectas = 0
        self.categorias_disponibles = list(self.categorias.keys())   
        for categoria in self.categorias:
            self.categorias[categoria] = globals()[categoria].copy()  
                                                                      
if __name__ == "__main__":
    preguntados = Preguntados()
    preguntados.jugar_preguntados()







#AHORCADO






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
            print("2. Volver al menú principal")
            print("3. Salir")
            opcion = input("Elige una opción (1, 2, 3): ").strip()  

            if opcion == "1":
                self.__init__()
                self.jugar()
                break
            elif opcion == "2":
                print("Volviendo al menú principal... (aún por implementar)")
                break
            elif opcion == "3":
                print("¡Gracias por jugar! Hasta la próxima.")
                exit()
            else:
                print("Opción no válida. Por favor, elige 1, 2 o 3.")

if __name__ == "__main__":     
    juego = Ahorcados()
    juego.jugar()




#TRES EN RAYA






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



#PIEDRA PAPEL TIJERA LAGARTO SPOCK




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





