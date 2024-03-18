from kivy.app import App
from kivy.uix.screenmanager import ScreenManager		
from kivy.lang import Builder
from MenuScreen import MenuScreen
from screens.DailyRoutineScreens.DailyRoutineScreen import DailyRoutineScreen
from screens.StrategicGoalsScreens.StrategicGoalsScreen import StrategicGoalsScreen
from screens.DailyRoutineScreens.ToDoListScreen import ToDoListScreen
from screens.IdeaBucketScreen.IdeaBucketScreen import IdeaBucketScreen
from screens.ArchiveScreens.DiaryCalendarScreen import DiaryCalendarScreen
from screens.ArchiveScreens.DiaryPageScreen import DiaryPageScreen
from objects.Task import TaskLoader
from datetime import date
from kivy.core.window import Window
from screens.StrategicGoalsScreens.SpheresOfLifeScreen import SpheresOfLifeScreen
from screens.StrategicGoalsScreens.FranklinPyramidScreen import FranklinPyramidScreen


Builder.load_file('MenuScreen.kv')
Builder.load_file('.\screens\DailyRoutineScreens\DailyRoutineScreen.kv') 
Builder.load_file('.\screens\StrategicGoalsScreens\StrategicGoalsScreen.kv') 
Builder.load_file('.\screens\DailyRoutineScreens\ToDoListScreen.kv') 
Builder.load_file('.\screens\IdeaBucketScreen\IdeaBucketScreen.kv') 
Builder.load_file('.\screens\ArchiveScreens\DiaryCalendarScreen.kv')
Builder.load_file('.\screens\ArchiveScreens\DiaryPageScreen.kv')
Builder.load_file('.\screens\StrategicGoalsScreens\SpheresOfLifeScreen.kv')
Builder.load_file('.\screens\StrategicGoalsScreens\FranklinPyramidScreen.kv')

class igantaApp(App):
	taskLoader = TaskLoader()
	
	def build(self):
		selected_date = date.today()
		
		App.get_running_app().diary_selected_date = str(selected_date.day) + '-' + str(selected_date.month) + '-' + str(selected_date.year)
		sm = ScreenManager()
		sm.add_widget(MenuScreen(name = 'MenuScreen'))
		sm.add_widget(ToDoListScreen(name = 'ToDoListScreen'))
		sm.add_widget(IdeaBucketScreen(name = 'IdeaBucketScreen'))
		sm.add_widget(DiaryCalendarScreen(name = 'DiaryCalendarScreen'))
		sm.add_widget(DiaryPageScreen(name = 'DiaryPageScreen'))
		sm.add_widget(SpheresOfLifeScreen(name = 'SpheresOfLifeScreen'))
		sm.add_widget(FranklinPyramidScreen(name = 'FranklinPyramidScreen'))
		return sm

if __name__ == '__main__':
    igantaApp().run()