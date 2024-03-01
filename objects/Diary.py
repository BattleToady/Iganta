import os
import json

class Diary():
    def __init__(self):
        if('diary.json' not in os.listdir('.\\data')):
            with open('.\\data\\diary.json', 'w') as file:
                json.dump([], file)
            self.records = []
        else:
            with open('.\\data\\diary.json', 'r') as file:
                self.records = json.load(file)

    def add_record(self, date, text, emoji):
        record = dict()
        record['date'] = date
        record['text'] = text
        record['emoji'] = emoji

    