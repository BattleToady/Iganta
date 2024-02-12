import os
import datetime
import json

class Task():
    def __init__(self, name: str, description: str, tag: str, deadline: datetime, 
                 duration : datetime, difficulty: int, importance: int, period: datetime, 
                 creationdate: datetime, done : str):
        self.name = name
        self.description = description
        self.tag = tag
        self.deadline = deadline
        self.duration = duration
        self.difficulty = difficulty
        self.period = period
        self.importance = importance
        self.creationdate = creationdate
        self.done = done

class TaskLoader():
    DATA_PATH = '.\\data\\tasks'
    def __init__(self):
        self.tasks = TaskLoader.read()

    def read():
        if('tasks.json' not in os.listdir('.\\data')):
            with open('.\\data\\tasks.json', 'w') as file:
                json.dump([], file)
            return []
        else:
            with open('.\\data\\tasks.json', 'r') as file:
                return json.load(file)
            
    def save():
        with open('.\\data\\tasks.json', 'w') as file:
                json.dump(self.tasks, file)

    