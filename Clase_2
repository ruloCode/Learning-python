# clase_2.py

# Resumen de la clase
"""
Entender cómo trabajar con las cadenas en Python es fundamental para la manipulación de textos y datos en muchos proyectos. 
Desde definir variables hasta aplicar métodos específicos, el uso de strings es una habilidad básica, pero poderosa, 
que se utiliza en áreas avanzadas como el procesamiento del lenguaje natural (NLP).
"""

# Ejemplo 1: Definición de cadenas
# Las cadenas se pueden definir con comillas simples, dobles o triples.

# Comillas simples
nombre_1 = 'Carli'
print("Comillas simples:", nombre_1)  # Salida: Carli

# Comillas dobles
nombre_2 = "Carli"
print("Comillas dobles:", nombre_2)  # Salida: Carli

# Comillas triples (útil para cadenas multilínea)
nombre_3 = '''Carli'''
print("Comillas triples:", nombre_3)  # Salida: Carli

# Ejemplo 2: Imprimir y verificar el tipo de dato
# Usamos print() para mostrar el valor y type() para verificar el tipo de dato.
print("Valor de nombre_1:", nombre_1)  # Salida: Carli
print("Tipo de dato de nombre_1:", type(nombre_1))  # Salida: <class 'str'>

# Ejemplo 3: Indexación de cadenas
# Las cadenas son colecciones ordenadas y accesibles por índices.
nombre = 'Carli'
print("Primer carácter:", nombre[0])  # Salida: C
print("Último carácter:", nombre[-1])  # Salida: i

# Ejemplo 4: Error al acceder a un índice fuera de rango
# Si intentas acceder a un índice que no existe, Python arrojará un IndexError.
try:
    print(nombre[20])  # Esto generará un IndexError
except IndexError as e:
    print("Error:", e)  # Salida: string index out of range

# Ejemplo 5: Concatenación de cadenas
# Puedes concatenar cadenas con el operador + y repetirlas con el operador *.
nombre = 'Carli'
apellido = 'Florida'
nombre_completo = nombre + ' ' + apellido
print("Nombre completo:", nombre_completo)  # Salida: Carli Florida

print("Repetir nombre 3 veces:", nombre * 3)  # Salida: CarliCarliCarli

# Ejemplo 6: Longitud de una cadena
# Usamos la función len() para obtener la longitud de una cadena.
print("Longitud de 'Carli':", len(nombre))  # Salida: 5

# Ejemplo 7: Métodos de cadenas
# Las cadenas tienen métodos como lower(), upper(), y strip().
texto = "  Hola, Mundo!  "
print("Texto en minúsculas:", texto.lower())  # Salida: hola, mundo!
print("Texto en mayúsculas:", texto.upper())  # Salida: HOLA, MUNDO!
print("Texto sin espacios en blanco al principio y al final:", texto.strip())  # Salida: Hola, Mundo!

# Ejemplo 8: Reemplazar texto en una cadena
# Usamos el método replace() para reemplazar partes de una cadena.
texto = "Hola, Carli"
nuevo_texto = texto.replace("Carli", "Mundo")
print("Texto reemplazado:", nuevo_texto)  # Salida: Hola, Mundo

# Ejemplo 9: Importancia de las cadenas en NLP
# En NLP, las cadenas se limpian y procesan para análisis avanzados.
texto_nlp = "  Este es un TEXTO de Ejemplo para NLP.  "
texto_limpio = texto_nlp.strip().lower().replace("ejemplo", "muestra")
print("Texto limpio para NLP:", texto_limpio)  # Salida: este es un texto de muestra para nlp.
