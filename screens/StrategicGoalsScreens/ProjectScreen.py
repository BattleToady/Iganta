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
        self.ids.project_name_input.text = str(selected_project['name'])
        self.ids.project_mark_input.text = str(selected_project['mark'])
        self.ids.project_reason_input.text = str(selected_project['reason'])
        self.ids.project_criteria_input.text = str(selected_project['criteria'])
        self.upgrade_plan_layout()

    def project_changes_save(self):
        name = self.ids.project_name_input.text
        mark = self.ids.project_mark_input.text
        reason = self.ids.project_reason_input.text
        criteria = self.ids.project_criteria_input.text
        
        reader.update_project(selected_project['id'], name, mark, reason, criteria)

    def upgrade_plan_layout(self):
        for node in [i for i in self.ids.planTree.iterate_all_nodes()]:
            self.ids.planTree.remove_node(node)
        self.ids.planTree.bind(selected_node=self.on_node_selected)
        max_pos = 0
        for phase in selected_project['phases']:
            if(phase['pos'] > max_pos):
                max_pos = phase['pos']
        done_percent = 0
        for i in range(max_pos+1):
            for phase in selected_project['phases']:
                if(phase['pos'] == i):
                    phase_node = self.ids.planTree.add_node(TreeViewLabel(text=phase['name']))
                    phase_done_max_percent = phase['percent']

                    done_tasks_count = 0
                    max_task_pos = 0
                    for task in phase['tasks']:
                        if(task['pos'] > max_task_pos):
                            max_task_pos = task['pos']
                    for j in range(max_task_pos+1):
                        for task in phase['tasks']:
                            if(task['pos'] == j):
                                if task['done']:
                                    done_tasks_count += 1 
                                self.ids.planTree.add_node(TreeViewLabel(text=task['name']), phase_node)
                                continue
                    done_percent += phase_done_max_percent * (done_tasks_count / (max_task_pos + 1))
                    continue
        self.ids.project_progress_bar.value = done_percent
        self.ids.progress_label.text = f'{done_percent:.1f}%'
        
        self.ids.phase_percent_spinner.values = [str(2.5 * i) for i in range(41)]

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
                self.ids.phase_percent_spinner.text = str(self.selected_phase['percent'])
                self.ids.phase_criteria_input.text = self.selected_phase['criteria']
            else:
                self.ids.task_name_input.text = node.text
                self.selected_phase = reader.find_phase_by_name(selected_project['id'], parent_node.text)
                self.selected_task = reader.find_task_by_name(selected_project['id'], self.selected_phase['pos'], node.text)
                print(self.selected_task)
                self.ids.task_done_checkbox.active = self.selected_task['done']

    def deselect_node(self):
        #self.ids.planTree._selected_node.is_selected = False
        self.ids.planTree._selected_node = None
        self.ids.task_done_checkbox.active = False
        self.ids.phase_name_input.text = ''
        self.ids.task_name_input.text = ''

    def add_phase_button_clicked(self):
        global selected_project
        name = self.ids.task_name_input.text if self.ids.task_name_input.text != '' else ''
        reader.add_phase(selected_project['id'], name, 0, '')
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
        criteria = self.ids.phase_criteria_input.text
        percent = float(self.ids.phase_percent_spinner.text)
        reader.update_phase(selected_project['id'], self.selected_phase['pos'], name, criteria, percent)
        self.upgrade_plan_layout()
    
    def save_task_changes(self):
        name = self.ids.task_name_input.text
        done = self.ids.task_done_checkbox.active
        reader.update_task(selected_project['id'], self.selected_phase['pos'], self.selected_task['pos'], name, done)
        self.upgrade_plan_layout()

    def decrease_phase_pos(self):
        reader.change_phase_pos(selected_project['id'], self.selected_phase['pos'], False)
        self.upgrade_plan_layout()

    def increase_phase_pos(self):
        reader.change_phase_pos(selected_project['id'], self.selected_phase['pos'], True)
        self.upgrade_plan_layout()

    def decrease_task_pos(self):
        reader.change_task_pos(selected_project['id'], self.selected_phase['pos'], self.selected_task['pos'], False)
        self.upgrade_plan_layout()

    def increase_task_pos(self):
        reader.change_task_pos(selected_project['id'], self.selected_phase['pos'], self.selected_task['pos'], True)
        self.upgrade_plan_layout()