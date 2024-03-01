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

	def upgrade_calendar(self):
		calendar_widget = self.ids.calendar

		calendar_widget.clear_widgets()

		self.ids.month_name_id.text = calendar.month_abbr[self.current_month] + ' ' + str(self.current_year)

		weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
		for i in range(7):
			day_label = Label(text = weekdays[i])
			calendar_widget.add_widget(day_label)

		days_range = monthrange(self.current_year, self.current_month)

		print(days_range)
		for i in range(days_range[0]):
			none_label = Label(text = '')
			calendar_widget.add_widget(none_label)

		for i in range(1, days_range[1] + 1):
			
			if(i == self.current_day):
				day_button = Button(text = str(i), background_color =(0.1, 0.8, 0.1, 1))
			else:
				day_button = Button(text = str(i))
			calendar_widget.add_widget(day_button)
			#day_button.bind(on_press = partial(self.day_button_press, i))

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