from objects.SpheresOfLife import Spheres
import math
from kivy.uix.screenmanager import Screen
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from functools import partial

spheresObj = Spheres()

class SpheresOfLifeScreen(Screen):
	def SpheresOfLifeScreenPreEnter(self):
		pass

	def rebuildSpheres(self):
		self.rebuildSphere(sphere_button = self.ids.GeneralSphere, sphere_name = "generalSphere")
		self.rebuildSphere(sphere_button = self.ids.HealthSphere, sphere_name = "healthSphere")
		self.rebuildSphere(sphere_button = self.ids.RelationshipSphere, sphere_name = "relationshipSphere")
		self.rebuildSphere(sphere_button = self.ids.EnvironmentSphere, sphere_name = "environmentSphere")
		self.rebuildSphere(sphere_button = self.ids.VocationSphere, sphere_name = "vocationSphere")
		self.rebuildSphere(sphere_button = self.ids.IdependenceSphere, sphere_name = "independenceSphere")
		self.rebuildSphere(sphere_button = self.ids.SelfdevelopmentSphere, sphere_name = "selfdevelopmentSphere")
		self.rebuildSphere(sphere_button = self.ids.BrightnessSphere, sphere_name = "brightnessSphere")
		self.rebuildSphere(sphere_button = self.ids.SpiritualitySphere, sphere_name = "spiritualitySphere")
		
	def generalSphereClicked(self):
		print('GENERAL CLICKED')
		self.rebuildSliders('generalSphere')

	def healthSphereClicked(self):
		print('HEALTH CLICKED')
		self.rebuildSliders('healthSphere')

	def relationshipSphereClicked(self):
		print('RELATIONSHIP CLICKED')
		self.rebuildSliders('relationshipSphere')

	def environmentSphereClicked(self):
		print('ENVIRONMENT CLICKED')
		self.rebuildSliders('environmentSphere')

	def vocationSphereClicked(self):
		print('VOCATION CLICKED')
		self.rebuildSliders('vocationSphere')

	def independenceSphereClicked(self):
		print('INDEPENDENCE CLICKED')
		self.rebuildSliders('independenceSphere')

	def selfdevelopmentSphereClicked(self):
		print('SELFDEVELOPMENT CLICKED')
		self.rebuildSliders('selfdevelopmentSphere')

	def brightnessSphereClicked(self):
		print('BRIGHTNESS CLICKED')
		self.rebuildSliders('brightnessSphere')

	def spiritualitySphereClicked(self):
		print('SPIRITUALITY CLICKED')
		self.rebuildSliders('spiritualitySphere')

	def rebuildSliders(self, sphere_name):
		self.ids.layout_sliders.clear_widgets()
		for field in spheresObj.spheres[sphere_name]:
			layout = BoxLayout()
			layout.orientation = 'horizontal'
			
			slider_name_label = Label(text = field + ':')
			layout.add_widget(slider_name_label)
			
			slider = Slider(min = 0, max = 10, step = 1)
			slider.value = spheresObj.spheres[sphere_name][field]
			layout.add_widget(slider)
			
			slider_value_label = Label(text = str(slider.value))
			slider.bind(value=lambda instance, value, label=slider_value_label: self.on_slider_value_change_label_text(instance, value, label))
			field_name = field
			slider.bind(value=lambda instance, value, sphere_name=sphere_name, field=field_name: self.on_slider_value_change_sphere(instance, value, sphere_name, field))
			layout.add_widget(slider_value_label)

			
			self.ids.layout_sliders.add_widget(layout)
			
	def on_slider_value_change_label_text(self, instance, value, label):
		label.text = str(int(value))
		
	def on_slider_value_change_sphere(self, instance, value, sphere_name, field_name):
		spheresObj.change_spheres(sphere_name, field_name, int(value))
		self.rebuildSpheres()

	def rebuildSphere(self, sphere_button, sphere_name):
		spheres = spheresObj.spheres
		spheresColors = [249/255, 242/255, 107/255]
		sphere_button.clear_widgets()
		sphere_button.canvas.clear()
		sphere_button.canvas.after.clear()
		sphere_len = len(spheres[sphere_name].keys())
		counter = 0
		with sphere_button.canvas:
			Color(0.4, 0.4, 0.4, 1)
			Rectangle(pos = sphere_button.pos, size = sphere_button.size)
			Color(1, 0.2, 0.2, 1, z = 1)
			Line(ellipse = (
				sphere_button.center_x - (3/10)*min(sphere_button.width, sphere_button.height)/2,
				sphere_button.center_y - (3/10)*min(sphere_button.width, sphere_button.height)/2,
				(3/10)*min(sphere_button.width, sphere_button.height),
				(3/10)*min(sphere_button.width, sphere_button.height)
				 ), width = 1.5, z = 3)
			Color(1, 1, 0.2, 1)
			Line(ellipse = (
				sphere_button.center_x - (5/10)*min(sphere_button.width, sphere_button.height)/2,
				sphere_button.center_y - (5/10)*min(sphere_button.width, sphere_button.height)/2,
				(5/10)*min(sphere_button.width, sphere_button.height),
				(5/10)*min(sphere_button.width, sphere_button.height)
				 ), width = 1.5, z = 3)
			Color(0.2, 1, 0.2, 1)
			Line(ellipse = (
				sphere_button.center_x - (7/10)*min(sphere_button.width, sphere_button.height)/2,
				sphere_button.center_y - (7/10)*min(sphere_button.width, sphere_button.height)/2,
				(7/10)*min(sphere_button.width, sphere_button.height),
				(7/10)*min(sphere_button.width, sphere_button.height)
				 ), width = 1.5, z = 1)
			mean_score = sum(spheres[sphere_name].values())/len(spheres[sphere_name].values())
			for key in spheres[sphere_name].keys():
				Color(spheresColors[0], spheresColors[1], spheresColors[2], 1)
				Ellipse(pos = (sphere_button.center_x - (spheres[sphere_name][key]/10)*min(sphere_button.width, sphere_button.height)/2, sphere_button.center_y - (spheres[sphere_name][key]/10)*min(sphere_button.width, sphere_button.height)/2),
					size = ((spheres[sphere_name][key]/10)*min(sphere_button.width, sphere_button.height), (spheres[sphere_name][key]/10)*min(sphere_button.width, sphere_button.height)),
					angle_start = (counter/sphere_len * 360),
				    angle_end = ((counter + 1)/sphere_len * 360), z = 2)
				counter += 1
			Color(0.4, 0.4, 0.4, 1)
			Line(ellipse = (
				sphere_button.center_x - (mean_score/10)*min(sphere_button.width, sphere_button.height)/2,
				sphere_button.center_y - (mean_score/10)*min(sphere_button.width, sphere_button.height)/2,
				(mean_score/10)*min(sphere_button.width, sphere_button.height),
				(mean_score/10)*min(sphere_button.width, sphere_button.height)
				 ), width = 1.5, z = 3, font_size = '10sp')
		counter = 0
		for key in spheres[sphere_name].keys():
			new_label = Label(text = '[color=#222222]' + key + '[/color]', pos = (
				sphere_button.center_x - sphere_button.width/12 + 1.8*math.sin((counter + 0.5)*2*3.14/sphere_len)*min(sphere_button.width, sphere_button.height)/4,
				sphere_button.center_y - sphere_button.height/6 + 1.8*math.cos((counter + 0.5)*2*3.14/sphere_len)*min(sphere_button.width, sphere_button.height)/4), 
			font_size = '14sp', color = (0.95, 0.95, 0.95, 1), markup = True)
			sphere_button.add_widget(new_label)
			counter += 1
			'''Color(0.3, 0.3, 0.3, 1)
			Line(width = 2,
				ellipse = (
					self.ids.generalSphereButton.center_x - (spheres["generalSphere"][key]/10)*min(self.ids.generalSphereButton.width, self.ids.generalSphereButton.height)/2, 
				    self.ids.generalSphereButton.center_y - (spheres["generalSphere"][key]/10)*min(self.ids.generalSphereButton.width, self.ids.generalSphereButton.height)/2,
				    (spheres["generalSphere"][key]/10)*min(self.ids.generalSphereButton.width, self.ids.generalSphereButton.height),
				    (spheres["generalSphere"][key]/10)*min(self.ids.generalSphereButton.width, self.ids.generalSphereButton.height),
				    (counter/sphere_len * 360),
			    	((counter + 1)/sphere_len * 360)
				))
			Line(width = 1.5, points = (
				self.ids.generalSphereButton.center_x + math.sin(counter/sphere_len * 360)*(spheres["generalSphere"][key]/10)*min(self.ids.generalSphereButton.width, self.ids.generalSphereButton.height)/2,
				self.ids.generalSphereButton.center_y + math.cos(counter/sphere_len * 360)*(spheres["generalSphere"][key]/10)*min(self.ids.generalSphereButton.width, self.ids.generalSphereButton.height)/2,
				self.ids.generalSphereButton.center_x,
				self.ids.generalSphereButton.center_y
				))'''
