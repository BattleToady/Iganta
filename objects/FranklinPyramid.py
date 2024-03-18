import json
import os

class Pyramid():
	def __init__(self):
		self.read()

	def read(self):
		if(os.path.isfile('.\\data\\franklinPyramid.json')):
			with open('.\\data\\franklinPyramid.json', 'r') as file:
				self.pyramid = json.load(file)
		else:
			self.pyramid = {
				"shortTermPlan" : "",
				"middleTermPlan" : "",
				"longTermPlan" : "",
				"generalPlan" : "",
				"globalMarks" : "",
				"mainValues" : ""}
			with open('.\\data\\franklinPyramid.json', 'w') as file:
				json.dump(self.pyramid, file)
			
	def update(self, shortTermPlan, middleTermPlan, longTermPlan, generalPlan, globalMarks, mainValues):
		self.pyramid['shortTermPlan'] = shortTermPlan
		self.pyramid['middleTermPlan'] = middleTermPlan
		self.pyramid['longTermPlan'] = longTermPlan
		self.pyramid['generalPlan'] = generalPlan
		self.pyramid['globalMarks'] = globalMarks
		self.pyramid['mainValues'] = mainValues
		with open('.\\data\\franklinPyramid.json', 'w') as file:
			json.dump(self.pyramid, file)