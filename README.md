Here is a description formatted for a GitHub repository's `README.md` file, based on the code you provided.

-----

# Interactive Command-Line Task Manager

A simple yet powerful task management application that runs in your terminal. This tool uses an interactive, menu-driven interface to help you keep track of your tasks, with all data persistently stored in a local JSON file.

## Features

  * **Add New Tasks**: Quickly add new tasks with a description.
  * **List All Tasks**: View a formatted list of all your current tasks.
  * **Update Tasks**: Modify the description of an existing task using an interactive selection menu.
  * **Delete Tasks**: Remove tasks you no longer need from the list.
  * **Change Task Status**: Update a task's status with one of three valid options: `todo`, `in-progress`, or `done`.
  * **Interactive Interface**: Navigate and select tasks and options easily using arrow keys, powered by the `inquirer` library.
  * **Persistent Storage**: Your tasks are automatically saved to a `$tasks.json$` file, ensuring your data is not lost when the application closes.

## Project Structure

The application is designed with a clear separation of concerns, dividing the core logic from the user interface.

  * `$Task_manager.py$`: This file acts as the backend or logic layer. It handles all data manipulation (Create, Read, Update, Delete) and interacts directly with the `$tasks.json$` file.
  * `$Cli.py$`: This file serves as the frontend or user interface layer. It is responsible for all user interaction, displaying menus, and calling the appropriate backend functions to perform actions.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

  * Python 3.x
  * pip (Python package installer)

### Installation

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **Install dependencies:**
    The project uses the `inquirer` library to create the interactive command-line menus. Install it using pip:

    ```sh
    pip install inquirer
    ```

### Running the Application

To start the task manager, execute the `$Cli.py$` script from your terminal:

```sh
python Cli.py
```

You will be greeted with an interactive menu where you can begin managing your tasks.

## Data Model

Each task is stored as a JSON object in the `$tasks.json$` file with the following structure:

```json
{
    "id": 1,
    "description": "This is a sample task.",
    "status": "todo",
    "createdAt": "YYYY-MM-DDTHH:MM:SS.ffffff",
    "updatedAt": "YYYY-MM-DDTHH:MM:SS.ffffff"
}
```
