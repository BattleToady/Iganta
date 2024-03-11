from kivy.app import App
from kivy.uix.screenmanager import ScreenManager		
from kivy.lang import Builder
from MenuScreen import MenuScreen
from screens.DailyRoutineScreens.DailyRoutineScreen import DailyRoutineScreen
from screens.StrategicGoalsScreen import StrategicGoalsScreen
from screens.DailyRoutineScreens.ToDoListScreen import ToDoListScreen
from screens.IdeaBucketScreen.IdeaBucketScreen import IdeaBucketScreen
from screens.ArchiveScreens.DiaryCalendarScreen import DiaryCalendarScreen
from screens.ArchiveScreens.DiaryPageScreen import DiaryPageScreen
from objects.Task import TaskLoader

Builder.load_file('MenuScreen.kv')
Builder.load_file('.\screens\DailyRoutineScreens\DailyRoutineScreen.kv') 
Builder.load_file('.\screens\StrategicGoalsScreen.kv') 
Builder.load_file('.\screens\DailyRoutineScreens\ToDoListScreen.kv') 
Builder.load_file('.\screens\IdeaBucketScreen\IdeaBucketScreen.kv') 
Builder.load_file('.\screens\ArchiveScreens\DiaryCalendarScreen.kv')
Builder.load_file('.\screens\ArchiveScreens\DiaryPageScreen.kv')

class igantaApp(App):
	taskLoader = TaskLoader()
	
	def build(self):
	
		sm = ScreenManager()
		sm.add_widget(MenuScreen(name = 'MenuScreen'))
		sm.add_widget(ToDoListScreen(name = 'ToDoListScreen'))
		sm.add_widget(IdeaBucketScreen(name = 'IdeaBucketScreen'))
		sm.add_widget(DiaryCalendarScreen(name = 'DiaryCalendarScreen'))
		sm.add_widget(DiaryPageScreen(name = 'DiaryPageScreen'))
		return sm

if __name__ == '__main__':
    igantaApp().run()