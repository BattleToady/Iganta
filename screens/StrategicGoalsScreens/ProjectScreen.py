from kivy.uix.screenmanager import Screen
from kivy.app import App
from objects.Project import ProjectReader
from kivy.uix.button import Button
from functools import partial
from kivy.uix.treeview import TreeView, TreeViewLabel

reader = ProjectReader()
selected_project = None

class ProjectScreen(Screen):
    selected_phase = None
    selected_task = None

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
        for node in [i for i in self.ids.planTree.iterate_all_nodes()]:
            self.ids.planTree.remove_node(node)
        self.ids.planTree.bind(selected_node=self.on_node_selected)
        max_pos = 0
        for phase in selected_project['phases']:
            if(phase['pos'] > max_pos):
                max_pos = phase['pos']
        for i in range(max_pos+1):
            for phase in selected_project['phases']:
                if(phase['pos'] == i):
                    phase_node = self.ids.planTree.add_node(TreeViewLabel(text=phase['name']))

                    max_task_pos = 0
                    for task in phase['tasks']:
                        if(task['pos'] > max_task_pos):
                            max_task_pos = task['pos']
                    for j in range(max_task_pos+1):
                        for task in phase['tasks']:
                            if(task['pos'] == j):
                                self.ids.planTree.add_node(TreeViewLabel(text=task['name']), phase_node)
                                continue
                    continue

    def on_node_selected(self, treeview, node):
        self.selectedNode = node
        if node != self.ids.planTree.root:
            parent_node = None
            for child_node in self.ids.planTree.iterate_all_nodes():
                if node in child_node.nodes:
                    parent_node = child_node
                    break
            if(parent_node == self.ids.planTree.root):
                self.ids.phase_name_input.text = node.text
                global selected_project
                self.selected_phase = reader.find_phase_by_name(selected_project['id'], node.text)
            else:
                self.ids.task_name_input.text = node.text
                self.selected_task = reader.find_task_by_name(selected_project['id'], self.selected_phase['pos'], node.text)

    def add_phase_button_clicked(self):
        global selected_project
        reader.add_phase(selected_project['id'], '', 0, '')
        selected_project = reader.get_project(selected_project['id'])
        self.upgrade_plan_layout()

    def add_task_button_clicked(self):
        global selected_project
        name = self.ids.task_name_input.text if self.ids.task_name_input.text != '' else ''
        reader.add_task(selected_project['id'], self.selected_phase['pos'], name)
        self.upgrade_plan_layout()

    def remove_task_button_clicked(self):
        global selected_project
        reader.remove_task(selected_project['id'], self.selected_phase['pos'], self.selected_task['pos'])
        self.upgrade_plan_layout()

    def remove_phase_button_clicked(self):
        global selected_project
        reader.remove_phase(selected_project['id'], self.selected_phase['pos'])
        self.upgrade_plan_layout()
        
    def save_phase_changes(self):
        name = self.ids.phase_name_input.text
        reader.update_phase(selected_project['id'], self.selected_phase['pos'], name, '')
        self.upgrade_plan_layout()
    
    def save_task_changes(self):
        name = self.ids.task_name_input.text
        reader.update_task(selected_project['id'], self.selected_phase['pos'], self.selected_task['pos'], name)
        self.upgrade_plan_layout()

    def decrease_phase_pos(self):
        reader.change_phase_pos(selected_project['id'], self.selected_phase['pos'], False)
        self.upgrade_plan_layout()
    def increase_phase_pos(self):
        reader.change_phase_pos(selected_project['id'], self.selected_phase['pos'], True)
        self.upgrade_plan_layout()
    def decrease_task_pos(self):
        print(self.selected_task['pos'])
        reader.change_task_pos(selected_project['id'], self.selected_phase['pos'], self.selected_task['pos'], False)
        self.upgrade_plan_layout()
    def increase_task_pos(self):
        print(self.selected_task['pos'])
        reader.change_task_pos(selected_project['id'], self.selected_phase['pos'], self.selected_task['pos'], True)
        self.upgrade_plan_layout()