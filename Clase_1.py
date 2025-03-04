# clase_1.py

# Resumen de la clase
"""
Comprender los conceptos de semántica y sintaxis es crucial en programación. 
La semántica da sentido al código, asegurando consistencia y coherencia en las operaciones, 
mientras que la sintaxis dicta cómo escribir correctamente el código, siguiendo reglas específicas.
"""

# Ejemplo 1: Semántica en programación
# La semántica se refiere al significado y consistencia del código.
# Aquí, trabajamos con números, por lo que las entradas y salidas deben ser números.

# Correcto: Semántica coherente
numero_1 = 10
numero_2 = 20
suma = numero_1 + numero_2
print("La suma es:", suma)  # Salida esperada: La suma es: 30

# Incorrecto: Semántica inconsistente
# nombre = "Juan"
# edad = 25
# suma_incoherente = nombre + edad  # Esto generará un error de tipo TypeError

# Ejemplo 2: Sintaxis en programación
# La sintaxis es el conjunto de reglas que dicta cómo escribir el código correctamente.

# Correcto: Sintaxis válida
if suma > 15:
    print("La suma es mayor que 15")

# Incorrecto: Error de sintaxis
# if suma > 15
#     print("La suma es mayor que 15")  # Falta el dos puntos al final del if

# Ejemplo 3: Manejo de errores de sintaxis
# El entorno de desarrollo o el compilador indicará errores de sintaxis.

# Error de sintaxis común: Paréntesis sin cerrar
# print("Hola, mundo"  # Falta cerrar el paréntesis

# Ejemplo 4: Uso correcto de variables
# Las variables son contenedores de información y su correcto uso es fundamental para la semántica.

# Correcto: Nombres descriptivos y significativos
nombre_usuario = "Juan"
edad_usuario = 25
print("Nombre:", nombre_usuario)
print("Edad:", edad_usuario)

# Incorrecto: Nombres de variables no descriptivos
# a = "Juan"
# b = 25
# print(a, b)  # Menos comprensible

# Ejemplo 5: Errores comunes con variables
# Usar nombres de variables que no reflejan su contenido.
# Intentar utilizar palabras reservadas como nombres de variables.
# Iniciar nombres de variables con números.
# No declarar una variable antes de su uso.

# Incorrecto: Usar palabras reservadas
# if = 10  # 'if' es una palabra reservada en Python

# Incorrecto: Iniciar nombres de variables con números
# 1nombre = "Juan"  # Esto generará un error de sintaxis

# Incorrecto: No declarar una variable antes de su uso
# print(apellido)  # NameError: name 'apellido' is not defined

# Ejemplo 6: Redefinición de variables
# Redefinir una variable sobrescribirá su valor anterior.

valor = 10
print("Valor inicial:", valor)  # Salida: Valor inicial: 10

valor = 20
print("Valor redefinido:", valor)  # Salida: Valor redefinido: 20

# Ejemplo 7: Evitar errores de semántica al nombrar variables
# Usar nombres de variables que reflejen claramente su propósito.

# Correcto: Nombre de variable que refleja su propósito
nombre = "Juan"
edad = 25
print("Nombre:", nombre)
print("Edad:", edad)

# Incorrecto: Nombre de variable que no refleja su propósito
# x = "Juan"
# y = 25
# print(x, y)  # Menos claro y propenso a confusiones
