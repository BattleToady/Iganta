from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen		
from kivy.lang import Builder
from MenuScreen import MenuScreen
from screens.DailyRoutineScreen import DailyRoutineScreen
from screens.StrategicGoalsScreen import StrategicGoalsScreen

Builder.load_file('MenuScreen.kv') 
Builder.load_file('.\screens\DailyRoutineScreen.kv') 
Builder.load_file('.\screens\StrategicGoalsScreen.kv') 

class igantaApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(MenuScreen(name = 'MenuScreen'))
		sm.add_widget(DailyRoutineScreen(name = 'DailyRoutineScreen'))
		sm.add_widget(StrategicGoalsScreen(name = 'StrategicGoalsScreen'))
		return sm

if __name__ == '__main__':
    igantaApp().run()