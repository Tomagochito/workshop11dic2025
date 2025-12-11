"""
Módulo principal de la aplicación To-Do List Manager.

Este script sirve como punto de entrada (Entry Point) para la interfaz de línea
de comandos (CLI), permitiendo al usuario interactuar con la clase ToDoList
para gestionar sus tareas.
"""

import sys
from todo_list import ToDoList

def mostrar_menu():
    """
    Imprime en consola las opciones del menú principal.
    """
    print("\n" + "="*30)
    print("   TO-DO LIST MANAGER")
    print("="*30)
    print("1. Agregar tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Borrar TODA la lista")
    print("6. Salir")
    print("="*30)

def main():
    """
    Función principal que inicializa el sistema y ejecuta el bucle de eventos.
    
    Maneja la entrada del usuario y delega las acciones a la instancia
    de ToDoList.
    """
    try:
        mi_lista = ToDoList()
    except ImportError:
        print("Error crítico: No se encuentra el módulo 'todo_list' o la clase 'ToDoList'.")
        return

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-6): ")

        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            prioridad = input("Prioridad (Alta/Media/Baja) [Enter para Media]: ")
            
            if not prioridad:
                mi_lista.add_task(nombre)
            else:
                mi_lista.add_task(nombre, priority=prioridad)
            
            print(f"--> ¡Tarea '{nombre}' procesada!")

        elif opcion == "2":
            print("\n--- TUS TAREAS ---")
            print(mi_lista.list_tasks())

        elif opcion == "3":
            nombre = input("Escribe el nombre exacto de la tarea a completar: ")
            resultado = mi_lista.mark_completed(nombre)
            print(f"--> {resultado}")

        elif opcion == "4":
            nombre = input("Escribe el nombre exacto de la tarea a ELIMINAR: ")
            resultado = mi_lista.delete_task(nombre)
            print(f"--> {resultado}")

        elif opcion == "5":
            confirmar = input("¿Seguro que quieres borrar todo? (s/n): ")
            if confirmar.lower() == 's':
                print(f"--> {mi_lista.clear_list()}")
            else:
                print("--> Operación cancelada.")

        elif opcion == "6":
            print("Saliendo del sistema...")
            sys.exit()

        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()