# clase_7.py

# Resumen de la clase
"""
Las listas en Python nos facilitan la tarea de permitir la manipulación y almacenamiento 
de datos diversos de manera estructurada y eficiente.
"""

# Ejemplo 1: Creación de una lista
# Las listas se crean utilizando corchetes y pueden contener múltiples elementos.
todo = ["Dirigirnos al hotel", "Almorzar", "Visitar un museo", "Volver al hotel"]
print("Lista 'todo':", todo)

# Ejemplo 2: Tipos de datos en listas
# Las listas pueden almacenar diferentes tipos de datos, incluyendo otras listas.
mix = ["string", 1, 2.5, True, [3, 4]]
print("Lista 'mix':", mix)

# Ejemplo 3: Longitud de una lista
# Usamos la función len() para determinar cuántos elementos hay en una lista.
print("Longitud de 'mix':", len(mix))  # Salida: 5

# Ejemplo 4: Acceso a elementos de una lista
# Los elementos de una lista se acceden utilizando índices.
print("Primer elemento de 'mix':", mix[0])  # Salida: string
print("Último elemento de 'mix':", mix[-1])  # Salida: [3, 4]

# Ejemplo 5: Slicing en listas
# El slicing permite obtener sublistas especificando un rango de índices.
print("Elementos del índice 1 al 2:", mix[1:3])  # Salida: [1, 2.5]
print("Elementos desde el inicio hasta el índice 1:", mix[:2])  # Salida: ['string', 1]
print("Elementos desde el índice 2 hasta el final:", mix[2:])  # Salida: [2.5, True, [3, 4]]

# Ejemplo 6: Métodos de manipulación de listas
# Añadir elementos al final de la lista: append()
mix.append(False)
print("Lista 'mix' después de append:", mix)  # Salida: ['string', 1, 2.5, True, [3, 4], False]

# Insertar elementos en una posición específica: insert()
mix.insert(1, ["A", "B"])
print("Lista 'mix' después de insert:", mix)  # Salida: ['string', ['A', 'B'], 1, 2.5, True, [3, 4], False]

# Encontrar la primera aparición de un elemento: index()
print("Índice de ['A', 'B']:", mix.index(["A", "B"]))  # Salida: 1

# Encontrar el mayor y menor elemento: max() y min()
numbers = [1, 2, 3.5, 90, 100]
print("Máximo de 'numbers':", max(numbers))  # Salida: 100
print("Mínimo de 'numbers':", min(numbers))  # Salida: 1

# Ejemplo 7: Eliminación de elementos de una lista
# Eliminar por índice: del
del numbers[-1]
print("Lista 'numbers' después de eliminar el último elemento:", numbers)  # Salida: [1, 2, 3.5, 90]

# Eliminar una porción de la lista: del
del numbers[0:2]
print("Lista 'numbers' después de eliminar los primeros dos elementos:", numbers)  # Salida: [3.5, 90]

# Eliminar toda la lista: del
del numbers
# print(numbers)  # Esto generará un NameError porque la lista ya no existe

# Ejemplo 8: Otros métodos útiles de listas
# Ordenar una lista: sort()
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numeros.sort()
print("Lista 'numeros' ordenada:", numeros)  # Salida: [1, 1, 2, 3, 4, 5, 5, 6, 9]

# Invertir una lista: reverse()
numeros.reverse()
print("Lista 'numeros' invertida:", numeros)  # Salida: [9, 6, 5, 5, 4, 3, 2, 1, 1]

# Contar ocurrencias de un elemento: count()
print("Número de veces que aparece 5:", numeros.count(5))  # Salida: 2
