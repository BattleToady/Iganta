from kivy.uix.screenmanager import Screen
from kivy.app import App
from objects.Project import ProjectReader

reader = ProjectReader()
selected_project = None

class ProjectScreen(Screen):
    def pre_enter(self):
        global selected_project
        selected_project = reader.get_project(App.get_running_app().selected_project)
        self.ids.name_input.text = str(selected_project['name'])
        self.ids.mark_input.text = str(selected_project['mark'])
        self.ids.reason_input.text = str(selected_project['reason'])
        self.ids.criteria_input.text = str(selected_project['criteria'])

    def text_input_changed(self):
        reader.update_project(selected_project['id'], self.ids.name_input.text, self.ids.mark_input.text, self.ids.reason_input.text, self.ids.criteria_input.text)