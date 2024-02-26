from kivy.uix.screenmanager import Screen
from objects.ToDoList import ToDoList
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from objects.Task import TaskLoader



class DailyRoutineScreen(Screen):

    def fill_todo_list(self):
        self.ids.todo_list_layout.clear_widgets()
        loader = TaskLoader()
        todoList = ToDoList()
        for task in loader.tasks:
            if(task['id'] in todoList.tasks):
                checkbox = CheckBox()
                self.ids.todo_list_layout.add_widget(checkbox)

                name_label = Label()
                name_label.text = task['name']
                self.ids.todo_list_layout.add_widget(name_label)

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
