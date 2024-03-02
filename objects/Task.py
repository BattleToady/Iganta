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

        if('taskTags.json' not in os.listdir('.\\data')):
            with open('.\\data\\taskTags.json', 'w') as file:
                json.dump([], file)
            self.tags = []
        else:
            with open('.\\data\\taskTags.json', 'r') as file:
                self.tags = json.load(file)
            
    def save(self):
        with open('.\\data\\tasks.json', 'w') as file:
            json.dump(self.tasks, file)
        with open('.\\data\\taskTags.json', 'w') as file:
            json.dump(self.tags, file)

    def addTag(self, tag):
        self.tags.append(tag)
        self.save()

    def removeTag(self, tag):
        self.tags.remove(tag)
        self.save()
    
    def changeTag(self, tag, new_tag):
        for i in range(len(self.tags)):
            if(self.tags[i] == tag):
                self.tags[i] = new_tag
            
        for task in self.tasks:
            if(task['tag'] == tag):
                task['tag'] = new_tag

        self.save()

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