# clase_8.py

# Resumen de la clase
"""
Cuando asignamos una lista a una nueva variable, por ejemplo, B = A, no estamos creando 
una copia independiente. Ambas variables apuntan al mismo espacio de memoria. Así, 
cualquier cambio en A se reflejará en B.
"""

# Ejemplo 1: Asignación de listas y memoria compartida
# Al asignar una lista a otra variable, ambas apuntan al mismo espacio de memoria.
A = [1, 2, 3, 4, 5]
B = A  # B apunta al mismo espacio de memoria que A

print("Lista A:", A)
print("Lista B:", B)

# Modificamos la lista A
A.append(6)
print("Después de modificar A:")
print("Lista A:", A)
print("Lista B:", B)  # B también refleja el cambio

# Verificamos los IDs de memoria
print("ID de A:", id(A))
print("ID de B:", id(B))  # Ambos IDs son iguales

# Ejemplo 2: Crear una copia independiente usando slicing
# Para evitar que dos variables apunten al mismo espacio de memoria, usamos slicing.
A = [1, 2, 3, 4, 5]
C = A[:]  # C es una copia independiente de A

print("Lista A:", A)
print("Lista C:", C)

# Modificamos la lista A
A.append(6)
print("Después de modificar A:")
print("Lista A:", A)
print("Lista C:", C)  # C no refleja el cambio

# Verificamos los IDs de memoria
print("ID de A:", id(A))
print("ID de C:", id(C))  # Los IDs son diferentes

# Ejemplo 3: Uso de la función copy() para crear una copia
# Otra forma de crear una copia independiente es usando el método copy().
A = [1, 2, 3, 4, 5]
D = A.copy()  # D es una copia independiente de A

print("Lista A:", A)
print("Lista D:", D)

# Modificamos la lista A
A.append(6)
print("Después de modificar A:")
print("Lista A:", A)
print("Lista D:", D)  # D no refleja el cambio

# Verificamos los IDs de memoria
print("ID de A:", id(A))
print("ID de D:", id(D))  # Los IDs son diferentes

# Ejemplo 4: Copias superficiales vs copias profundas
# Las copias superficiales no funcionan correctamente con listas anidadas.
A = [1, 2, [3, 4]]
B = A[:]  # Copia superficial

print("Lista A:", A)
print("Lista B:", B)

# Modificamos la lista anidada en A
A[2].append(5)
print("Después de modificar la lista anidada en A:")
print("Lista A:", A)
print("Lista B:", B)  # B también refleja el cambio en la lista anidada

# Para copias profundas, usamos el módulo copy.
import copy

A = [1, 2, [3, 4]]
C = copy.deepcopy(A)  # Copia profunda

print("Lista A:", A)
print("Lista C:", C)

# Modificamos la lista anidada en A
A[2].append(5)
print("Después de modificar la lista anidada en A:")
print("Lista A:", A)
print("Lista C:", C)  # C no refleja el cambio en la lista anidada
