# Símbolos de los jugadores
j1 = "X"
j2 = "O"

# Nombres de los jugadores
nombre1 = input("Nombre del jugador 1: ")
nombre2 = input("Nombre del jugador 2: ")

# Crear el tablero definitivo, que consiste en 9 tableros pequeños
tablero_definitivo = [[[' ' for _ in range(3)] for _ in range(3)] for _ in range(9)]

# Lista para rastrear el estado de cada tablero pequeño (si tiene ganador o no)
estado_tablero_pequeño = [' ' for _ in range(9)]

# Función para mostrar el tablero
def dibujarTablero():
    for fila_grande in range(3):
        for fila_pequeña in range(3):
            linea = ''
            for col_grande in range(3):
                indice_tablero = fila_grande * 3 + col_grande
                linea += ' | '.join(tablero_definitivo[indice_tablero][fila_pequeña])
                if col_grande < 2:
                    linea += ' || '
            print(linea)
        if fila_grande < 2:
            print("-" * 11 + "++" + "-" * 11 + "++" + "-" * 11)

# Función para verificar si un jugador ha ganado en un tablero pequeño
def verificar_tablero_pequeño(tablero):
    condiciones_ganar = [
        [(0, 0), (0, 1), (0, 2)], # filas
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)], # columnas
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)], # diagonales
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condicion in condiciones_ganar:
        if tablero[condicion[0][0]][condicion[0][1]] == tablero[condicion[1][0]][condicion[1][1]] == tablero[condicion[2][0]][condicion[2][1]] != ' ':
            return tablero[condicion[0][0]][condicion[0][1]]
    return None

# Función para verificar al ganador definitivo del juego
def verificar_ganador_definitivo():
    return verificar_tablero_pequeño([estado_tablero_pequeño[i:i+3] for i in range(0, 9, 3)])

# Función para validar la entrada
def obtener_entrada_valida(tablero_objetivo=None):
    while True:
        try:
            if tablero_objetivo is not None:
                print(f"Debe jugar en el tablero {tablero_objetivo + 1}.")
                movimiento = tablero_objetivo
            else:
                movimiento = int(input("Ingrese el número del tablero (1-9): ")) - 1
            
            if 0 <= movimiento < 9:
                return movimiento
            else:
                print("Entrada inválida. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")

# Función para elegir un tablero alternativo
def elegir_tablero_alternativo():
    print("El tablero al que se te mandó ya ha sido ganado. Puedes elegir uno de los siguientes tableros:")
    for i in range(9):
        if estado_tablero_pequeño[i] == ' ':
            print(f"Tablero {i + 1}")
    while True:
        tablero_opcion = int(input("Ingrese el número del tablero (1-9): ")) - 1
        if 0 <= tablero_opcion < 9 and estado_tablero_pequeño[tablero_opcion] == ' ':
            return tablero_opcion
        else:
            print("Entrada inválida. Intente de nuevo.")

# Ciclo principal del juego
jugador_actual = j1
tablero_siguiente = None

while True:
    dibujarTablero()
    
    # Elegir el tablero y la casilla
    print(f"Turno de {nombre1 if jugador_actual == j1 else nombre2} ({jugador_actual})")
    
    if tablero_siguiente is None:
        tablero_pequeño = obtener_entrada_valida()
    else:
        tablero_pequeño = tablero_siguiente

    casilla = obtener_entrada_valida()

    # Asegurarse de que el tablero pequeño no haya sido ganado y la casilla esté vacía
    if estado_tablero_pequeño[tablero_pequeño] == ' ' and tablero_definitivo[tablero_pequeño][casilla // 3][casilla % 3] == ' ':
        # Colocar el símbolo del jugador
        tablero_definitivo[tablero_pequeño][casilla // 3][casilla % 3] = jugador_actual

        # Verificar si el jugador ganó este tablero pequeño
        ganador = verificar_tablero_pequeño(tablero_definitivo[tablero_pequeño])
        if ganador:
            estado_tablero_pequeño[tablero_pequeño] = ganador
            print(f"¡Felicidades! ¡{ganador} ha ganado el tablero {tablero_pequeño + 1}!")

        # Verificar si hay un ganador definitivo
        ganador_definitivo = verificar_ganador_definitivo()
        if ganador_definitivo:
            dibujarTablero()
            print(f"¡{ganador_definitivo} ha ganado el juego!")
            break

        # Determinar el tablero objetivo para el oponente
        tablero_siguiente = casilla  # El tablero correspondiente a la casilla elegida

        # Si el tablero al que se envía al oponente ya ha sido ganado
        if estado_tablero_pequeño[tablero_siguiente] != ' ':
            tablero_siguiente = elegir_tablero_alternativo()  # Permitir elegir otro tablero

        # Mostrar el tablero y luego informar al siguiente jugador
        print(f"Jugador ha jugado en el tablero {tablero_pequeño + 1}, así que te ha mandado a tablero {tablero_siguiente + 1}.")
        
        # Cambiar de jugador
        jugador_actual = j2 if jugador_actual == j1 else j1
    else:
        print("Movimiento no válido, intente otra vez.")