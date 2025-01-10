# clase_5.py

# Resumen de la clase
"""
En el mundo de la programación con Python, las operaciones matemáticas básicas como la suma, 
resta, multiplicación y división son fundamentales. Sin embargo, Python ofrece operaciones 
adicionales que expanden nuestras posibilidades.
"""

# Ejemplo 1: Operaciones matemáticas básicas
# Suma, resta, multiplicación y división.
a = 10
b = 3
print("Suma:", a + b)  # Salida: 13
print("Resta:", a - b)  # Salida: 7
print("Multiplicación:", a * b)  # Salida: 30
print("División:", a / b)  # Salida: 3.333...

# Ejemplo 2: Operador módulo
# El operador módulo (%) obtiene el residuo de una división.
a = 13
b = 5
print("Módulo:", a % b)  # Salida: 3

# Ejemplo 3: División por cero
# Dividir por cero genera un error (ZeroDivisionError).
a = 10
b = 0
try:
    print(a / b)
except ZeroDivisionError:
    print("Error: División por cero")  # Salida: Error: División por cero

# Ejemplo 4: División de enteros
# La división de enteros (//) devuelve solo la parte entera de una división.
a = 10
b = 3
print("División Entera:", a // b)  # Salida: 3

# Ejemplo 5: Potenciación
# La potenciación se representa con **.
a = 10
b = 3
print("Potenciación:", a ** b)  # Salida: 1000

# Ejemplo 6: Regla PEMDAS
# PEMDAS define la prioridad de operaciones: Paréntesis, Exponentes, Multiplicación/División, Adición/Sustracción.
operation = (2 + 3) * 4
print("Resultado de (2 + 3) * 4:", operation)  # Salida: 20

# Ejemplo 7: Operadores booleanos
# Los operadores booleanos comparan valores y devuelven True o False.
a = 10
b = 3
print("¿a > b?:", a > b)  # Salida: True
print("¿a < b?:", a < b)  # Salida: False
print("¿a == b?:", a == b)  # Salida: False
print("¿a != b?:", a != b)  # Salida: True

# Ejemplo 8: Operadores lógicos
# Los operadores lógicos (and, or, not) se usan para combinar condiciones.
x = 5
print("¿x está entre 0 y 10?:", 0 < x < 10)  # Salida: True
print("¿x es menor que 0 o mayor que 10?:", x < 0 or x > 10)  # Salida: False
print("¿x no es igual a 5?:", not x == 5)  # Salida: False

# Ejemplo 9: Operaciones con números flotantes
# Las operaciones con flotantes pueden tener resultados inesperados debido a la precisión.
print("0.1 + 0.2:", 0.1 + 0.2)  # Salida: 0.30000000000000004

# Ejemplo 10: Redondeo de números
# Usamos la función round() para redondear números.
resultado = 0.1 + 0.2
print("Redondeo de 0.1 + 0.2:", round(resultado, 2))  # Salida: 0.3
