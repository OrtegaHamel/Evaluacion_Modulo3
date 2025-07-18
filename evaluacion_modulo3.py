# Lista para almacenar las tareas
tareas = []

# Agregar nueva tarea
def agregar_tarea():
    descripcion = input("Escribe la descripción de la tarea: ").strip()
    if descripcion:
        tarea = {"descripcion": descripcion, "completada": False}
        tareas.append(tarea)
        print("Tarea agregada correctamente.")
    else:
        print("La descripción no puede estar vacía.")

# Ver lista de tareas
def ver_tareas():
    if not tareas:
        print("No hay tareas registradas.")
        return
    print("\n--- Lista de Tareas ---")
    for i, tarea in enumerate(tareas, start=1):
        estado = "Completada" if tarea["completada"] else "Pendiente"
        print(f"{i}. {tarea['descripcion']} [{estado}]")

# Marcar tarea como completada
def marcar_completada():
    ver_tareas()
    if not tareas:
        return
    try:
        indice = int(input("Ingresa el número de la tarea a marcar como completada: "))
        if 1 <= indice <= len(tareas):
            tareas[indice - 1]["completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número.")

# Eliminar una tarea
def eliminar_tarea():
    ver_tareas()
    if not tareas:
        return
    try:
        indice = int(input("Ingresa el número de la tarea a eliminar: "))
        if 1 <= indice <= len(tareas):
            eliminada = tareas.pop(indice - 1)
            print(f"Tarea eliminada: {eliminada['descripcion']}")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Entrada no válida. Debes ingresar un número.")

# Mostrar el menú
def mostrar_menu():
    print("\n--- Gestor de Tareas ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

# Función principal
def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                agregar_tarea()
            elif opcion == 2:
                ver_tareas()
            elif opcion == 3:
                marcar_completada()
            elif opcion == 4:
                eliminar_tarea()
            elif opcion == 5:
                print("Saliendo del programa. Hasta luego.")
                break
            else:
                print("Opción no válida. Intenta nuevamente.")
        except ValueError:
            print("Por favor, ingresa un número válido (1 al 5).")


# Ejecutar programa
main()
