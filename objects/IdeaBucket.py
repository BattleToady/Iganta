import os
import json

class IdeaBucket():
    def __init__(self):
        if('ideaTags.json' not in os.listdir('.\\data')):
            with open('.\\data\\ideaTags.json', 'w') as file:
                json.dump([], file)
            self.tags = []
        else:
            with open('.\\data\\ideaTags.json', 'r') as file:
                self.tags = json.load(file)


        if('ideaBucket.json' not in os.listdir('.\\data')):
            with open('.\\data\\ideaBucket.json', 'w') as file:
                json.dump([], file)
            self.ideas = []
        else:
            with open('.\\data\\ideaBucket.json', 'r') as file:
                self.ideas = json.load(file)

    def add_tag(self, tag):
        for t in self.tags:
            if(t['name'] == tag['name']):
                print('This name is already exists!')
                return 1
            
        print(tag)
        if(tag not in self.tags):
            self.tags.append(tag)
            with open('.\\data\\ideaTags.json', 'w') as file:
                json.dump(self.tags, file)
    
    def add_idea(self, idea):
        for i in self.ideas:
            if(i['name'] == idea['name']):
                print('This name is already exists!')
                return 1
            
        if(idea not in self.ideas):
            self.ideas.append(idea)
            with open('.\\data\\ideaBucket.json', 'w') as file:
                json.dump(self.ideas, file)

    def remove_tag(self, tag_name):
        for tag in self.tags:
            if(tag['name'] == tag_name):
                self.tags.remove(tag)
                with open('.\\data\\ideaTags.json', 'w') as file:
                    json.dump(self.tags, file)
                break

    def remove_idea(self, idea):
        self.ideas.remove(idea)
        with open('.\\data\\ideaBucket.json', 'w') as file:
            json.dump(self.ideas, file)

    def change_tag(self, tag, new_name):
        for t in self.tags:
            if(t['name'] == new_name):
                print('This name is already exists!')
                return 1
            
        for t in self.tags:
            if(t['name'] == tag):
                for idea in self.ideas:
                    if(idea['tag'] == tag):
                        idea['tag'] = new_name
                with open('.\\data\\ideaBucket.json', 'w') as file:
                    json.dump(self.ideas, file)
                t['name'] = new_name
                with open('.\\data\\ideaTags.json', 'w') as file:
                    json.dump(self.tags, file)
                break
    
    def change_idea(self, idea, new_name, new_description, new_tag):
        for i in self.ideas:
            if((i['name'] == new_name) and (idea != new_name)):
                print('This name is already exists!')
                return 1
        
        for i in self.ideas:
            if(i['name'] == idea):
                i['name'] = new_name
                i['description'] = new_description
                i['tag'] = new_tag
                #i['new_tag'] = new_tag
                with open('.\\data\\ideaBucket.json', 'w') as file:
                    json.dump(self.ideas, file)
                break