import os
import json

class ToDoList():
    def __init__(self):
        if('todolist.json' not in os.listdir('.\\data')):
            with open('.\\data\\todolist.json', 'w') as file:
                json.dump([], file)
            self.tasks = []
        else:
            with open('.\\data\\todolist.json', 'r') as file:
                self.tasks = json.load(file)

    def add_task(self, id):
        if(id not in self.tasks):
            self.tasks.append(id)
            with open('.\\data\\todolist.json', 'w') as file:
                json.dump(self.tasks, file)

    def remove_task(self, id):
        self.tasks.remove(id)
        with open('.\\data\\todolist.json', 'w') as file:
            json.dump(self.tasks, file)