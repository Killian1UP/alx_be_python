task = input("Enter your task: ")
priority = input("Priority high/medium/low: ")
time_bound = input("Is it time-bound? (yes/no): ")

p = "is high priority task."
q = "is medium priority task."
r = "is low priority task."

match priority:
    case "high":
        print("is high priority task.")
    case "medium":
        print("is medium priority task.")
    case "low":
        print("is low priority task.")
if time_bound == "yes" and priority == "high":
    print(f"Reminder: '{task}' {p} that requires immediate attention today!")
elif time_bound == "yes" and priority == "medium":
    print(f"Reminder: '{task}' {q} that requires immediate attention today!")
elif time_bound == "yes" and priority == "low":
    print(f"Reminder: '{task}' {r} that requires immediate attention today!")
elif time_bound == "no" and priority == "high":
    print(f"Note: '{task}' {p} Consider completing it when you have free time.")
elif time_bound == "no" and priority == "medium":
    print(f"Note: '{task}' {q} Consider completing it when you have free time.")
elif time_bound == "no" and priority == "low":
    print(f"Note: '{task}' {r} Consider completing it when you have free time.")
