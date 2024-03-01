from kivy.uix.screenmanager import Screen
from objects.Diary import Diary
from datetime import date
import calendar
from calendar import monthrange
from functools import partial
from kivy.uix.label import Label
from kivy.uix.button import Button

diary = Diary()

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
			
			if(i == self.current_day):
				if((self.current_month == date.today().month) and (self.current_year == date.today().year)):
					day_button = Button(text = str(i), background_color =(0.1, 0.8, 0.1, 1))
				else:
					day_button = Button(text = str(i))
			else:
				day_button = Button(text = str(i))
			calendar_widget.add_widget(day_button)
			day_button.bind(on_press = partial(self.day_button_press, i))
			self.buttons.append(day_button)

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

		#df = pd.read_csv('./data/diary.csv')
		#data = df[df.date == str(selected_date)]
		#if(len(data) != 0):
			#self.ids.RecordTextField.text = data.iloc[0]['record']
		#else:
			#self.ids.RecordTextField.text = ''

		self.ids.ChoosenDateLabel.text = str(self.selected_date.day) + '-' + calendar.month_abbr[self.selected_date.month] + ' ' + str(self.selected_date.year) + ':'
		
		for but in self.buttons:
			but.background_color = (0.95, 0.95, 0.95, 1)
			if((but.text == str(self.current_day)) and (self.current_month == date.today().month) and (self.current_year == date.today().year)):
				but.background_color = (0.1, 0.8, 0.1, 1)
		button.background_color  = (0.1, 0.7, 0.7, 1)