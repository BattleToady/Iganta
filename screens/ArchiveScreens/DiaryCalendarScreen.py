from kivy.uix.screenmanager import Screen
from objects.Diary import Diary
from datetime import date
import calendar
from calendar import monthrange
from functools import partial
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.image import Image

diary = Diary()
EMOJI_NAME_TO_IMAGE = {
	'cool' : 'cool',
	'crying' : 'sad-2',
	'disgusting' : 'disgusting',
	'excited' : 'excited',
	'fear' : 'fear',
	'like' : 'like',
	'love' : 'love',
	'Oh' : 'oh',
	'sad' : 'sad',
	'silence' : 'silence',
	'sleepy' : 'sleepy',
	'smile-2' : 'very happy',
	'smile' : 'happy',
	'thoughtful' : 'thoughtful', 
	'tongue out' : 'tongue-out',
	'angry' : 'angry'
}

class DiaryCalendarScreen(Screen):
	def __init__(self,**kwargs):
		super(Screen, self).__init__(**kwargs)
		self.current_month = 0
		self.current_year = 0

		current_date = date.today()
		self.current_month = current_date.month
		self.current_year = current_date.year
		self.current_day = current_date.day

		self.selected_date = current_date

		self.buttons = []

		self.bind(size=self.on_size_changed)

	def on_size_changed(self, instance, value):
		self.upgrade_emoji()

	def upgrade_calendar(self):
		calendar_widget = self.ids.calendar
		self.buttons = []

		calendar_widget.clear_widgets()

		self.ids.month_name_id.text = calendar.month_abbr[self.current_month] + ' ' + str(self.current_year)

		weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
		for i in range(7):
			day_label = Label(text = weekdays[i])
			calendar_widget.add_widget(day_label)

		days_range = monthrange(self.current_year, self.current_month)

		for i in range(days_range[0]):
			none_label = Label(text = '')
			calendar_widget.add_widget(none_label)

		for i in range(1, days_range[1] + 1):
			
			emoji_image = None
			if(i == self.current_day):
				if((self.current_month == date.today().month) and (self.current_year == date.today().year)):
					day_button = Button(text = str(i), background_color =(0.1, 0.8, 0.1, 1))
					if(diary.get_record(str(i) + '-' + str(self.current_month) + '-' + str(self.current_year)) is not None):
						record = diary.get_record(str(i) + '-' + str(self.current_month) + '-' + str(self.current_year))
						day_button = Button(text = str(i), background_color =(0.8, 0.8, 0.1, 1))
						if(record['emoji'] != ''):
							src = 'icons\\emoji\\' + EMOJI_NAME_TO_IMAGE[record['emoji']] + '.png'
							emoji_image = Image(source = src)
							day_button.add_widget(emoji_image)
					
			else:
				if(diary.get_record(str(i) + '-' + str(self.current_month) + '-' + str(self.current_year)) is not None):
					record = diary.get_record(str(i) + '-' + str(self.current_month) + '-' + str(self.current_year))
					day_button = Button(text = str(i), background_color =(0.8, 0.8, 0.1, 1))
					if(record['emoji'] != ''):
						src = 'icons\\emoji\\' + EMOJI_NAME_TO_IMAGE[record['emoji']] + '.png'
						emoji_image = Image(source = src)
						day_button.add_widget(emoji_image)
				else:
					day_button = Button(text = str(i))
			calendar_widget.add_widget(day_button)
			
			day_button.bind(on_press = partial(self.day_button_press, i))
			self.buttons.append(day_button)
			self.upgrade_emoji()

	def upgrade_emoji(self):
		for but in self.buttons:
			for child in but.children:
				if(isinstance(child, Image)):
					child.size = (but.height*3/4, but.height*3/4)
					child.pos = (but.x+self.width/256, but.y + but.height/8)

	def turn_left(self):
		self.current_month -= 1

		if(self.current_month < 1):
			self.current_year -= 1
			self.current_month = 12
		elif(self.current_month > 12):
			self.current_year += 1
			self.current_month = 1

		self.upgrade_calendar()

	def turn_right(self):
		self.current_month += 1

		if(self.current_month < 1):
			self.current_year -= 1
			self.current_month = 12
		elif(self.current_month > 12):
			self.current_year += 1
			self.current_month = 1

		self.upgrade_calendar()
		
	def set_date_current(self):
		current_date = date.today()
		self.current_month = current_date.month
		self.current_year = current_date.year
		self.upgrade_calendar()

	def day_button_press(self, day, button):
		
		self.selected_date = date(self.current_year, self.current_month, day)

		self.ids.ChoosenDateLabel.text = str(self.selected_date.day) + '-' + calendar.month_abbr[self.selected_date.month] + ' ' + str(self.selected_date.year) + ':'

		if(diary.get_record(str(self.selected_date.day) + '-' + str(self.selected_date.month) + '-' + str(self.selected_date.year)) is not None):
			self.ids.RecordTextField.text = diary.get_record(str(self.selected_date.day) + '-' + str(self.selected_date.month) + '-' + str(self.selected_date.year))['text']
		else:
			self.ids.RecordTextField.text = ''
		
		for but in self.buttons:
			but.background_color = (0.95, 0.95, 0.95, 1)
			if(diary.get_record(but.text + '-' + str(self.current_month) + '-' + str(self.current_year)) is not None):
				but.background_color = (0.8, 0.8, 0.1, 1)
				
			if((but.text == str(self.current_day)) and (self.current_month == date.today().month) and (self.current_year == date.today().year)):
				but.background_color = (0.1, 0.8, 0.1, 1)
			
		button.background_color  = (0.1, 0.7, 0.7, 1)
		App.get_running_app().diary_selected_date = str(self.selected_date.day) + '-' + str(self.selected_date.month) + '-' + str(self.selected_date.year)