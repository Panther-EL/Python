#To-Do list

tasks = ['Praying','Sleeping','Bathing', 'Cooking','Learning', 'Gaming', 'Washing']

def show_tasks(tasks):  #Display all tasks
    for i in tasks:
        print(i)



def add_task(tasks):   #Add a new task
 new_task = input('Enter a new task: ')
 tasks.append(new_task)
 print(new_task)
    


def mark_done():    #Mark a task as completed
    user_input = input('Have you completed your task? Yes/No ')
    if user_input.lower() == 'yes':
        print('Done')
    else:
        print('Uncompleted')
        

#def delete_task():

# Actual Program
while True:
 print("--- To Do List Menu ---")
 options = ['1.View Tasks', '2.Add Task', '3.Mark Task as Done', '4.Delete Task', '5.Exit']
 for o in options:
    print(o)

 choice = input('Enter your choice:')
 if choice == '1':
    show_tasks(tasks)
 elif choice == '2':
    add_task(tasks)
 elif choice == '3':
    mark_done()
 elif choice == '5':
    break
