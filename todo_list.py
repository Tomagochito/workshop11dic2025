"""
Módulo de lógica de negocio para la gestión de tareas.

Este módulo define las estructuras de datos (Task) y el controlador principal
(ToDoList) para administrar el ciclo de vida de las tareas.
"""

class Task:
    """
    Representa una unidad de trabajo o tarea individual.
    """

    def __init__(self, name, priority="Media", category="General"):
        """
        Inicializa una nueva tarea con los atributos requeridos.

        Args:
            name (str): El nombre o descripción de la tarea.
            priority (str): Nivel de prioridad (ej. Alta, Media, Baja).
            category (str): Categoría de la tarea.
        """
        self.name = name
        self.status = "Pending"
        self.priority = priority
        self.category = category

    def __str__(self):
        """
        Retorna una representación legible de la tarea para la consola.
        """
        return f"{self.name} | P: {self.priority} | Est: {self.status}"


class ToDoList:
    """
    Clase controladora que gestiona la colección de tareas.
    Permite agregar, listar, completar y eliminar elementos.
    """

    def __init__(self):
        """Inicializa una lista de tareas vacía."""
        self.tasks = []

    def add_task(self, name, priority="Media"):
        """
        Crea una instancia de Task y la añade a la lista.

        Args:
            name (str): Nombre de la tarea.
            priority (str, opcional): Prioridad. Por defecto es "Media".

        Returns:
            str: Mensaje de confirmación.
        """
        new_task = Task(name, priority=priority)
        self.tasks.append(new_task)
        return f"Tarea '{name}' agregada."

    def list_tasks(self):
        """
        Genera un reporte en texto de todas las tareas actuales.

        Returns:
            str: Cadena con el listado de tareas o mensaje de lista vacía.
        """
        if not self.tasks:
            return "La lista está vacía."
        
        output = "Tasks:"
        for task in self.tasks:
            output += f"\n- {task.name} ({task.priority}) [{task.status}]"
        return output

    def mark_completed(self, task_name):
        """
        Busca una tarea por nombre y actualiza su estado a 'Completed'.

        Args:
            task_name (str): Nombre exacto de la tarea a buscar.

        Returns:
            str: Mensaje de éxito o error si no se encuentra.
        """
        for task in self.tasks:
            if task.name == task_name:
                task.status = "Completed"
                return "marcada como completada"
        return f"Error: Tarea '{task_name}' no encontrada."

    def clear_list(self):
        """
        Elimina todas las tareas de la lista.

        Returns:
            str: Mensaje de confirmación.
        """
        self.tasks = []
        return "Lista vaciada"

    def get_task(self, task_name):
        """
        Método auxiliar para recuperar un objeto Task.
        Útil para pruebas y verificaciones internas.

        Args:
            task_name (str): Nombre de la tarea.

        Returns:
            Task | None: El objeto tarea si existe, None si no.
        """
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None

    def delete_task(self, task_name):
        """
        Elimina una tarea específica de la lista basándose en su nombre.

        Args:
            task_name (str): Nombre de la tarea a eliminar.

        Returns:
            str: Mensaje indicando si la eliminación fue exitosa o no.
        """
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.name != task_name]
        
        if len(self.tasks) < initial_count:
            return f"Tarea '{task_name}' eliminada exitosamente."
        return f"Error: Tarea '{task_name}' no encontrada para eliminar."