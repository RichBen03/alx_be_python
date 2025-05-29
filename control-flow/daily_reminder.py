task = input("Enter your task: ")
time_bound = input("Is it time-bound? (yes/no): ")
priority = input("Priority (high/medium/low): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task but it is time-bound. Plan to complete it soon.")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Do it when your schedule allows.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task, but it's time-bound. Avoid procrastination.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
