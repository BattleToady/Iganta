import os
import datetime
import json

class TaskLoader():
    DATA_PATH = '.\\data\\tasks'
    def __init__(self):
        self.read()

    def read(self):
        if('tasks.json' not in os.listdir('.\\data')):
            with open('.\\data\\tasks.json', 'w') as file:
                json.dump([], file)
            self.tasks = []
        else:
            with open('.\\data\\tasks.json', 'r') as file:
                self.tasks = json.load(file)
            
    def save(self):
        with open('.\\data\\tasks.json', 'w') as file:
            json.dump(self.tasks, file)

    def addTask(self, name, description, tag, deadline, duration, difficulty, importance, period, creationdate, done):
        with open('.\\data\\counters.json', 'r') as file:
            counter = json.load(file)
        id = counter['tasks']
        counter['tasks'] += 1
        with open('.\\data\\counters.json', 'w') as file:
            json.dump(counter, file)

        self.tasks.append(dict(
            id = id,
            name = name,
            description = description,
            tag = tag,
            deadline = deadline,
            duration = duration,
            difficulty = difficulty,
            importance = importance,
            period = period,
            creationdate = creationdate,
            done = done
        ))

        self.save()

    def find_task(self, task_id):
        for task in self.tasks:
            if(task['id'] == task_id):
                return task
            
    def delete_task(self, task_id: int):
        self.tasks.remove(self.find_task(task_id))
        self.save()

    def delete_task(self, task: dict):
        self.tasks.remove(task)
        self.save()

    def modify_task(self, changed_task):
        for task in self.tasks:
            if(task['id'] == changed_task['id']):
                task['name'] = changed_task['name']
                task['description'] = changed_task['description']
                task['duration'] = changed_task['duration']
                task['difficulty'] = changed_task['difficulty']
                task['deadline'] = changed_task['deadline']
                task['importance'] = changed_task['importance']
                task['period'] = changed_task['period']
                task['done'] = changed_task['done']

        self.save()