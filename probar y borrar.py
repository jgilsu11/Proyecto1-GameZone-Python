#Intento fallido de menú
#Prueba gitignore
class Preguntados(Juego):
    def __init__(self, menu):
        """Es el constructor de la clase
        """
        super().__init__(menu)
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

    def jugar(self):
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

        
        self.opciones_post()

    def opciones_post(self):
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
                self.jugar()
                break
            elif opcion == "2":
                print("Volviendo al menú juegos...")
                self.menu.ejecutar()
                break 
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
