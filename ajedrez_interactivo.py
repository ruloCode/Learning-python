import curses

# Representación del tablero de ajedrez
tablero = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],  # Fila 0: Piezas negras
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  # Fila 1: Peones negros
    [0, 0, 0, 0, 0, 0, 0, 0],                  # Fila 2: Casillas vacías
    [0, 0, 0, 0, 0, 0, 0, 0],                  # Fila 3: Casillas vacías
    [0, 0, 0, 0, 0, 0, 0, 0],                  # Fila 4: Casillas vacías
    [0, 0, 0, 0, 0, 0, 0, 0],                  # Fila 5: Casillas vacías
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # Fila 6: Peones blancos
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']   # Fila 7: Piezas blancas
]

# Función para imprimir el tablero con colores y contrastes mejorados
def imprimir_tablero(stdscr, tablero, seleccion=None, movimientos_validos=None):
    stdscr.clear()
    # Colores ANSI
    COLOR_FONDO_CLARO = curses.color_pair(1)  # Fondo blanco
    COLOR_FONDO_OSCURO = curses.color_pair(2)  # Fondo negro
    COLOR_TEXTO_BLANCO = curses.color_pair(3)  # Texto blanco
    COLOR_TEXTO_NEGRO = curses.color_pair(4)   # Texto negro
    COLOR_SELECCION = curses.color_pair(5)     # Color para la selección
    COLOR_MOVIMIENTOS = curses.color_pair(6)   # Color para movimientos válidos

    stdscr.addstr(0, 0, "   a b c d e f g h\n")  # Columnas identificadas por letras
    for i, fila in enumerate(tablero):
        stdscr.addstr(f"{8 - i} ")  # Filas identificadas por números
        for j, casilla in enumerate(fila):
            # Alternar colores de fondo
            color_fondo = COLOR_FONDO_CLARO if (i + j) % 2 == 0 else COLOR_FONDO_OSCURO
            # Color de texto: blanco para piezas blancas, negro para piezas negras
            color_texto = COLOR_TEXTO_BLANCO if isinstance(casilla, str) and casilla.isupper() else COLOR_TEXTO_NEGRO
            pieza = casilla if casilla != 0 else " "

            # Resaltar la casilla seleccionada
            if seleccion and (i, j) == seleccion:
                stdscr.addstr(f" {pieza} ", COLOR_SELECCION)
            # Resaltar movimientos válidos
            elif movimientos_validos and (i, j) in movimientos_validos:
                stdscr.addstr(f" {pieza} ", COLOR_MOVIMIENTOS)
            else:
                stdscr.addstr(f" {pieza} ", color_fondo | color_texto)
        stdscr.addstr(f" {8 - i}\n")
    stdscr.addstr("   a b c d e f g h\n")
    stdscr.refresh()

# Función para verificar si una posición está dentro del tablero
def es_posicion_valida(fila, columna):
    return 0 <= fila < 8 and 0 <= columna < 8

# Función para verificar si una casilla está vacía o contiene una pieza enemiga
def es_casilla_valida(tablero, fila, columna, es_blanco):
    if not es_posicion_valida(fila, columna):
        return False
    pieza = tablero[fila][columna]
    return pieza == 0 or (es_blanco and pieza.islower()) or (not es_blanco and pieza.isupper())

# Función para obtener movimientos válidos de una pieza
def obtener_movimientos_validos(tablero, fila, columna, turno):
    movimientos_validos = []
    pieza = tablero[fila][columna]
    if pieza == 0:
        return movimientos_validos

    # Movimientos específicos para cada tipo de pieza
    if pieza.lower() == 'p':  # Peón
        direccion = -1 if turno == 'blanco' else 1
        if es_casilla_valida(tablero, fila + direccion, columna, turno == 'blanco'):
            movimientos_validos.append((fila + direccion, columna))
        if es_casilla_valida(tablero, fila + 2 * direccion, columna, turno == 'blanco') and \
           ((turno == 'blanco' and fila == 6) or (turno == 'negro' and fila == 1)):
            movimientos_validos.append((fila + 2 * direccion, columna))
    elif pieza.lower() == 'r':  # Torre
        for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            f, c = fila + df, columna + dc
            while es_posicion_valida(f, c):
                if es_casilla_valida(tablero, f, c, turno == 'blanco'):
                    movimientos_validos.append((f, c))
                    if tablero[f][c] != 0:
                        break
                else:
                    break
                f += df
                c += dc
    elif pieza.lower() == 'n':  # Caballo
        for df, dc in [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]:
            f, c = fila + df, columna + dc
            if es_casilla_valida(tablero, f, c, turno == 'blanco'):
                movimientos_validos.append((f, c))
    elif pieza.lower() == 'b':  # Alfil
        for df, dc in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            f, c = fila + df, columna + dc
            while es_posicion_valida(f, c):
                if es_casilla_valida(tablero, f, c, turno == 'blanco'):
                    movimientos_validos.append((f, c))
                    if tablero[f][c] != 0:
                        break
                else:
                    break
                f += df
                c += dc
    elif pieza.lower() == 'q':  # Reina
        for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            f, c = fila + df, columna + dc
            while es_posicion_valida(f, c):
                if es_casilla_valida(tablero, f, c, turno == 'blanco'):
                    movimientos_validos.append((f, c))
                    if tablero[f][c] != 0:
                        break
                else:
                    break
                f += df
                c += dc
    elif pieza.lower() == 'k':  # Rey
        for df, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            f, c = fila + df, columna + dc
            if es_casilla_valida(tablero, f, c, turno == 'blanco'):
                movimientos_validos.append((f, c))
    return movimientos_validos

# Función para alternar turnos
def alternar_turno(turno_actual):
    return 'blanco' if turno_actual == 'negro' else 'negro'

# Función para mover una pieza
def mover_pieza(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna, turno):
    if (nueva_fila, nueva_columna) in obtener_movimientos_validos(tablero, fila_inicial, columna_inicial, turno):
        pieza = tablero[fila_inicial][columna_inicial]
        tablero[fila_inicial][columna_inicial] = 0
        tablero[nueva_fila][nueva_columna] = pieza
        return True
    return False

# Función principal del juego
def main(stdscr):
    # Inicializar colores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Fondo claro
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Fondo oscuro
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Texto blanco
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Texto negro
    curses.init_pair(5, curses.COLOR_RED, curses.COLOR_YELLOW)   # Selección
    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Movimientos válidos

    turno = 'blanco'
    seleccion = None
    movimientos_validos = []

    while True:
        imprimir_tablero(stdscr, tablero, seleccion, movimientos_validos)
        stdscr.addstr(10, 0, "Instrucciones: Flechas para mover, Espacio para seleccionar/mover, Q para salir")
        stdscr.addstr(11, 0, f"Turno de las piezas {turno}")
        key = stdscr.getch()

        if key == curses.KEY_UP:
            if seleccion:
                seleccion = (max(0, seleccion[0] - 1), seleccion[1])
            else:
                seleccion = (7, 0)  # Iniciar en la esquina superior izquierda
        elif key == curses.KEY_DOWN:
            if seleccion:
                seleccion = (min(7, seleccion[0] + 1), seleccion[1])
        elif key == curses.KEY_LEFT:
            if seleccion:
                seleccion = (seleccion[0], max(0, seleccion[1] - 1))
        elif key == curses.KEY_RIGHT:
            if seleccion:
                seleccion = (seleccion[0], min(7, seleccion[1] + 1))
        elif key == ord(' '):  # Espacio para seleccionar o mover
            if seleccion:
                # Capturar la posición de destino
                nueva_fila, nueva_columna = seleccion
                if mover_pieza(tablero, seleccion[0], seleccion[1], nueva_fila, nueva_columna, turno):
                    turno = alternar_turno(turno)
                    seleccion = None
                    movimientos_validos = []
            else:
                seleccion = (fila, columna)
                movimientos_validos = obtener_movimientos_validos(tablero, fila, columna, turno)
        elif key == ord('q'):  # Salir del juego
            break

# Llamar a la función principal con curses
curses.wrapper(main)