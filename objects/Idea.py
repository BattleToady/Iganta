import datetime

class Idea():
    def __init__(self, name: str, description: str, tag: str, deadline: datetime, 
                 duration : datetime, difficulty: int, importance: int, period: datetime, done : str):
        self.name = name
        self.description = description
        self.tag = tag
        self.deadline = deadline
        self.duration = duration
        self.difficulty = difficulty
        self.period = period
        self.importance = importance
        self.done = done