task = input("Enter your task: ")
priority = input("Priority high/medium/low: ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        p=print("is high priority task.")
    case "medium":
        p=print("is medium priority task.")
    case "low":
        p=print("is low priority task.")
if time_bound == "yes":
    print(f"Reminder: '{task}' {p} that requires immediate attention today!")
elif time_bound == "no":
    print(f"Note: '{task}' {p} Consider completing it when you have free time.")
