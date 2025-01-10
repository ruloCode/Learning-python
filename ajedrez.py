# Resumen del proyecto
"""
Este proyecto implementa un juego de ajedrez en Python. 
Permite a dos jugadores mover piezas en un tablero 8x8, 
validar movimientos según las reglas del ajedrez y alternar turnos.
Además, incluye un sistema de puntuación y métricas.
"""

# Representación del tablero de ajedrez
# - Letras mayúsculas para piezas blancas: P (peón), R (torre), N (caballo), B (alfil), Q (reina), K (rey).
# - Letras minúsculas para piezas negras: p, r, n, b, q, k.
# - El número 0 representa una casilla vacía.

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

# Diccionario de valores de las piezas
valores_piezas = {
    'p': 1, 'P': 1,
    'n': 3, 'N': 3,
    'b': 3, 'B': 3,
    'r': 5, 'R': 5,
    'q': 9, 'Q': 9,
    'k': 0, 'K': 0  # El rey no tiene valor de captura
}

# Variables para el score y métricas
score_blanco = 0
score_negro = 0
movimientos_blanco = 0
movimientos_negro = 0
piezas_capturadas_blanco = []
piezas_capturadas_negro = []

# Función para imprimir el tablero con colores y contrastes mejorados
def imprimir_tablero(tablero):
    # Colores ANSI
    COLOR_FONDO_CLARO = "\033[47m"  # Fondo blanco
    COLOR_FONDO_OSCURO = "\033[40m"  # Fondo negro
    COLOR_TEXTO_BLANCO = "\033[97m"  # Texto blanco
    COLOR_TEXTO_NEGRO = "\033[30m"   # Texto negro
    RESET = "\033[0m"                # Restablecer colores

    print("\n   " + " ".join(["a ", "b ", "c ", "d ", "e ", "f ", "g ", "h "]))  # Columnas identificadas por letras
    for i, fila in enumerate(tablero):
        print(f"{8 - i} ", end="")  # Filas identificadas por números
        for j, casilla in enumerate(fila):
            # Alternar colores de fondo
            color_fondo = COLOR_FONDO_CLARO if (i + j) % 2 == 0 else COLOR_FONDO_OSCURO
            # Color de texto: blanco para piezas blancas, negro para piezas negras
            color_texto = COLOR_TEXTO_BLANCO if isinstance(casilla, str) and casilla.isupper() else COLOR_TEXTO_NEGRO
            pieza = casilla if casilla != 0 else " "
            print(f"{color_fondo}{color_texto} {pieza} {RESET}", end="")
        print(f" {8 - i}")
    print("   " + " ".join(["a ", "b ", "c ", "d ", "e ", "f ", "g ", "h "]))
    print()

# Función para verificar si una posición está dentro del tablero
def es_posicion_valida(fila, columna):
    return 0 <= fila < 8 and 0 <= columna < 8

# Función para verificar si una casilla está vacía o contiene una pieza enemiga
def es_casilla_valida(tablero, fila, columna, es_blanco):
    if not es_posicion_valida(fila, columna):
        return False
    pieza = tablero[fila][columna]
    return pieza == 0 or (es_blanco and pieza.islower()) or (not es_blanco and pieza.isupper())

# Función para validar movimientos de piezas
def es_movimiento_valido(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna, turno):
    pieza = tablero[fila_inicial][columna_inicial]
    if pieza == 0:
        return False  # No hay pieza en la casilla inicial

    # Verificar si la pieza pertenece al jugador actual
    if (turno == 'blanco' and pieza.islower()) or (turno == 'negro' and pieza.isupper()):
        return False

    # Movimientos específicos para cada tipo de pieza
    if pieza.lower() == 'p':  # Peón
        return validar_movimiento_peon(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna, turno)
    elif pieza.lower() == 'r':  # Torre
        return validar_movimiento_torre(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna)
    elif pieza.lower() == 'n':  # Caballo
        return validar_movimiento_caballo(fila_inicial, columna_inicial, nueva_fila, nueva_columna)
    elif pieza.lower() == 'b':  # Alfil
        return validar_movimiento_alfil(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna)
    elif pieza.lower() == 'q':  # Reina
        return validar_movimiento_reina(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna)
    elif pieza.lower() == 'k':  # Rey
        return validar_movimiento_rey(fila_inicial, columna_inicial, nueva_fila, nueva_columna)
    return False

# Funciones para validar movimientos específicos de cada pieza
def validar_movimiento_peon(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna, turno):
    direccion = -1 if turno == 'blanco' else 1  # Los peones blancos avanzan hacia arriba, los negros hacia abajo
    if columna_inicial == nueva_columna:  # Movimiento hacia adelante
        if fila_inicial + direccion == nueva_fila and tablero[nueva_fila][nueva_columna] == 0:
            return True
        if fila_inicial + 2 * direccion == nueva_fila and fila_inicial == (6 if turno == 'blanco' else 1) and tablero[nueva_fila][nueva_columna] == 0:
            return True
    elif abs(columna_inicial - nueva_columna) == 1 and fila_inicial + direccion == nueva_fila:  # Captura
        if tablero[nueva_fila][nueva_columna] != 0:
            return True
    return False

def validar_movimiento_torre(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna):
    if fila_inicial != nueva_fila and columna_inicial != nueva_columna:
        return False  # La torre solo se mueve en línea recta
    return verificar_camino_recto(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna)

def validar_movimiento_caballo(fila_inicial, columna_inicial, nueva_fila, nueva_columna):
    return (abs(fila_inicial - nueva_fila) == 2 and abs(columna_inicial - nueva_columna) == 1) or \
           (abs(fila_inicial - nueva_fila) == 1 and abs(columna_inicial - nueva_columna) == 2)

def validar_movimiento_alfil(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna):
    if abs(fila_inicial - nueva_fila) != abs(columna_inicial - nueva_columna):
        return False  # El alfil solo se mueve en diagonal
    return verificar_camino_diagonal(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna)

def validar_movimiento_reina(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna):
    if fila_inicial == nueva_fila or columna_inicial == nueva_columna:
        return verificar_camino_recto(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna)
    elif abs(fila_inicial - nueva_fila) == abs(columna_inicial - nueva_columna):
        return verificar_camino_diagonal(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna)
    return False

def validar_movimiento_rey(fila_inicial, columna_inicial, nueva_fila, nueva_columna):
    return abs(fila_inicial - nueva_fila) <= 1 and abs(columna_inicial - nueva_columna) <= 1

# Funciones auxiliares para verificar caminos libres
def verificar_camino_recto(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna):
    paso_fila = 1 if nueva_fila > fila_inicial else -1
    paso_columna = 1 if nueva_columna > columna_inicial else -1
    if fila_inicial == nueva_fila:  # Movimiento horizontal
        for col in range(columna_inicial + paso_columna, nueva_columna, paso_columna):
            if tablero[fila_inicial][col] != 0:
                return False
    else:  # Movimiento vertical
        for fila in range(fila_inicial + paso_fila, nueva_fila, paso_fila):
            if tablero[fila][columna_inicial] != 0:
                return False
    return True

def verificar_camino_diagonal(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna):
    paso_fila = 1 if nueva_fila > fila_inicial else -1
    paso_columna = 1 if nueva_columna > columna_inicial else -1
    fila, col = fila_inicial + paso_fila, columna_inicial + paso_columna
    while fila != nueva_fila and col != nueva_columna:
        if tablero[fila][col] != 0:
            return False
        fila += paso_fila
        col += paso_columna
    return True

# Función para alternar turnos
def alternar_turno(turno_actual):
    return 'blanco' if turno_actual == 'negro' else 'negro'

# Función para mover una pieza y actualizar el score
def mover_pieza(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna, turno):
    global score_blanco, score_negro, movimientos_blanco, movimientos_negro, piezas_capturadas_blanco, piezas_capturadas_negro

    if es_movimiento_valido(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna, turno):
        pieza = tablero[fila_inicial][columna_inicial]
        pieza_capturada = tablero[nueva_fila][nueva_columna]

        # Actualizar el score si se captura una pieza
        if pieza_capturada != 0:
            valor_pieza = valores_piezas.get(pieza_capturada, 0)
            if turno == 'blanco':
                score_blanco += valor_pieza
                piezas_capturadas_blanco.append(pieza_capturada)
            else:
                score_negro += valor_pieza
                piezas_capturadas_negro.append(pieza_capturada)

        # Mover la pieza
        tablero[fila_inicial][columna_inicial] = 0
        tablero[nueva_fila][nueva_columna] = pieza

        # Actualizar el número de movimientos
        if turno == 'blanco':
            movimientos_blanco += 1
        else:
            movimientos_negro += 1

        return True
    return False

# Función para mostrar el score y las métricas
def mostrar_metricas():
    print("\n--- Métricas del Juego ---")
    print(f"Score Blanco: {score_blanco}")
    print(f"Score Negro: {score_negro}")
    print(f"Movimientos Blanco: {movimientos_blanco}")
    print(f"Movimientos Negro: {movimientos_negro}")
    print(f"Piezas capturadas por Blanco: {', '.join(piezas_capturadas_blanco)}")
    print(f"Piezas capturadas por Negro: {', '.join(piezas_capturadas_negro)}")
    print("--------------------------\n")

# Juego principal
def jugar_ajedrez():
    turno = 'blanco'
    while True:
        print(f"Turno de las piezas {turno}")
        imprimir_tablero(tablero)
        mostrar_metricas()
        
        # Pedir al usuario que ingrese el movimiento
        try:
            entrada = input("Ingrese el movimiento (ejemplo: 'a2 a4'): ").strip().split()
            if len(entrada) != 2:
                print("Formato incorrecto. Intente de nuevo.")
                continue
            col_inicial, fila_inicial = entrada[0][0], int(entrada[0][1])
            col_nueva, fila_nueva = entrada[1][0], int(entrada[1][1])
            
            # Convertir coordenadas a índices de matriz
            fila_inicial = 8 - fila_inicial
            columna_inicial = ord(col_inicial) - ord('a')
            nueva_fila = 8 - fila_nueva
            nueva_columna = ord(col_nueva) - ord('a')
            
            if mover_pieza(tablero, fila_inicial, columna_inicial, nueva_fila, nueva_columna, turno):
                turno = alternar_turno(turno)
            else:
                print("Movimiento no válido, intenta de nuevo.")
        except (ValueError, IndexError):
            print("Entrada inválida. Intente de nuevo.")

# Llamar a la función principal para iniciar el juego
jugar_ajedrez()