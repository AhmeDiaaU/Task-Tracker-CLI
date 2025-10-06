import json
import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file. If it doesn't exist or is empty, return an empty list."""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        # Handle both "not found" and "empty/invalid file" errors
        return []


def task_status(task_id , new_status):
    """make 3 valid choices of the status"""

    valid_status = ["todo" , "in-progress" , "done"]

    if new_status not in valid_status : 
        print(f"Error '{new_status}' is not valid status , use one of the following [todo , in-progress , done]")
        return False
    
    # load task from the file 
    tasks = load_tasks()

    task_found = False 

    for task in tasks : 
        if task["id"] == task_id :
            task['status'] = new_status
            task['updated_at'] = datetime.datetime.now().isoformat()
            task_found = True
            break
    if task_found : 
        with open(TASKS_FILE , 'w' , encoding="UTF-8") as f :
            json.dump(tasks , f , indent=4 , ensure_ascii=False)
            return True
        # if task is not founded we return this 
    print(f"Error: Task with ID {task_id} not found.")
    return False

def add_task(description):
    """Adds a new task with the given description."""
    # Get the current time as a string
    timestamp = datetime.datetime.now().isoformat()

    # Load existing tasks FIRST
    tasks = load_tasks()
    
    #  Generate the new ID based on the loaded tasks
    new_id = max([task['id'] for task in tasks]) + 1 if tasks else 1
    
    # Create the new task dictionary with consistent keys
    new_task = {
        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": timestamp,
        "updatedAt": timestamp
    }

    # 5. Add the new task to the list
    tasks.append(new_task)

    # 6. Save the updated list back to the file
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)
        
    print(f"✅ Task '{description}' was added successfully with ID {new_id}")

def update_task(task_id, new_description):
    """Finds a task by its ID and updates its description."""
    
    tasks = load_tasks()
    task_found = False

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            # Convert the datetime object to a string before saving
            task["updatedAt"] = datetime.datetime.now().isoformat()
            task_found = True
            break
            
    if task_found:
        with open(TASKS_FILE, 'w', encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
        return True    
    return False

def delete_task(task_id):
    # get tasks from file
    tasks = load_tasks()
    # get total tasks in my file 
    total_tasks = len(tasks)
    #keep tasks i want only
    tasks_to_keep = [task for task in tasks if task['id'] != task_id]

    if len(tasks_to_keep) < total_tasks : 
        
        with open(TASKS_FILE , 'w' , encoding="utf-8") as f :
            json.dump(tasks , f , indent=4 , ensure_ascii=False)
        print(f"task {task_id} has been sucessfully deleted")

        return True
    else : 
        print(f"task with id {task_id} is not founded")
        return False
    
def list_all_tasks():
    """Loads and prints all tasks in a readable format."""
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return

    print("--- All Tasks ---")
    for task in tasks:
        print(f"  ID: {task['id']} | Status: {task['status']}")
        print(f"  Description: {task['description']}\n")


def list_done_tasks():
    """Loads and prints all tasks in a readable format."""
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return

    print("--- Done Tasks ---")
    for task in tasks:
        if task['status'] == 'done' :
            print(f"  ID: {task['id']} | Status: {task['status']} | Created At : {task['created_at']}")
            print(f"  Description: {task['description']}\n")


def list_progress_tasks():
    """Loads and prints all tasks in a readable format."""
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return

    print("--- in progress Tasks ---")
    for task in tasks:
        if task['status'] == 'in progress' :
            print(f"  ID: {task['id']} | Status: {task['status']}")
            print(f"  Description: {task['description']}\n")

def list_todo_tasks():
    """Loads and prints all tasks in a readable format."""
    tasks = load_tasks()
    
    if not tasks:
        print("No tasks found.")
        return

    print("--- todo Tasks ---")
    for task in tasks:
        if task['status'] == 'todo' :
            print(f"  ID: {task['id']} | Status: {task['status']}")
            print(f"  Description: {task['description']}\n")
