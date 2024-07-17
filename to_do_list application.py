import os
import json

class Task:
    def __init__(self, title, description, completed=False):
        self.title=title
        self.description=description
        self.completed=completed

    def __repr__(self):
        status="Completed" if self.completed else "Incomplete"
        return f"Title:{self.title}, Description:{self.description}, Status:{status}"
    

class TodoList:
    def __init__(self, filename="tasks.txt"):
        self.filename=filename
        self.tasks=self.load_tasks()

    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("No tasks available")
        else:
            for idx, task in enumerate(self.tasks):
                print(f"ID: {idx}, {task}")

    def mark_task(self, task_id, completed=True):
        try:
            self.tasks[task_id].completed=completed
            self.save_tasks()
        except IndexError:
            print("Invalid task ID")
        
    def delete_task(self, task_id):
        try:
            self.tasks.pop(task_id)
            self.save_tasks()
        except IndexError:
            print("Invalid Task ID")

    def save_tasks(self):
        with open(self.filename,'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    
    def load_tasks(self):
        if os.path.exists(self.filename):
            if os.path.getsize(self.filename) > 0:
                with open(self.filename, 'r') as file:
                    tasks_data = json.load(file)
                    return [Task(**task) for task in tasks_data]
            else:
                return []
        return []

def main():
    todo_list= TodoList()

    while True:
        print("\n1.Add Task")
        print("\n2.List Tasks")
        print("\n3.Mark Task as Complete")
        print("\n4.Mark Task as Incomplete")
        print("\n5.Delete Task")
        print("\n6.Exit")

        option=input("Choose an option")

        if option=='1':
            title= input("Enter Task Title")
            description= input("Enter Task Description:")
            todo_list.add_task(title, description)
        
        elif option=='2':
            todo_list.list_tasks()

        elif option=='3':
            task_id=int(input("Enter task ID to mark as complete:"))
            todo_list.mark_task(task_id, completed=True)

        elif option=='4':
            task_id=int(input("Enter task Id to mark as Incomplete:"))
            todo_list.mark_task(task_id, completed=False)
        
        elif option=='5':
            task_id=int(input("Enter Task id to delete"))
            todo_list.delete_task(task_id)

        elif option=='6':
            break
        else:
            print("Invalid Option, please try again")

if __name__=="__main__":
    main()