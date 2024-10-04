import random

# Estructura original con la respuesta correcta incluida
geografia = {
    "pregunta1": "¿Cuál es la capital de Francia?paris",
    "pregunta2": "¿Qué país tiene la mayor cantidad de habitantes?china",
    "pregunta3": "¿En qué continente se encuentra Egipto?africa",
    "pregunta4": "¿Cuál es el río más largo del mundo?nilo"
}

ciencia = {
    "pregunta1": "¿Qué gas es fundamental para la respiración humana?oxigeno",
    "pregunta2": "¿Cuál es la fórmula química del agua?h2o",
    "pregunta3": "¿Qué tipo de animal es una ballena?mamifero",
    "pregunta4": "¿Cuántos planetas tiene el sistema solar?8"
}

historia = {
    "pregunta1": "¿En qué año se descubrió América?1492",
    "pregunta2": "¿Quién fue el primer presidente de los Estados Unidos?george washington",
    "pregunta3": "¿Cuál fue el conflicto armado que tuvo lugar entre 1939 y 1945?segunda guerra mundial",
    "pregunta4": "¿Qué revolucionario cubano nació en Argentina?che guevara"
}

cultura_general = {
    "pregunta1": "¿Cuál es el planeta más cercano al Sol?mercurio",
    "pregunta2": "¿Cuál es el idioma más hablado en el mundo?mandarin",
    "pregunta3": "¿Qué invento se le atribuye a Alexander Graham Bell?telefono",
    "pregunta4": "¿Cuál es el océano más grande?pacifico"
}

# Clase Preguntados
class Preguntados:
    def __init__(self):
        # Diccionario que contiene las categorías y sus preguntas
        self.categorias = {
            "geografia": geografia.copy(),  # Usamos .copy() para no modificar los originales
            "ciencia": ciencia.copy(),
            "historia": historia.copy(),
            "cultura_general": cultura_general.copy()
        }
        self.categorias_disponibles = list(self.categorias.keys())  # Lista de categorías disponibles
        self.correctas = 0  # Para contar las respuestas correctas
        self.incorrectas = 0  # Para contar las respuestas incorrectas

    def seleccionar_categoria(self):
        """Selecciona una categoría al azar entre las disponibles."""
        if self.categorias_disponibles:
            self.categoria_actual = random.choice(self.categorias_disponibles)
            print(f"\nCategoría seleccionada: {self.categoria_actual.capitalize()}")
        else:
            print("\n¡No quedan más categorías disponibles!")
            return False  # Devuelve False si no quedan categorías
        return True

    def seleccionar_pregunta(self):
        """Selecciona una pregunta aleatoria de la categoría actual."""
        preguntas_disponibles = list(self.categorias[self.categoria_actual].values())
        
        if preguntas_disponibles:
            pregunta_completa = random.choice(preguntas_disponibles)  # Selecciona una pregunta aleatoria
            self.pregunta, self.respuesta_correcta = pregunta_completa.split("?")  # Separa la pregunta y la respuesta
            # Eliminar la pregunta ya hecha del diccionario
            pregunta_key = list(self.categorias[self.categoria_actual].keys())[preguntas_disponibles.index(pregunta_completa)]
            del self.categorias[self.categoria_actual][pregunta_key]  # Elimina la pregunta hecha
            print(f"Pregunta: {self.pregunta}")
        else:
            # Si no quedan preguntas en la categoría, la eliminamos de las categorías disponibles
            print(f"\nNo quedan más preguntas en la categoría {self.categoria_actual.capitalize()}.")
            self.categorias_disponibles.remove(self.categoria_actual)

    def verificar_respuesta(self, respuesta_usuario):
        """Verifica si la respuesta del usuario es correcta."""
        if respuesta_usuario.lower().strip() == self.respuesta_correcta.lower().strip():
            print("¡Correcto!")
            self.correctas += 1  # Incrementa el contador de respuestas correctas
        else:
            print(f"Incorrecto. La respuesta correcta era: {self.respuesta_correcta}")
            self.incorrectas += 1  # Incrementa el contador de respuestas incorrectas

    def jugar(self):
        """Inicia el juego con 15 rondas por defecto."""
        print("¡Bienvenido a Preguntados!")
        rondas = 15  # Número de rondas por defecto
        
        for ronda in range(1, rondas + 1):
            if not self.seleccionar_categoria():
                break  # Si no quedan categorías disponibles, se termina el juego
            print(f"\n--- Ronda {ronda}/{rondas} ---")
            self.seleccionar_pregunta()
            respuesta_usuario = input("Escribe tu respuesta: ")
            self.verificar_respuesta(respuesta_usuario)

        # Al finalizar las rondas o si no hay más preguntas, mostramos los resultados
        print("\n--- Fin del juego ---")
        print(f"Respuestas correctas: {self.correctas}")
        print(f"Respuestas incorrectas: {self.incorrectas}")

# Inicializamos y jugamos
juego = Preguntados()
juego.jugar()
