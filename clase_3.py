# clase_3.py

# Resumen de la clase
"""
Comprender los diferentes tipos de datos en Python es crucial para la programación eficiente. 
En Python, cada variable pertenece a una clase o “class”, y su tipo puede ser identificado usando la función type().
"""

# Ejemplo 1: Tipos de datos básicos
# Usamos la función type() para verificar el tipo de dato de una variable.

# Enteros (int)
x = 5
print("Tipo de x:", type(x))  # Salida: <class 'int'>

# Flotantes (float)
y = 5.0
print("Tipo de y:", type(y))  # Salida: <class 'float'>

# Cadenas (str)
texto = "Hola, Mundo!"
print("Tipo de texto:", type(texto))  # Salida: <class 'str'>

# Booleanos (bool)
es_verdadero = True
print("Tipo de es_verdadero:", type(es_verdadero))  # Salida: <class 'bool'>

# Ejemplo 2: Notación científica
# La notación científica es útil para números muy grandes o muy pequeños.

numero_grande = 1e6  # 1,000,000
numero_pequeno = 1e-6  # 0.000001
print("Número grande:", numero_grande)  # Salida: 1000000.0
print("Número pequeño:", numero_pequeno)  # Salida: 1e-06

# Ejemplo 3: Operaciones matemáticas básicas
# Python maneja automáticamente los tipos de datos en operaciones matemáticas.

# Suma de enteros
suma_enteros = 3 + 5
print("Suma de enteros:", suma_enteros)  # Salida: 8

# Suma de entero y flotante
suma_mixta = 3 + 5.0
print("Suma mixta:", suma_mixta)  # Salida: 8.0

# Multiplicación de flotantes
multiplicacion_flotantes = 2.5 * 4.0
print("Multiplicación de flotantes:", multiplicacion_flotantes)  # Salida: 10.0

# División de enteros (devuelve flotante)
division = 10 / 2
print("División de enteros:", division)  # Salida: 5.0

# Ejemplo 4: Booleanos y operaciones lógicas
# Los booleanos son fundamentales para las estructuras de control.

es_mayor = 10 > 5  # True
es_menor = 10 < 5  # False
print("¿10 es mayor que 5?:", es_mayor)  # Salida: True
print("¿10 es menor que 5?:", es_menor)  # Salida: False

# Operaciones lógicas
and_resultado = es_mayor and es_menor  # False
or_resultado = es_mayor or es_menor  # True
not_resultado = not es_mayor  # False
print("AND lógico:", and_resultado)  # Salida: False
print("OR lógico:", or_resultado)  # Salida: True
print("NOT lógico:", not_resultado)  # Salida: False

# Ejemplo 5: Comentarios en Python
# Los comentarios se usan para explicar el código y no son ejecutados.

# Este es un comentario de una línea
suma = 3 + 5  # Este es un comentario al final de una línea

"""
Este es un comentario
de múltiples líneas.
Python lo ignora completamente.
"""

# Ejemplo 6: Conversión entre tipos de datos
# Python permite convertir entre tipos de datos usando funciones como int(), float(), str(), etc.

# Conversión de entero a flotante
entero = 10
flotante = float(entero)
print("Entero a flotante:", flotante)  # Salida: 10.0

# Conversión de flotante a entero
flotante = 10.7
entero = int(flotante)
print("Flotante a entero:", entero)  # Salida: 10 (se trunca el decimal)

# Conversión de cadena a entero
cadena = "123"
entero = int(cadena)
print("Cadena a entero:", entero)  # Salida: 123

# Conversión de entero a cadena
entero = 456
cadena = str(entero)
print("Entero a cadena:", cadena)  # Salida: '456'

