import inquirer
from Task_manager import (
    task_status,
    update_task,
    load_tasks,
    list_all_tasks,
    delete_task,
    add_task
)

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def handle_add_task():
    """Handles the logic for adding a new task."""
    description = input("Enter the task description: ")
    if description:
        add_task(description)

def handle_update_task():
    """Handles the logic for updating a task."""
    task_id = choose_task_from_list("Which task do you want to update?")
    if task_id:
        new_description = input("Enter the new description: ")
        if new_description:
            update_task(task_id, new_description)

def handle_delete_task():
    """Handles the logic for deleting a task."""
    task_id = choose_task_from_list("Which task do you want to delete?")
    if task_id:
        delete_task(task_id)

def handle_change_status():
    """Handles the logic for changing a task's status."""
    task_id = choose_task_from_list("Which task's status do you want to change?")
    if task_id:
        status_question = [
            inquirer.List(
                'new_status',
                message="Select the new status",
                choices=["todo", "in-progress", "done"],
            ),
        ]
        answer = inquirer.prompt(status_question)
        if answer:
            task_status(task_id, answer['new_status'])

def choose_task_from_list(message="Select a task"):
    """Lets the user select a task using arrow keys."""
    tasks = load_tasks()
    if not tasks:
        print(f"{Colors.YELLOW}No tasks to choose from.{Colors.RESET}")
        return None

    task_choices = [
        (f"[{task['status']}] {task['description']}", task['id'])
        for task in tasks
    ]

    questions = [
        inquirer.List('task_id', message=message, choices=task_choices),
    ]
    answers = inquirer.prompt(questions)
    return answers['task_id'] if answers else None

def main():
    """Main application loop."""
    print("Welcome to your Interactive Task Tracker!")
    
    actions = {
        "List all tasks": list_all_tasks,
        "Add a new task": handle_add_task,
        "Update a task": handle_update_task,
        "Delete a task": handle_delete_task,
        "Change a task's status": handle_change_status,
        "Exit": None
    }

    while True:
        action_question = [
            inquirer.List(
                'action',
                message=f"{Colors.GREEN}What would you like to do?{Colors.RESET}",
                choices=actions.keys(),
            ),
        ]
        
        try:
            answers = inquirer.prompt(action_question)
            if not answers:  # User pressed Ctrl+C
                break
            
            chosen_action = answers['action']
            
            if chosen_action == "Exit":
                break
            
            # Call the corresponding function
            action_function = actions[chosen_action]
            action_function()
        
        except KeyboardInterrupt:
            break
        
        input("\nPress Enter to return to the menu...")

    print(f"\n{Colors.YELLOW}Goodbye!{Colors.RESET}")

if __name__ == "__main__":
    main()