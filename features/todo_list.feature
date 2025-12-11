Feature: To-Do List Manager
  The user can manage tasks by adding, listing, marking as completed, clearing tasks and more.

  Background:
    Given the to-do list is initialized

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      """
      Tasks:
      - Buy groceries (Media) [Pending]
      - Pay bills (Media) [Pending]
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task          | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed
    And the last operation message should contain "marcada como completada"

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty
    And the last operation message should contain "Lista vaciada"

  Scenario: Attempting to mark an unexisting task as completed
    Given the to-do list contains tasks:
      | Task |
      | Buy groceries |
    When the user marks task "Pay bills" as completed
    Then an error message "Error: Tarea 'Pay bills' no encontrada." should be shown
