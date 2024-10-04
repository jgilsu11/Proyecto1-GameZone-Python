import random

geografia = {
    "pregunta1": "¿Cuál es la capital de Francia?paris",
    "pregunta2": "¿Qué país tiene la mayor cantidad de habitantes?china",
    "pregunta3": "¿En qué continente se encuentra Egipto?africa",
    "pregunta4": "¿Cuál es el río más largo del mundo?nilo",
    "pregunta5": "¿Cuál es el desierto más grande del mundo?sahara",
    "pregunta6": "¿Cuál es el país más pequeño del mundo?vaticano",
    "pregunta7": "¿En qué país se encuentra la Torre Eiffel?francia"
}

ciencia = {
    "pregunta1": "¿Qué gas es fundamental para la respiración humana?oxigeno",
    "pregunta2": "¿Cuál es la fórmula química del agua?h2o",
    "pregunta3": "¿Qué tipo de animal es una ballena?mamifero",
    "pregunta4": "¿Cuántos planetas tiene el sistema solar?8",
    "pregunta5": "¿Qué planeta es conocido como el planeta rojo?marte",
    "pregunta6": "¿Cuál es el metal más abundante en la corteza terrestre?aluminio",
    "pregunta7": "¿Cuál es la unidad de medida de la corriente eléctrica?amperio"
}

historia = {
    "pregunta1": "¿En qué año se descubrió América?1492",
    "pregunta2": "¿Quién fue el primer presidente de los Estados Unidos?george washington",
    "pregunta3": "¿Cuál fue el conflicto armado que tuvo lugar entre 1939 y 1945?segunda guerra mundial",
    "pregunta4": "¿Qué revolucionario cubano nació en Argentina?che guevara",
    "pregunta5": "¿En qué año cayó el Muro de Berlín?1989",
    "pregunta6": "¿Qué imperio construyó la Gran Muralla China?chino",
    "pregunta7": "¿Quién fue el emperador de Francia durante el siglo XIX?napoleon"
}

cultura_general = {
    "pregunta1": "¿Cuál es el planeta más cercano al Sol?mercurio",
    "pregunta2": "¿Cuál es el idioma más hablado en el mundo?mandarin",
    "pregunta3": "¿Qué invento se le atribuye a Alexander Graham Bell?telefono",
    "pregunta4": "¿Cuál es el océano más grande?pacifico",
    "pregunta5": "¿Cuál es la moneda oficial de Japón?yen",
    "pregunta6": "¿En qué ciudad se encuentra la Estatua de la Libertad?nueva york",
    "pregunta7": "¿En qué país se originaron los Juegos Olímpicos?grecia"
}

class Preguntados:
    def __init__(self):
        
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
        """Selecciona una categoría al azar entre las disponibles."""
        if self.categorias_disponibles:   
            self.categoria_actual = random.choice(self.categorias_disponibles)
            print(f"\nCategoría seleccionada: {self.categoria_actual.capitalize()}")
            return True
        else:
            print("\n¡No quedan más categorías disponibles!")
            return False 
        

    def seleccionar_pregunta(self):
        """Selecciona una pregunta aleatoria de la categoría actual."""
        preguntas_disponibles = list(self.categorias[self.categoria_actual].values()) #Self.categ es el diccionario del constructor y para acceder al diccionario concreto de categoría es la self_categ_actual y el .values junto con list nos da una lista de los valores(pregunta y respuesta juntos)
        
        if preguntas_disponibles:
            pregunta_completa = random.choice(preguntas_disponibles)  
            self.pregunta, self.respuesta_correcta = pregunta_completa.split("?")  
            pregunta_key = list(self.categorias[self.categoria_actual].keys())[preguntas_disponibles.index(pregunta_completa)]
            del self.categorias[self.categoria_actual][pregunta_key]  
            print(f"Pregunta: {self.pregunta}")
        else:
            print(f"\nNo quedan más preguntas en la categoría {self.categoria_actual.capitalize()}.")
            self.categorias_disponibles.remove(self.categoria_actual)

    def verificar_respuesta(self, respuesta_usuario):
        """Verifica si la respuesta del usuario es correcta."""
        if respuesta_usuario.lower().strip() == self.respuesta_correcta.lower().strip():
            print("¡Correcto!")
            self.correctas += 1  
        else:
            print(f"Incorrecto. La respuesta correcta era: {self.respuesta_correcta}")
            self.incorrectas += 1  

    def jugar(self):
        """Inicia el juego con 15 rondas por defecto."""
        print("¡Bienvenido a Preguntados!")
        rondas = 15 
    
        for ronda in range(1, rondas + 1):
            if not self.seleccionar_categoria():   
                break
            else:
                print(f"\n--- Ronda {ronda}/{rondas} ---")
                self.seleccionar_pregunta()
                respuesta_usuario = input("Escribe tu respuesta: ")
                self.verificar_respuesta(respuesta_usuario)

        
        print("\n--- Fin del juego ---")
        print(f"Respuestas correctas: {self.correctas}")
        print(f"Respuestas incorrectas: {self.incorrectas}")
        print("\n--- Espero que lo hayas disfrutado ---")

juego = Preguntados()
juego.jugar()
