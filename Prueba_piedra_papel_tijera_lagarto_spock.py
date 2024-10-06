

import random
import os

def limpiar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_opciones_y_resultados(modo):
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

def obtener_opcion_jugador(opciones):
    while True:
        print("\nElige una opción:")
        for i, opcion in enumerate(opciones, 1):
            print(f"{i}. {opcion.capitalize()}")
        eleccion = input("Tu elección: ").strip()
        if eleccion.isdigit() and 1 <= int(eleccion) <= len(opciones):
            return opciones[int(eleccion) - 1]
        else:
            print("Opción no válida. Intenta de nuevo.")

def obtener_opcion_maquina(opciones):
    return random.choice(opciones)

def determinar_ganador(jugador, maquina, resultados):
    if jugador == maquina:
        return "empate"
    elif maquina in resultados[jugador]:
        return "jugador"
    else:
        return "maquina"

def jugar_ronda(opciones, resultados, victorias_jugador, victorias_maquina):
    jugador = obtener_opcion_jugador(opciones)
    maquina = obtener_opcion_maquina(opciones)
    print(f"\nTú elegiste: {jugador.capitalize()}")
    print(f"La máquina eligió: {maquina.capitalize()}")

    ganador = determinar_ganador(jugador, maquina, resultados)
    if ganador == "jugador":
        print("¡Ganaste esta ronda!")
        victorias_jugador += 1
    elif ganador == "maquina":
        print("La máquina ganó esta ronda.")
        victorias_maquina += 1
    else:
        print("Esta ronda es un empate.")

    print(f"\nVictorias - Jugador: {victorias_jugador}, Máquina: {victorias_maquina}")
    return victorias_jugador, victorias_maquina

def opciones_despues_del_juego():
    while True:
        print("\n¿Qué te gustaría hacer ahora?")
        print("1. Volver a jugar")
        print("2. Ir al menú principal")
        print("3. Ir al menú de juegos")
        print("4. Terminar")
        opcion = input("Elige una opción (1, 2 o 3): ").strip()

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
            print("Opción no válida. Por favor, elige 1, 2 o 3.")

def jugar(modo):
    limpiar_terminal()
    opciones, resultados = obtener_opciones_y_resultados(modo)
    victorias_jugador = 0
    victorias_maquina = 0
    rondas_para_ganar = 3

    print(f"¡Bienvenido a Piedra, Papel, Tijera{' , Lagarto, Spock' if modo == 'extendido' else ''}!")
    while victorias_jugador < rondas_para_ganar and victorias_maquina < rondas_para_ganar:
        victorias_jugador, victorias_maquina = jugar_ronda(opciones, resultados, victorias_jugador, victorias_maquina)

    if victorias_jugador == rondas_para_ganar:
        print("\n¡Felicidades! Has ganado el juego.")
    else:
        print("\nLa máquina ha ganado el juego. Mejor suerte la próxima vez.")

    return opciones_despues_del_juego()

def main_menu():
    while True:
        print("Menú Principal")
        print("1. Jugar Piedra, Papel, Tijera, Lagarto, Spock")
        print("2. Jugar Piedra, Papel, Tijera clásico")
        print("3. Salir")
        choice = input("Selecciona una opción: ")
        if choice == '1':
            resultado = jugar(modo="extendido")
            if resultado == "reiniciar":
                jugar(modo="extendido")
        elif choice == '2':
            resultado = jugar(modo="clasico")
            if resultado == "reiniciar":
                jugar(modo="clasico")
        elif choice == '3':
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main_menu()
