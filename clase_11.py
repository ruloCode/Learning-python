# clase_11.py

# Resumen de la clase
"""
Los diccionarios en Python son una estructura que almacenan dos datos, la clave y el valor. 
Un ejemplo cotidiano es un diccionario físico donde buscamos el significado de una palabra 
y encontramos la palabra (clave) y su definición (valor). Veamos cómo se utilizan en código.
"""

# Ejemplo 1: Creación de un diccionario
# Iniciamos creando una variable llamada numbers y especificamos el uso de diccionarios utilizando llaves.
# Asignamos valores a las claves:
numbers = {1: "one", "2": "two", 3: "three"}
print("Diccionario numbers:", numbers)

# Ejemplo 2: Acceso a elementos de un diccionario
# Para consultar la información de una clave específica, utilizamos la indexación:
print("Valor asociado a la clave '2':", numbers["2"])

# Ejemplo 3: Eliminación de elementos de un diccionario
# Para eliminar un elemento, utilizamos la clave del mismo:
information = {"nombre": "Carlos", "edad": 25, "ciudad": "Lima"}
print("Diccionario information antes de eliminar:", information)
del information["edad"]
print("Diccionario information después de eliminar 'edad':", information)

# Ejemplo 4: Métodos para trabajar con diccionarios
# Podemos utilizar métodos propios de los diccionarios, como keys(), values(), e items():

# Obtener las claves
claves = information.keys()
print("Claves del diccionario information:", claves)

# Obtener los valores
valores = information.values()
print("Valores del diccionario information:", valores)

# Obtener los pares clave-valor
pares = information.items()
print("Pares clave-valor del diccionario information:", pares)

# Ejemplo 5: Creación de un diccionario de diccionarios
# Podemos crear una agenda de contactos usando diccionarios de diccionarios:
contactos = {
    "Camilo": {"apellido": "Florida", "altura": 1.7, "edad": 30},
    "Diego": {"apellido": "Antesana", "altura": 1.75, "edad": 32}
}

# Acceso a la información de un contacto específico
print("Información de Carla:", contactos["Camilo"])

# Ejemplo 6: Recorrer un diccionario de diccionarios
# Podemos recorrer el diccionario de contactos para mostrar toda la información:
print("\nAgenda de contactos:")
for nombre, datos in contactos.items():
    print(f"Nombre: {nombre}")
    print(f"Apellido: {datos['apellido']}")
    print(f"Altura: {datos['altura']} m")
    print(f"Edad: {datos['edad']} años")
    print()  # Espacio para separar contactos

# Ejemplo 7: Modificación de un diccionario
# Podemos agregar o modificar elementos en un diccionario:
contactos["Camilo"]["edad"] = 31  # Modificamos la edad de Carla
contactos["Maria"] = {"apellido": "Gomez", "altura": 1.68, "edad": 28}  # Agregamos un nuevo contacto

print("Agenda de contactos después de modificaciones:")
for nombre, datos in contactos.items():
    print(f"Nombre: {nombre}, Apellido: {datos['apellido']}, Altura: {datos['altura']} m, Edad: {datos['edad']} años")

# Ejemplo 8: Eliminación de un contacto
# Eliminamos un contacto del diccionario:
del contactos["Diego"]
print("\nAgenda de contactos después de eliminar a Diego:")
for nombre, datos in contactos.items():
    print(f"Nombre: {nombre}, Apellido: {datos['apellido']}, Altura: {datos['altura']} m, Edad: {datos['edad']} años")