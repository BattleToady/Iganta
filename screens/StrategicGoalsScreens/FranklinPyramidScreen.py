from kivy.uix.screenmanager import Screen
from objects.FranklinPyramid import Pyramid

pyramid = Pyramid()

class FranklinPyramidScreen(Screen):
	def update_piramid(self):
		
		self.ids.shortTermPlanTextInput.text = pyramid.pyramid["shortTermPlan"]
		self.ids.middleTermPlanTextInput.text = pyramid.pyramid["middleTermPlan"]
		self.ids.longTermPlanTextInput.text = pyramid.pyramid["longTermPlan"]
		self.ids.generalPlanTextInput.text = pyramid.pyramid["generalPlan"]
		self.ids.globalMarksTextInput.text = pyramid.pyramid["globalMarks"]
		self.ids.mainValuesTextInput.text = pyramid.pyramid["mainValues"]

	def textInputChanged(self):
		shortTermPlan = self.ids.shortTermPlanTextInput.text
		middleTermPlan = self.ids.middleTermPlanTextInput.text
		longTermPlan = self.ids.longTermPlanTextInput.text
		generalPlan = self.ids.generalPlanTextInput.text
		globalMarks = self.ids.globalMarksTextInput.text
		mainValues = self.ids.mainValuesTextInput.text
		pyramid.update(shortTermPlan, middleTermPlan, longTermPlan, generalPlan, globalMarks, mainValues)