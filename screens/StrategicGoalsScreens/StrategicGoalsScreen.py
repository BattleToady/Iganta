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
            projectButton = Button(text = project['name'] + '\n' + '25%')
            projectButton.height = 60
            projectButton.bind(on_press = partial(self.project_button_clicked, project['id']))
            self.ids.projectsLayout.add_widget(projectButton)

    def project_button_clicked(self, project_id, button):
        App.get_running_app().selected_project = project_id
        App.get_running_app().root.current = 'ProjectScreen'