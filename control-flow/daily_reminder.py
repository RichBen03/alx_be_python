task = input("Enter a task description: ")
priority = input("What's the tasks priority?(high,medium,low) ")
time_bound = input("Is the task time bound? (yes/no) ")

match priority:
    case "high":
        if time_bound== "yes":
                print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
             print(f"Reminder: {task} is a high priority task find time and do it!")
    case "medium":
          if time_bound == "yes":
               print(f"Reminder: {task} is a medium priorty task but is time-bound please find time and complete it")
          else:
               print(f"Reminder: {task} is a medium priority task, find time to do it ")
    case "low":
          if time_bound == "yes":
               print(f"Reminder: {task} is of low priority but kindly remember to do it on time, avoid procastination")
          else:
               print(f"Reminder: {task} is a low priority task. Consider completing it when you have free time.")