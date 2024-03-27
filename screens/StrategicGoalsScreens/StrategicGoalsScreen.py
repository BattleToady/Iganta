from kivy.uix.screenmanager import Screen
from objects.Project import ProjectReader
from kivy.uix.button import Button
from functools import partial
from kivy.app import App

projectReader = ProjectReader()

class StrategicGoalsScreen(Screen):
    def add_project_button_clicked(self):
        projectReader.create_project('', '', '', '')
        self.update_projects_layout()

    def update_projects_layout(self):
        for project in projectReader.projects:
            progress = 0
            for phase in project['phases']:
                phase_max_progress = phase['percent']
                done_tasks_count = 0
                tasks_count = 0
                for task in phase['tasks']:
                    tasks_count += 1
                    if(task['done']):
                        done_tasks_count += 1
                if(tasks_count != 0):
                    progress += phase_max_progress * (done_tasks_count/tasks_count)
            projectButton = Button(text = f'{project['name']}\n{progress:.1f}%')
            projectButton.height = 60
            projectButton.bind(on_press = partial(self.project_button_clicked, project['id']))
            self.ids.projectsLayout.add_widget(projectButton)

    def project_button_clicked(self, project_id, button):
        App.get_running_app().selected_project = project_id
        App.get_running_app().root.current = 'ProjectScreen'