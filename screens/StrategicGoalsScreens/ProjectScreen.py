from kivy.uix.screenmanager import Screen
from kivy.app import App
from objects.Project import ProjectReader
from kivy.uix.button import Button
from functools import partial

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
        self.upgrade_plan_layout()

    def text_input_changed(self):
        global selected_project
        reader.update_project(selected_project['id'], self.ids.name_input.text, self.ids.mark_input.text, self.ids.reason_input.text, self.ids.criteria_input.text)
        selected_project = reader.get_project(selected_project['id'])

    def upgrade_plan_layout(self):
        self.ids.plan_layout.clear_widgets()
        for phase in selected_project['phases']:
            phaseButton = Button(text = phase['name'])
            phaseButton.height = 60
            phaseButton.bind(on_press = partial(self.phase_button_clicked, phase['pos']))
            self.ids.plan_layout.add_widget(phaseButton)

    def phase_button_clicked(self, phase, button):
        pass

    def add_phase_button_clicked(self):
        global selected_project
        reader.add_phase(selected_project['id'], '', 0, '')
        selected_project = reader.get_project(selected_project['id'])
        self.upgrade_plan_layout()