# clase_6.py

# Resumen de la clase
"""
En Python, cuando trabajamos con proyectos que requieren interacción del usuario, es común 
solicitar datos como correo o contraseña para ejecutar acciones específicas. Este mismo 
enfoque es útil para entender la función input.
"""

# Ejemplo 1: Uso básico de input
# La función input permite recibir información del usuario desde la consola.
nombre = input("Ingrese su nombre: ")
print("Nombre ingresado:", nombre)

# Ejemplo 2: Solicitar múltiples datos
# Podemos solicitar varios datos y mostrarlos en pantalla.
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print("Nombre:", nombre)
print("Edad:", edad)

# Ejemplo 3: Tipo de dato devuelto por input
# El resultado de input es siempre un string, incluso si se ingresa un número.
name = input("Ingrese su nombre: ")
age = input("Ingrese su edad: ")
print("Tipo de dato de 'name':", type(name))  # Salida: <class 'str'>
print("Tipo de dato de 'age':", type(age))  # Salida: <class 'str'>

# Ejemplo 4: Conversión de tipo de dato (casting)
# Podemos convertir el resultado de input a otros tipos de datos, como int o float.
age = int(input("Ingrese su edad: "))
print("Edad como entero:", age)
print("Tipo de dato de 'age':", type(age))  # Salida: <class 'int'>

# Ejemplo 5: Conversión a flotante
# También podemos convertir a flotante si esperamos números decimales.
altura = float(input("Ingrese su altura en metros: "))
print("Altura ingresada:", altura)
print("Tipo de dato de 'altura':", type(altura))  # Salida: <class 'float'>

# Ejemplo 6: Manejo de errores con casting
# Si el usuario ingresa un dato inesperado, se produce un ValueError.
try:
    edad = int(input("Ingrese su edad: "))
    print("Edad ingresada:", edad)
except ValueError:
    print("Error: Debe ingresar un número entero válido.")

# Ejemplo 7: Solicitar y validar un número entero
# Podemos usar un bucle para asegurarnos de que el usuario ingrese un número válido.
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        break  # Salir del bucle si la conversión es exitosa
    except ValueError:
        print("Error: Debe ingresar un número entero válido. Intente nuevamente.")
print("Edad ingresada:", edad)

# Ejemplo 8: Solicitar y validar un número flotante
# Similar al ejemplo anterior, pero para números flotantes.
while True:
    try:
        altura = float(input("Ingrese su altura en metros: "))
        break  # Salir del bucle si la conversión es exitosa
    except ValueError:
        print("Error: Debe ingresar un número válido. Intente nuevamente.")
print("Altura ingresada:", altura)

# Ejemplo 9: Combinar input con operaciones matemáticas
# Podemos usar el resultado de input directamente en operaciones matemáticas.
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    suma = num1 + num2
    print("La suma es:", suma)
except ValueError:
    print("Error: Debe ingresar números válidos.")
