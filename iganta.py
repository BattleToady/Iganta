from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen		


class igantaApp(App):
	def build(self):
		sm = ScreenManager()
		return sm

if __name__ == '__main__':
    igantaApp().run()