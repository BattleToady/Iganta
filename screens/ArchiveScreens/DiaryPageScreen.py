from kivy.uix.screenmanager import Screen
from kivy.app import App
from objects.Diary import Diary

diary = Diary()

class DiaryPageScreen(Screen):
    def __init__(self,**kwargs):
        super(Screen, self).__init__(**kwargs)

    def on_page_enter(self):
        self.record = diary.get_record(App.get_running_app().diary_selected_date)
        if(self.record is None):
            self.record = {'date' : App.get_running_app().diary_selected_date, 'text': '', 'emoji':''}

        self.ids.DiaryPageTextInput.text = self.record['text']
        self.selected_emoji = self.record['emoji']
        self.ids.label_current_emoji.text = self.selected_emoji

    def back_button_pressed(self):
        self.save_record()

    def save_record(self):
        text = self.ids.DiaryPageTextInput.text

        if(diary.get_record(App.get_running_app().diary_selected_date) is None):
            diary.add_record(App.get_running_app().diary_selected_date, text, self.selected_emoji)
        else:
            diary.change_record(App.get_running_app().diary_selected_date, text, self.selected_emoji)

    def emoji_button_clicked(self, emoji):
        self.selected_emoji = emoji
        self.ids.label_current_emoji.text = emoji
        text = self.ids.DiaryPageTextInput.text
        diary.change_record(App.get_running_app().diary_selected_date, text, self.selected_emoji)