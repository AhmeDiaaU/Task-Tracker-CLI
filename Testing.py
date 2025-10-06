# test_runner.py
import os
import json
import Task_manager  # Use the lowercase name

def run_all_tests():
    """Runs a complete suite of tests on the task manager functions."""
    print("--- 🧪 Starting Task Manager Tests 🧪 ---\n")

    # 1. SETUP: Ensure a clean slate before starting
    if os.path.exists(Task_manager.TASKS_FILE):
        os.remove(Task_manager.TASKS_FILE)
        print("🧹 Cleaned up old tasks.json file.")

    # 2. TEST ADD FUNCTION
    print("\n▶️  TEST 1: Adding tasks...")
    Task_manager.add_task("Buy groceries")
    Task_manager.add_task("Finish the project report")
    
    # 3. TEST LIST FUNCTION
    print("\n▶️  TEST 2: Listing all tasks...")
    Task_manager.list_all_tasks()

    # 4. TEST UPDATE FUNCTION
    print("\n▶️  TEST 3: Updating a task...")
    Task_manager.update_task(1, "Buy groceries and milk")
    print("Updated task 1. Current tasks:")
    Task_manager.list_all_tasks()

    # 5. TEST STATUS FUNCTION
    print("\n▶️  TEST 4: Updating task statuses...")
    Task_manager.task_status(1, "in-progress")
    Task_manager.task_status(2, "done")
    Task_manager.task_status(1, "waiting")  # Test invalid status
    print("Updated statuses. Current tasks:")
    Task_manager.list_all_tasks()

    # 6. TEST DELETE FUNCTION
    print("\n▶️  TEST 5: Deleting a task...")
    Task_manager.delete_task(1)
    
    # Verification step
    remaining_tasks = Task_manager.load_tasks()
    if len(remaining_tasks) == 1 and remaining_tasks[0]['id'] == 2:
        print("✅ TEST PASSED: Task deletion was successful.")
    else:
        print("❌ TEST FAILED: Task was not deleted correctly from the file.")
        print(f"   Expected 1 task to remain, but found {len(remaining_tasks)}.")
    
    print("\nFinal tasks in file after delete attempt:")
    Task_manager.list_all_tasks()

    # 7. TEST EDGE CASES
    print("\n▶️  TEST 6: Testing edge cases...")
    print("Attempting to delete a non-existent task:")
    Task_manager.delete_task(99)  # Should print "not found"
    
    print("\n--- 🏁 All Tests Finished 🏁 ---")

if __name__ == "__main__":
    run_all_tests()