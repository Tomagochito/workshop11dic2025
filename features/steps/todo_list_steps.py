from behave import given, when, then
from todo_list import ToDoList

# ---------------------------------------------------
# Background
# ---------------------------------------------------
@given("the to-do list is initialized")
def step_initialize_list(context):
    context.todo = ToDoList()
    context.last_message = None
    context.output = None

# ---------------------------------------------------
# Helper: create tasks from table (handles optional Status column)
# ---------------------------------------------------
def _create_tasks_from_table(context):
    # Reset tasks
    context.todo.tasks = []
    for row in context.table:
        name = row["Task"]
        # add with default priority
        context.todo.add_task(name)
        # set status if provided in table
        if "Status" in row.headings and row["Status"]:
            t = context.todo.get_task(name)
            if t:
                t.status = row["Status"]

# ---------------------------
# Add task
# ---------------------------
@given("the to-do list is empty")
def step_empty_list(context):
    context.todo.tasks = []
    context.last_message = None

@when('the user adds a task "{task}"')
def step_add_task(context, task):
    context.last_message = context.todo.add_task(task)

@then('the to-do list should contain "{task}"')
def step_check_task_added(context, task):
    names = [t.name for t in context.todo.tasks]
    assert task in names, f"Expected '{task}' in {names}"

# ---------------------------
# List tasks
# ---------------------------
@given("the to-do list contains tasks:")
def step_given_tasks(context):
    _create_tasks_from_table(context)
    context.last_message = None

@when("the user lists all tasks")
def step_list_tasks(context):
    context.output = context.todo.list_tasks()

@then("the output should contain:")
def step_check_list_output(context):
    expected = context.text.strip()
    actual = context.output.strip()
    assert expected == actual, f"\nExpected:\n{expected}\n\nActual:\n{actual}"

# ---------------------------
# Mark completed
# ---------------------------
@when('the user marks task "{task}" as completed')
def step_mark_completed(context, task):
    context.last_message = context.todo.mark_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_check_completed(context, task):
    t = context.todo.get_task(task)
    assert t is not None, f"Tarea '{task}' no encontrada en la lista."
    assert t.status == "Completed", f"Tarea '{task}' no está Completed sino '{t.status}'"

@then('the last operation message should contain "{fragment}"')
def step_check_last_message_contains(context, fragment):
    assert context.last_message is not None, "No hay mensaje de la última operación"
    assert context.last_message == fragment, f"Mensaje esperado: '{fragment}', mensaje real: '{context.last_message}'"

# ---------------------------
# Clear list
# ---------------------------
@when("the user clears the to-do list")
def step_clear_list(context):
    context.last_message = context.todo.clear_list()

@then("the to-do list should be empty")
def step_check_empty(context):
    assert len(context.todo.tasks) == 0, f"Esperaba lista vacía, hay {len(context.todo.tasks)} elementos"

# ---------------------------
# Error message for failed mark
# ---------------------------
@then('an error message "{msg}" should be shown')
def step_error_message(context, msg):
    assert context.last_message == msg, f"Esperaba mensaje de error '{msg}', recibí '{context.last_message}'"
