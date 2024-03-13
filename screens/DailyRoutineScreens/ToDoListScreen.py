from kivy.uix.screenmanager import Screen
from kivy.utils import get_color_from_hex
from objects.Task import TaskLoader
import math
from datetime import datetime
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from datetime import datetime
from objects.ToDoList import ToDoList
from kivy.app import App

from functools import partial

IMPORTANCE_SELECTED = 3
DIFFICULTY_SELECTED = 3
loader = TaskLoader()
todoList = ToDoList()
selected_task = None
selected_date = str(datetime.now().year) + '-' + str(datetime.now().strftime('%m')) + '-' + str(datetime.now().day)

class ToDoListScreen(Screen):
    def refreshTagPicker(self):
        self.ids.tag_spinner.values = loader.tags
        self.ids.tag_spinner.text = ''

        self.ids.tag_chooser_spinner.values = [''] + loader.tags
        self.ids.tag_chooser_spinner.text = ''

    def tag_select(self):
        print('tag selected')
        self.ids.tag_input.text = self.ids.tag_spinner.text

    def add_tag_button_clicked(self):
        tag_name = self.ids.tag_input.text
        loader.addTag(tag_name)
        self.cancel_tag_button_clicked()
        self.refreshTagPicker()

    def remove_tag_button_clicked(self):
        tag_name = self.ids.tag_spinner.text
        loader.removeTag(tag_name)
        self.cancel_tag_button_clicked()
        self.refreshTagPicker()

    def save_tag_button_clicked(self):
        tag_name = self.ids.tag_spinner.text
        new_tag_name = self.ids.tag_input.text
        loader.changeTag(tag_name, new_tag_name)
        self.cancel_tag_button_clicked()
        self.refreshTagPicker()

    def cancel_tag_button_clicked(self):
        self.ids.tag_input.text = ''
        self.ids.tag_spinner.text = ''

    

        

    def refreshDatePicker(self):
        self.ids.year_spinner.text = str(datetime.now().year)
        self.ids.year_spinner.values = [str(year) for year in range(datetime.now().year, datetime.now().year+5)]

        self.ids.month_spinner.text = str(datetime.now().strftime('%m'))
        self.ids.month_spinner.values = [datetime.strptime(str(i), '%m').strftime('%m') for i in range(1, 13)]

        self.ids.day_spinner.text = str(datetime.now().day)
        self.ids.day_spinner.values = [str(day) for day in range(1, 32)]

    def update_date_label(self):
        year = int(self.ids.year_spinner.text)
        month = datetime.strptime(self.ids.month_spinner.text, '%m').month
        
        days_in_month = (datetime(year, month % 12 + 1, 1) - datetime(year, month, 1)).days
        self.ids.day_spinner.values = []
        self.ids.day_spinner.values = [str(day) for day in range(1, days_in_month + 1)]
        day = int(self.ids.day_spinner.text)
        
        global selected_date
        selected_date = datetime(year, month, day).strftime('%Y-%m-%d')

    def fill_todo_list(self):
        self.ids.todo_list_layout.clear_widgets()
        global loader
        global todoList
        for task in loader.tasks:
            if(task['id'] in todoList.tasks):
                checkbox = CheckBox()
                self.ids.todo_list_layout.add_widget(checkbox)

                name_button = Button()
                name_button.text = task['name']
                name_button.bind(on_press = partial(self.task_button_clicked, task['id']))
                self.ids.todo_list_layout.add_widget(name_button)

                tag_label = Label()
                tag_label.text = task['tag']
                self.ids.todo_list_layout.add_widget(tag_label)

                importance_label = Label()
                importance_label.text = str(task['importance'])
                self.ids.todo_list_layout.add_widget(importance_label)

                difficulty_label = Label()
                difficulty_label.text = str(task['difficulty'])
                self.ids.todo_list_layout.add_widget(difficulty_label)

                duration_label = Label()
                duration_label.text = f'{task['duration'][0]}:{task['duration'][1]}'
                self.ids.todo_list_layout.add_widget(duration_label)

                deadline_label = Label()
                deadline_label.text = str(task['deadline'])
                self.ids.todo_list_layout.add_widget(deadline_label)

                add_button = Button()
                add_button.text = 'Remove'
                self.ids.todo_list_layout.add_widget(add_button)
                add_button.bind(on_press = partial(self.remove_from_list_button_clicked, task['id']))
    
    def fill_bucket_list(self):
        global loader
        for task in loader.tasks:
            checkbox = CheckBox()
            self.ids.layout_task_bucket.add_widget(checkbox)

            name_button = Button()
            name_button.text = task['name']
            name_button.bind(on_press = partial(self.task_button_clicked, task['id']))
            self.ids.layout_task_bucket.add_widget(name_button)

            tag_label = Label()
            tag_label.text = task['tag']
            self.ids.layout_task_bucket.add_widget(tag_label)

            importance_label = Label()
            importance_label.text = str(task['importance'])
            self.ids.layout_task_bucket.add_widget(importance_label)

            difficulty_label = Label()
            difficulty_label.text = str(task['difficulty'])
            self.ids.layout_task_bucket.add_widget(difficulty_label)

            duration_label = Label()
            duration_label.text = f'{task['duration'][0]}:{task['duration'][1]}'
            self.ids.layout_task_bucket.add_widget(duration_label)

            deadline_label = Label()
            deadline_label.text = str(task['deadline'])
            self.ids.layout_task_bucket.add_widget(deadline_label)

            add_button = Button()
            add_button.text = 'Add'
            self.ids.layout_task_bucket.add_widget(add_button)
            add_button.bind(on_press = partial(self.add_to_list_button_clicked, task['id']))

    def add_to_list_button_clicked(self, task_id, button):
        todoList.add_task(task_id)
        self.fill_todo_list()

    def remove_from_list_button_clicked(self, task_id, button):
        todoList.remove_task(task_id)
        self.fill_todo_list()

    def task_button_clicked(self, task_id, button):
        global loader
        global selected_task
        selected_task = loader.find_task(task_id)

        self.ids.textinputTask.text = selected_task['name']
        self.ids.textinputTaskDescription.text = selected_task['description']
        
        importance_buttons = [self.ids.button_importance_1, self.ids.button_importance_2, self.ids.button_importance_3, self.ids.button_importance_4, self.ids.button_importance_5]
        importance_buttons[selected_task['importance'] - 1].dispatch('on_press')

        difficiculty_buttons = [self.ids.button_difficulty_1, self.ids.button_difficulty_2, self.ids.button_difficulty_3, self.ids.button_difficulty_4, self.ids.button_difficulty_5]
        difficiculty_buttons[selected_task['difficulty'] - 1].dispatch('on_press')

        self.ids.slider_duration.value = selected_task['duration'][0] + 0.01*selected_task['duration'][1]*100/60

        self.ids.tag_chooser_spinner.text = selected_task['tag']

        self.togle_layout_visibility(True)

    def importance_button_clicked(self, importance, button):
        importance_buttons = [self.ids.button_importance_1, self.ids.button_importance_2, self.ids.button_importance_3, self.ids.button_importance_4, self.ids.button_importance_5]
        
        for importance_button in importance_buttons:
            importance_button.background_color = get_color_from_hex('#ff0000')

        button.background_color = get_color_from_hex('#00ff00')

        global IMPORTANCE_SELECTED
        IMPORTANCE_SELECTED = importance

    def togle_layout_visibility(self, pr):
        '''if(pr):
            self.ids.layout_add_task.visible = False
            self.ids.layout_add_task.opacity = 0
            self.ids.layout_add_task.size_x = 0
            self.ids.layout_add_task.height = 0

            self.ids.layout_task_modification.visible = True
            self.ids.layout_task_modification.opacity = 1
            self.ids.layout_task_modification.size_hint_x = 1
            self.ids.layout_task_modification.height = 25
        else:
            self.ids.layout_add_task.visible = True
            self.ids.layout_add_task.opacity = 1
            self.ids.layout_add_task.size_hint_x = 1
            self.ids.layout_add_task.height = 0

            self.ids.layout_task_modification.visible = False
            self.ids.layout_task_modification.opacity = 0
            self.ids.layout_task_modification.size_x = 0
            self.ids.layout_task_modification.height = 25'''

    def difficulty_button_clicked(self, difficulty, button):
        difficiculty_buttons = [self.ids.button_difficulty_1, self.ids.button_difficulty_2, self.ids.button_difficulty_3, self.ids.button_difficulty_4, self.ids.button_difficulty_5]
        
        for difficulty_button in difficiculty_buttons:
            difficulty_button.background_color = get_color_from_hex('#ff0000')

        button.background_color = get_color_from_hex('#00ff00')

        global DIFFICULTY_SELECTED
        DIFFICULTY_SELECTED = difficulty

    def clear_add_task_fields(self, widget):
        # Clearing checkbox and textinputs
        self.ids.checkboxAddListForward.checked = False
        self.ids.textinputTask.text = ''
        self.ids.textinputTaskDescription.text = ''

        # Clearing importance buttons
        importance_buttons = [self.ids.button_importance_1, self.ids.button_importance_2, self.ids.button_importance_4, self.ids.button_importance_5]
        
        for importance_button in importance_buttons:
            importance_button.background_color = get_color_from_hex('#ff0000')

        self.ids.button_importance_3.background_color = get_color_from_hex('#00ff00')
        global IMPORTANCE_SELECTED
        IMPORTANCE_SELECTED = 3

        # Clearing difficulty buttons
        difficiculty_buttons = [self.ids.button_difficulty_1, self.ids.button_difficulty_2, self.ids.button_difficulty_4, self.ids.button_difficulty_5]
        
        for difficulty_button in difficiculty_buttons:
            difficulty_button.background_color = get_color_from_hex('#ff0000')

        self.ids.button_difficulty_3.background_color = get_color_from_hex('#00ff00')

        global DIFFICULTY_SELECTED
        DIFFICULTY_SELECTED = 3

        # Clearing slider
        self.ids.slider_duration.value = 0
        self.ids.label_slider_value.text = '0:00'

    def slider_duration_value_changed(self, slider):
        frac, whole = math.modf(slider.value)
        frac_part = f'{frac*60/100:1.2f}'.replace('0.', '')
        self.ids.label_slider_value.text = f'{math.floor(whole)}:{frac_part}'

    def add_button_clicked(self, button):
        if(len(self.ids.textinputTask.text) == 0):
            return 1

        frac, whole = math.modf(self.ids.slider_duration.value)
        frac_part = f'{frac*60/100:1.2f}'.replace('0.', '')

        tag_name = self.ids.tag_chooser_spinner.text

        global selected_date
        global loader
        loader.addTask(
            name = self.ids.textinputTask.text,
            description = self.ids.textinputTaskDescription.text,
            tag = tag_name,
            deadline = selected_date,
            duration = (int(whole), int(frac_part)),
            difficulty = DIFFICULTY_SELECTED,
            importance = IMPORTANCE_SELECTED,
            period = None,
            creationdate = datetime.now().strftime('%Y-%m-%d'),
            done = False
        )

        self.clear_add_task_fields(self)
        self.ids.layout_task_bucket.clear_widgets()
        self.fill_bucket_list()

    def delete_button_clicked(self, button):
        global loader
        global selected_task
        loader.delete_task(selected_task)
        selected_task = None
        self.clear_add_task_fields(self)
        self.ids.layout_task_bucket.clear_widgets()
        self.fill_bucket_list()

    def save_button_clicked(self, button):
        if(len(self.ids.textinputTask.text) == 0):
            return 1

        frac, whole = math.modf(self.ids.slider_duration.value)
        frac_part = f'{frac*60/100:1.2f}'.replace('0.', '')

        tag_name = self.ids.tag_chooser_spinner.text

        global selected_task
        global selected_date
        selected_task['name'] = self.ids.textinputTask.text
        selected_task['description'] = self.ids.textinputTaskDescription.text
        selected_task['tag'] = tag_name
        selected_task['deadline'] = None
        selected_task['duration'] = (int(whole), int(frac_part))
        selected_task['difficulty'] = DIFFICULTY_SELECTED
        selected_task['deadline'] = selected_date
        selected_task['importance'] = IMPORTANCE_SELECTED
        selected_task['period'] = None
        selected_task['creationdate'] = datetime.now().strftime('%Y-%m-%d')
        
        global loader
        loader.modify_task(selected_task)
        self.ids.layout_task_bucket.clear_widgets()
        self.fill_bucket_list()
        self.fill_todo_list()