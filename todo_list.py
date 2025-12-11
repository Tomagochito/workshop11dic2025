# Archivo: todo_list.py

class Task:
    def __init__(self, name, priority="Media", category="General"):
        # Cumple requisito PDF Pag 7: Mínimo 4 atributos
        self.name = name
        self.status = "Pending"
        self.priority = priority
        self.category = category

    def __str__(self):
        return f"{self.name} | P: {self.priority} | Est: {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, priority="Media"):
        # Ahora pasamos la prioridad al crear la tarea
        new_task = Task(name, priority=priority)
        self.tasks.append(new_task)
        return f"Tarea '{name}' agregada."

    def list_tasks(self):
        if not self.tasks:
            return "La lista está vacía."
        
        # Formato solicitado
        output = "Tasks:"
        for task in self.tasks:
            # Agregué detalles visuales para probar mejor en consola
            output += f"\n- {task.name} ({task.priority}) [{task.status}]"
        return output

    def mark_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.status = "Completed"
                return f"Tarea '{task_name}' marcada como completada."
        return f"Error: Tarea '{task_name}' no encontrada."

    def clear_list(self):
        self.tasks = []
        return "Lista vaciada completamente."

    def get_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                return task
        return None

    # --- FUNCIONALIDAD EXTRA ---
    def delete_task(self, task_name):
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.name != task_name]
        
        if len(self.tasks) < initial_count:
            return f"Tarea '{task_name}' eliminada exitosamente."
        return f"Error: Tarea '{task_name}' no encontrada para eliminar."