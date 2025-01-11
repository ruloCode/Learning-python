# Diccionario para almacenar los usuarios
usuarios = {}
contador_id = 1  # Contador para generar IDs únicos

# Función para agregar un usuario
def agregar_usuario():
    global contador_id
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    categoria = input("Categoría: ")

    usuarios[contador_id] = {
        "id": contador_id,
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "categoria": categoria
    }
    print(f"Usuario agregado con ID: {contador_id}")
    contador_id += 1

# Función para visualizar la lista de usuarios
def ver_usuarios():
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        print("\nLista de usuarios:")
        print("-" * 60)
        print("| ID  | Nombre          | Apellido        | Email                 | Categoría   |")
        print("-" * 60)
        for id_usuario, datos in usuarios.items():
            print(f"| {datos['id']:<4} | {datos['nombre']:<15} | {datos['apellido']:<15} | {datos['email']:<20} | {datos['categoria']:<11} |")
        print("-" * 60)

# Función para eliminar un usuario por su ID
def eliminar_usuario():
    id_usuario = int(input("Ingrese el ID del usuario a eliminar: "))
    if id_usuario in usuarios:
        del usuarios[id_usuario]
        print(f"Usuario con ID {id_usuario} eliminado.")
        # Llamar recursivamente a agregar_usuario después de eliminar
        agregar_usuario()
    else:
        print(f"No se encontró un usuario con ID {id_usuario}.")

# Función para buscar usuarios por nombre o apellido
def buscar_usuario():
    busqueda = input("Ingrese nombre o apellido para buscar: ").lower()
    resultados = []

    for id_usuario, datos in usuarios.items():
        if busqueda in datos["nombre"].lower() or busqueda in datos["apellido"].lower():
            resultados.append(datos)

    if resultados:
        print("\nResultados de la búsqueda:")
        print("-" * 60)
        print("| ID  | Nombre          | Apellido        | Email                 | Categoría   |")
        print("-" * 60)
        for datos in resultados:
            print(f"| {datos['id']:<4} | {datos['nombre']:<15} | {datos['apellido']:<15} | {datos['email']:<20} | {datos['categoria']:<11} |")
        print("-" * 60)
    else:
        print("No se encontraron usuarios con ese nombre o apellido.")

# Función para actualizar un usuario por su ID
def actualizar_usuario():
    id_usuario = int(input("Ingrese el ID del usuario a actualizar: "))
    if id_usuario in usuarios:
        print(f"\nDatos actuales del usuario con ID {id_usuario}:")
        print("-" * 60)
        print("| ID  | Nombre          | Apellido        | Email                 | Categoría   |")
        print("-" * 60)
        datos = usuarios[id_usuario]
        print(f"| {datos['id']:<4} | {datos['nombre']:<15} | {datos['apellido']:<15} | {datos['email']:<20} | {datos['categoria']:<11} |")
        print("-" * 60)

        # Solicitar nuevos datos
        nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
        apellido = input("Nuevo apellido (dejar vacío para no cambiar): ")
        email = input("Nuevo email (dejar vacío para no cambiar): ")
        categoria = input("Nueva categoría (dejar vacío para no cambiar): ")

        # Actualizar solo los campos que no están vacíos
        if nombre:
            usuarios[id_usuario]["nombre"] = nombre
        if apellido:
            usuarios[id_usuario]["apellido"] = apellido
        if email:
            usuarios[id_usuario]["email"] = email
        if categoria:
            usuarios[id_usuario]["categoria"] = categoria

        print(f"Usuario con ID {id_usuario} actualizado.")
    else:
        print(f"No se encontró un usuario con ID {id_usuario}.")

# Menú principal
def menu():
    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Agregar usuario")
        print("2. Ver lista de usuarios")
        print("3. Eliminar usuario por ID")
        print("4. Buscar usuario por nombre o apellido")
        print("5. Actualizar usuario por ID")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_usuario()
        elif opcion == "2":
            ver_usuarios()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            buscar_usuario()
        elif opcion == "5":
            actualizar_usuario()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()