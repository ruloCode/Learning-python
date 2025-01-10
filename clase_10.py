# clase_10.py

# Resumen de la clase
"""
Las matrices son una herramienta fundamental en muchas áreas de la computación y las matemáticas. 
En Python, podemos usar listas dentro de listas para representar matrices bidimensionales (2D). 
Hoy, vamos a explorar varias aplicaciones prácticas de las matrices, específicamente en la 
representación de tableros de juego como el ajedrez, y cómo implementar movimientos de piezas.
"""

# Ejemplo 1: Representación de un tablero de ajedrez
# Un tablero de ajedrez es una matriz de 8x8. Usamos letras para representar las piezas:
# - Letras mayúsculas para piezas blancas: P (peón), R (torre), N (caballo), B (alfil), Q (reina), K (rey).
# - Letras minúsculas para piezas negras: p, r, n, b, q, k.
# - El número 0 representa una casilla vacía.

chess_board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],  # Fila 0: Piezas negras
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  # Fila 1: Peones negros
    [0, 0, 0, 0, 0, 0, 0, 0],                  # Fila 2: Casillas vacías
    [0, 0, 0, 0, 0, 0, 0, 0],                  # Fila 3: Casillas vacías
    [0, 0, 0, 0, 0, 0, 0, 0],                  # Fila 4: Casillas vacías
    [0, 0, 0, 0, 0, 0, 0, 0],                  # Fila 5: Casillas vacías
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # Fila 6: Peones blancos
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']   # Fila 7: Piezas blancas
]

# Función para imprimir el tablero de manera legible
def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)
    print()  # Espacio adicional para separar las impresiones

print("Tablero de ajedrez inicial:")
imprimir_tablero(chess_board)

# Ejemplo 2: Movimiento de un caballo
# En ajedrez, los caballos se mueven en forma de "L":
# - Dos casillas en una dirección y luego una casilla perpendicular.
# - O una casilla en una dirección y luego dos casillas perpendicularmente.

# Posición inicial del caballo blanco en (7, 1)
fila_inicial, columna_inicial = 7, 1
print(f"Posición inicial del caballo: ({fila_inicial}, {columna_inicial})")

# Movimientos posibles del caballo en forma de "L"
movimientos_caballo = [
    (-2, -1), (-1, -2),  # Movimientos hacia arriba-izquierda
    (-2, 1), (-1, 2),    # Movimientos hacia arriba-derecha
    (2, -1), (1, -2),    # Movimientos hacia abajo-izquierda
    (2, 1), (1, 2)       # Movimientos hacia abajo-derecha
]

# Función para verificar si una posición está dentro del tablero
def es_posicion_valida(fila, columna):
    return 0 <= fila < 8 and 0 <= columna < 8

# Función para verificar si una casilla está vacía o contiene una pieza enemiga
def es_casilla_valida(tablero, fila, columna, es_blanco):
    if not es_posicion_valida(fila, columna):
        return False
    pieza = tablero[fila][columna]
    return pieza == 0 or (es_blanco and pieza.islower()) or (not es_blanco and pieza.isupper())

# Mostrar movimientos válidos del caballo
print("Movimientos válidos del caballo desde la posición inicial:")
for movimiento in movimientos_caballo:
    nueva_fila = fila_inicial + movimiento[0]
    nueva_columna = columna_inicial + movimiento[1]
    if es_casilla_valida(chess_board, nueva_fila, nueva_columna, es_blanco=True):
        print(f"Posición válida: ({nueva_fila}, {nueva_columna})")

# Ejemplo 3: Mover el caballo a una nueva posición
# Movemos el caballo de (7, 1) a (5, 2)
nueva_fila, nueva_columna = 5, 2

# Verificamos si la nueva posición es válida
if es_casilla_valida(chess_board, nueva_fila, nueva_columna, es_blanco=True):
    # Movemos el caballo
    chess_board[fila_inicial][columna_inicial] = 0  # Casilla original ahora está vacía
    chess_board[nueva_fila][nueva_columna] = 'N'   # Nueva posición del caballo
    print("\nTablero después de mover el caballo:")
    imprimir_tablero(chess_board)
else:
    print("Movimiento no válido: la posición de destino no es válida.")

# Ejemplo 4: Validación adicional
# Intentamos mover el caballo a una posición inválida (fuera del tablero)
nueva_fila, nueva_columna = 8, 2  # Fuera del tablero

if es_casilla_valida(chess_board, nueva_fila, nueva_columna, es_blanco=True):
    chess_board[fila_inicial][columna_inicial] = 0
    chess_board[nueva_fila][nueva_columna] = 'N'
else:
    print("\nMovimiento no válido: la posición de destino está fuera del tablero.")

# Ejemplo 5: Movimiento que captura una pieza enemiga
# Supongamos que hay un peón negro en (5, 2)
chess_board[5][2] = 'p'  # Colocamos un peón negro en (5, 2)
print("Tablero con un peón negro en (5, 2):")
imprimir_tablero(chess_board)

# Movemos el caballo a (5, 2) para capturar el peón
if es_casilla_valida(chess_board, 5, 2, es_blanco=True):
    chess_board[fila_inicial][columna_inicial] = 0  # Casilla original ahora está vacía
    chess_board[5][2] = 'N'  # Nueva posición del caballo
    print("Tablero después de capturar el peón negro:")
    imprimir_tablero(chess_board)
else:
    print("Movimiento no válido: la posición de destino no es válida.")
