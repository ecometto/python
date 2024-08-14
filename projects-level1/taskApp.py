import datetime, random, json

with open('./data.json', 'r') as f:
    tasks = json.load(f)
     
separation = "*" * 20


def taskGenerator(id):
    day = random.randint(1,30)   
    data = {    
            "id":datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(id),
            "taskTitle": f"title for task {id}", 
            "taskDescription": f"Description for your task number {id}",
            "expirationDate": f"2024/08/{day}",
            "status": 1
          }
    tasks.append(data)
    
    
def create():
        data = {    
            "id":datetime.datetime.now().strftime("%Y%m%d%H%M%S")+"1",
            "taskTitle": input("Add a short title for the task: "), 
            "taskDescription": input("Add a large description for the task: "), 
            "expirationDate": input("Add the 'expiration date' for the task (Ex: '2024/08/15'): "), 
            "status": 1
          }
        tasks.append(data)
        

def readTasks(stat):
    if len(tasks) == 0:
        print ("There are not tasks to show")
    else:
        template=""
        for task in tasks:
            if task['status'] == stat:
                status = "Solved" if task['status'] == 0 else "Pending"
                taskData= f"\n {separation} \nTask ID:{task['id']} - Title:{task['taskTitle']} - ExpirationDate:{task['expirationDate']} - status\n "
                template += taskData
            elif stat == 555:
                status = "Solved" if task['status'] == 0 else "Pending"
                taskData= f"\n {separation} \nTask ID:{task['id']} - Title:{task['taskTitle']} - ExpirationDate:{task['expirationDate']} - {status}  \n "
                template += taskData

            
        if stat == 0:
            if len(template)>0:
                print("\nSOLVED TASKS:")
                print(template)
            else:
                print("\n *** There are not SOLVED TASK yet ***")
        elif stat == 1:
            if len(template)>0:
                print("\nPENDING TASKS:")
                print(template)
            else:
                print("\n *** There are not SOLVED TASK yet ***")
        else:
            if len(template)>0:
                print("\TASKS LIST ) Pending and Solved:")
                print(template)
            else:
                print("\n *** There are not TASK to show ****")


def readOne(id):
    text = ""
    for task in tasks:
        if task['id'] == id:
            status = "Solved" if task['status'] == 0 else "Pending"
            text +=f""" 
                    **********************************************
                    Task id: '{task['id']}':
                    Title of task: '{task['taskTitle']}'

                    Description:
                                '{task['taskDescription']}'
                                
                    Expiration date                     Task Status
                    '{task['expirationDate']}'                         '{status}'
                    ********************************************** """ 
    if len(text) > 0:
        print("\n"+text)
    else:
        print("\nTask ID was not found")        


def update(id):
    for task in tasks:
        count = 0
        if task['id'] == id:
            taskTitle = input("Add a short 'TITLE (or 'enter' to continue without modify): ")
            taskDescription = input("Add a large 'DESCRIPTION' (or 'enter' to continue without modify): ")
            expirationDate = input("Add the 'EXPIRATION DATE' (or 'enter' to continue without modify): ")
            
            if len(taskTitle)>0: 
                task['taskTitle'] = taskTitle

            if len(taskDescription)>0:     
                task['taskDescription'] = taskDescription

            if len(expirationDate)>0: 
                task['expirationDate'] = expirationDate

            count += 1
    
    if count == 0:
        print("Task cound´t be updated")
    else:
        print("Task updated successfully")


def delete(id):
    count = 0
    for task in tasks:
        if task['id'] == id:
            task['status'] = 0
            print(task['status'])
            count += 1
            
    if count == 0:
        print("Task cound´t be deleted")
    else:
        print("Task deleted successfully")
        

#Generating previous data
# for i in range(1,10):
#     taskGenerator(i)


#RUNNUNG THE PROGRAM:
chosenOption = "0"

while chosenOption != "8":
    print("""
    Options: 
    1- Create task
    2- Read ALL tasks
    3- Read Active tasks
    4- Read Solved tasks
    5- Read One task detail
    6- Update a task
    7- Delete a task
    8- Exit to the program
      """)

    chosenOption = input("Select an option: ")

    if chosenOption == "1":
        create()
        
    elif chosenOption == "2": # Pending
        readTasks(555)
        
    elif chosenOption == "3": # Solved
        readTasks(1)
        
    elif chosenOption == "4": # All
        readTasks(0)
        
    elif chosenOption == "5":
        taskId = input("Type the 'id' you want to see details: ")
        readOne(taskId)
        
    elif chosenOption == "6":
        taskId = input("Type the 'id' you want to edit: ")
        update(taskId)

    elif chosenOption == "7":
        taskId = input("Type the 'id' you want to delete: ")
        delete(taskId)
        
    elif chosenOption == "8":
        print("thanks for using 'TaskApp'. See you soon\n")
        with open('data.json', 'w') as f:
            json.dump(tasks, f, indent=4)
    
    else:
        print("You have typed an incorrect option. Please try again.")