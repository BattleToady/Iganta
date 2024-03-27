import json
import os

class ProjectReader():
    def __init__(self):
        self.read()

    def read(self):
        if('projects.json' not in os.listdir('.\\data')):
            with open('.\\data\\projects.json', 'w') as file:
                json.dump([], file)
            self.projects = []
        else:
            with open('.\\data\\projects.json', 'r') as file:
                self.projects = json.load(file)

    def save(self):
        with open('.\\data\\projects.json', 'w') as file:
            json.dump(self.projects, file)

    def get_id(self):
        max_id = 0
        if(len(self.projects) != 0):
            for project in self.projects:
                if(project['id'] > max_id):
                    max_id = project['id']
            return max_id + 1
        else:
            return max_id
    
    def get_project(self, id):
        for project in self.projects:
            if(project['id'] == id):
                return project

    def create_project(self, name, mark, reason, criteria):
        if(name == ''):
            counter = 0
            pr = True
            while(pr):
                pr = False
                for project in self.projects:
                    pr = False
                    if(project['name'] == f'NewProject-{counter}'):
                        counter += 1
                        pr = True
                        continue
            name = f'NewProject-{counter}'
        self.projects.append({'id' : self.get_id(),'name' : name, 'mark' : mark, 'reason' : reason, 'criteria' : criteria, 'phases' : []})
        self.save()

    def update_project(self, id, name, mark, reason, criteria):
        project = self.get_project(id)
        project['name'] = name
        project['mark'] = mark
        project['reason'] = reason
        project['criteria'] = criteria
        self.save()

    def update_phase(self, project_id, phase_pos, name, criteria, percent):
        phase = self.get_phase(project_id, phase_pos)
        phase['name'] = name
        phase['criteria'] = criteria
        phase['percent'] = percent
        self.save()
    
    def update_task(self, project_id, phase_pos, task_pos, name, done):
        task = self.get_task(project_id, phase_pos, task_pos)
        task['name'] = name
        task['done'] = done
        self.save()

    def change_phase_pos(self, project_id, phase_pos, decr):
        project = self.get_project(project_id)
        max_pos = 0
        for phase in project['phases']:
            if(phase['pos'] > max_pos):
                max_pos = phase['pos']
        if(not decr):
            new_pos = phase_pos + 1
            if(new_pos > max_pos):
                return 1
        else:
            new_pos = phase_pos - 1
            if(new_pos < 0):
                return 1
        replaced_phase = self.get_phase(project_id, new_pos)
        moved_phase = self.get_phase(project_id, phase_pos)
        replaced_phase['pos'] = phase_pos
        moved_phase['pos'] = new_pos
        self.save()

    def change_task_pos(self, project_id, phase_pos, task_pos, decr):
        phase = self.get_phase(project_id, phase_pos)
        max_pos = 0
        for task in phase['tasks']:
            if(task['pos'] > max_pos):
                max_pos = task['pos']
        if(not decr):
            new_pos = task_pos + 1
            if(new_pos > max_pos):
                return 1
        else:
            new_pos = task_pos - 1
            if(new_pos < 0):
                return 1
        replaced_task = self.get_task(project_id, phase_pos, new_pos)
        moved_task = self.get_task(project_id, phase_pos, task_pos)
        replaced_task['pos'] = task_pos
        moved_task['pos'] = new_pos
        self.save()



    def get_task(self, project_id, phase_pos, task_pos):
        for project in self.projects:
            if(project['id'] == project_id):
                for phase in project['phases']:
                    if(phase['pos'] == phase_pos):
                        for task in phase['tasks']:
                            if(task['pos'] == task_pos):
                                return task

    def get_phase_pos(self, id):
        project = self.get_project(id)
        max_pos = 0
        if(len(project['phases']) != 0):
            for phase in project['phases']:
                if(phase['pos'] > max_pos):
                    max_pos = phase['pos']
            return max_pos + 1
        else:
            return max_pos
        
    def get_task_pos(self, project_id, phase_pos):
        phase = self.get_phase(project_id, phase_pos)
        max_pos = 0
        if(len(phase['tasks']) != 0):
            for task in phase['tasks']:
                if(task['pos'] > max_pos):
                    max_pos = task['pos']
            return max_pos + 1
        else:
            return max_pos

    def add_phase(self, project_id, name, percent, criteria):
        project = self.get_project(project_id)
        if(name == ''):
            counter = 0
            pr = True
            while(pr):
                pr = False
                for phase in project['phases']:
                    pr = False
                    if(phase['name'] == f'NewPhase-{counter}'):
                        counter += 1
                        pr = True
                        continue
            name = f'NewPhase-{counter}'
        
        project['phases'].append({'pos' : self.get_phase_pos(project_id), 'name' : name, 'percent' : percent, 'criteria' : criteria, 'tasks' : []})
        self.save()
    
    def find_phase_by_name(self, project_id, phase_name):
        project = self.get_project(project_id)
        for phase in project['phases']:
            if(phase['name'] == phase_name):
                return phase
            
    def find_task_by_name(self, project_id, phase_pos, task_name):
        project = self.get_project(project_id)
        for phase in project['phases']:
            if(phase['pos'] == phase_pos):
                for task in phase['tasks']:
                    if(task['name'] == task_name):
                        return task


    def get_phase(self, project_id, phase_pos):
        project = self.get_project(project_id)
        for phase in project['phases']:
            if(phase['pos'] == phase_pos):
                return phase

    def add_task(self, project_id, phase_pos, name):
        phase = self.get_phase(project_id, phase_pos)
        if(name == ''):
            for task in phase['tasks']:
                counter = 0
                pr = True
                while(pr):
                    pr = False
                    if(task['name'] == f'NewTask-{counter}'):
                        counter += 1
                        pr = True
                        continue
                name = f'NewTask-{counter}'
        phase['tasks'].append({'pos' : self.get_task_pos(project_id, phase_pos), 'name' : name, 'id' : None, 'done' : False})
        self.save()

    def remove_task(self, project_id, phase_pos, task_pos):
        phase = self.get_phase(project_id, phase_pos)
        for task in phase['tasks']:
            if(task['pos'] == task_pos):
                phase['tasks'].remove(task)
        self.save()

    def remove_phase(self, project_id, phase_pos):
        project = self.get_project(project_id)
        phase = self.get_phase(project_id, phase_pos)
        project['phases'].remove(phase)
        self.save()