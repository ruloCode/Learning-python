# clase_9.py

# Resumen de la clase
"""
Las matrices en Python son una herramienta poderosa que permite organizar datos en listas 
de listas, facilitando su manejo y manipulación. Además, las tuplas son estructuras 
inmutables que se utilizan para almacenar datos que no deben cambiar.
"""

# Ejemplo 1: Creación de una matriz
# Una matriz es una lista de listas, donde cada sublista representa una fila.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz inicial:")
for row in matrix:
    print(row)

# Ejemplo 2: Iterar a través de una matriz
# Usamos bucles for anidados para recorrer cada elemento de la matriz.
print("\nIterar e imprimir cada elemento de la matriz:")
for row in matrix:
    for element in row:
        print(element)

# Ejemplo 3: Acceder a elementos específicos en una matriz
# Para acceder a un elemento, usamos los índices de fila y columna.
print("\nAcceder al elemento en la fila 2, columna 2 (número 9):")
print(matrix[2][2])  # Salida: 9

# Ejemplo 4: Modificar elementos en una matriz
# Las matrices son mutables, por lo que podemos cambiar sus elementos.
matrix[0][0] = 10
print("\nMatriz después de modificar el primer elemento:")
for row in matrix:
    print(row)

# Ejemplo 5: Creación de una tupla
# Las tuplas son inmutables y se crean usando paréntesis.
numbers = (1, 2, 3)
print("\nTupla inicial:")
print(numbers)

# Ejemplo 6: Intentar modificar una tupla
# Las tuplas no permiten modificación después de su creación.
try:
    numbers[0] = 10  # Esto generará un error
except TypeError as e:
    print("\nError al intentar modificar la tupla:", e)

# Ejemplo 7: Diferencias entre matrices y tuplas
# Las matrices son mutables, mientras que las tuplas son inmutables.
# Aquí se muestra cómo agregar una nueva fila a una matriz.
matrix.append([10, 11, 12])
print("\nMatriz después de agregar una nueva fila:")
for row in matrix:
    print(row)

# Ejemplo 8: Uso de tuplas en matrices
# Podemos almacenar tuplas dentro de una matriz.
matrix_with_tuples = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
]
print("\nMatriz con tuplas:")
for row in matrix_with_tuples:
    print(row)

# Ejemplo 9: Acceso a elementos en una matriz de tuplas
# Accedemos a elementos específicos usando índices.
print("\nAcceder al elemento en la fila 1, columna 2 de la matriz de tuplas:")
print(matrix_with_tuples[1][2])  # Salida: 6

# Ejemplo 10: Uso de tuplas para coordenadas
# Las tuplas son útiles para representar coordenadas o pares de valores.
coordenadas = [(1, 2), (3, 4), (5, 6)]
print("\nCoordenadas:")
for x, y in coordenadas:
    print(f"X: {x}, Y: {y}")
