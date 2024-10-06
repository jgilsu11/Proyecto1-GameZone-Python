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

