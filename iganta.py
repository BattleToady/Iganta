from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen		
from kivy.lang import Builder
from MenuScreen import MenuScreen
from screens.DailyRoutineScreens.DailyRoutineScreen import DailyRoutineScreen
from screens.StrategicGoalsScreen import StrategicGoalsScreen
from screens.DailyRoutineScreens.ToDoListScreen import ToDoListScreen
from objects.Task import TaskLoader

Builder.load_file('MenuScreen.kv') 
Builder.load_file('.\screens\DailyRoutineScreens\DailyRoutineScreen.kv') 
Builder.load_file('.\screens\StrategicGoalsScreen.kv') 
Builder.load_file('.\screens\DailyRoutineScreens\ToDoListScreen.kv') 


class igantaApp(App):
	taskLoader = TaskLoader()
	
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MenuScreen(name = 'MenuScreen'))
		sm.add_widget(DailyRoutineScreen(name = 'DailyRoutineScreen'))
		sm.add_widget(StrategicGoalsScreen(name = 'StrategicGoalsScreen'))
		sm.add_widget(ToDoListScreen(name = 'ToDoListScreen'))
		return sm

if __name__ == '__main__':
    igantaApp().run()