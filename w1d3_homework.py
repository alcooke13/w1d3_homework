tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

#Print a list of uncompleted tasks
uncompleted_tasks = []
for task in tasks:
    if task["completed"] == False:
        uncompleted_tasks.append(task)
print(uncompleted_tasks)

#Print a list of completed tasks
completed_tasks = []
for task in tasks:
    if task["completed"] == True:
        completed_tasks.append(task)
print(completed_tasks)

#Print a list of all task descriptions
task_description = []
for task in tasks:
    task_description.append(task["description"])
print(task_description)

#Print a list of tasks where time_taken is at least a given time
long_tasks = []
for task in tasks:
    if task["time_taken"] > 20:
        long_tasks.append(task)
print(long_tasks)

#Print any task with a given description
def find_task(list, description):   
    given_description = None
    for task in list:
        if task["description"] == description:
            given_description = task
    return given_description
print(find_task(tasks, "Feed Cat"))

#Given a description update that task to mark it as complete.
def update_task(list, description):
    completed_task = None
    for task in list:
        if task["description"] == description:
            task["completed"] = True
            completed_task = task
    return completed_task
print(update_task(tasks, "Wash Dishes"))
    
#Add a task to the list
tasks.append({"description": "Mop Floor", "completed": True, "time_taken": 30})
#print(tasks)