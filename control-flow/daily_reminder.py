# daily_reminder.py

def get_task():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound

def create_reminder(task, priority, time_bound):
    reminder = ""
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            reminder = f"'{task}' has an unknown priority level"
    
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."
    
    return reminder

def main():
    task, priority, time_bound = get_task()
    reminder = create_reminder(task, priority, time_bound)
    print(f"Reminder:{task}", reminder)

if name == "__main__":
    main
