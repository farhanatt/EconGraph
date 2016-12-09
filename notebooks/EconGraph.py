import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.markers as markers
import collections
  
class Graph(object):
	xstart = 0
	xend = 10
	ystart = 0
	yend = 10

	def __init__(self):
		self.axes = [0, 10, 0, 10]
		self.xstart = 0
		self.xend = 10
		self.ystart = 0
		self.yend = 10
		self.curves = []

	def setAxes(self, xstart, xend, ystart, yend):
		self.xstart = xstart
		self.xend = xend
		self.ystart = ystart
		self.yend = yend
		self.axes = [xstart, xend, ystart, yend]

	def plot(self, *args):
		
		for a in args:
			self.curves.append(a)

		# self.createCurves()
		self.show()

	def getAxes(self):
		return self.axes

	def show(self):
		plt.plot()
		plt.axis(self.axes)
		for c in self.curves:
			l = str(c).split(".", 1)
			print(l)
			# c.show()

	def createDemandCurve(axes): 
		DemandCurve(axes)

	def DemandCurve(): 
		createDemandCurve(self.axes)


# DemandCurve TODO: Change in quantity demanded
class DemandCurve(object): 

	def __init__(self, axes):	
		# Axes scale
		self.xstart = 0
		self.xend = 10
		self.ystart = 0
		self.yend = 10		
		self.axes = [0, 10, 0, 10]
		# Coordinates for curve
		self.xcoordinates = [self.xend - 2, self.xstart + 2]
		self.ycoordinates = [self.ystart + 2, self.yend - 2]
		# Text for curve
		self.text = [5.1, 2, r'D']
		# Attributes for transformations
		self.markers = False
		self.shift = "none"
		self.slope_direction = "none"
		self.numLabels = 0
		self.labels = list([])		

	def increase(self):				
		self.xcoordinates =  list(map(lambda x: x+1, self.xcoordinates))
		self.ycoordinates =  list(map(lambda y: y+1, self.ycoordinates))
		self.shift = "increase"
		self.addToStr("shift", direction="increase")
		self.text[2] = r'D"'
		return self

	def setAxes(self, xstart, xend, ystart, yend):
		self.xstart = xstart
		self.xend = xend
		self.ystart = ystart
		self.yend = yend
		self.axes = [xstart, xend, ystart, yend]

	def decrease(self):
		self.xcoordinates =  list(map(lambda x: x-1, self.xcoordinates))
		self.ycoordinates =  list(map(lambda y: y-1, self.ycoordinates))
		self.shift = "decrease"
		self.addToStr("shift", direction="decrease")
		self.text[2] = r'D"'
		return self
	
	def label_line(self, x, y):
		plt.plot(np.array([0,x]), np.array([y,y]), linewidth=1, linestyle='dashed', color='red')
		plt.plot(np.array([x, x]), np.array([0,y]), linewidth=1, linestyle='dashed', color='red')
		plt.text(x+.1, 0, r'Qd')
		self.numLabels += 1
		self.addToStr("label", (x,y))
		self.labels.append((x, y))
		return self

	def slope(self, direction):
		if direction == "up":
			self.ycoordinates[0] = self.ycoordinates[0] - 0.5
			self.ycoordinates[1] = self.ycoordinates[1] + 0.5
			self.xcoordinates[0] = self.xcoordinates[0] - 1
			self.xcoordinates[1] = self.xcoordinates[1] + 1
			self.slope_direction = "up"
			self.addToStr("slope", direction="up")
			return self
		elif direction == "down": 
			self.ycoordinates[0] = self.ycoordinates[0] + 1
			self.ycoordinates[1] = self.ycoordinates[1] - 1
			self.slope_direction = "down"
			self.addToStr("slope", direction="down")
			return self
		elif direction == "horizontal": 
			self.ycoordinates[0] = 3
			self.ycoordinates[1] = 3
			self.xcoordinates[0] = self.xcoordinates[0] + 0.5
			self.xcoordinates[1] = self.xcoordinates[1] - 0.5
			self.slope_direction = "horizontal"
			self.addToStr("slope", direction="horizontal")
			return self
		elif direction == "vertical": 
			self.xcoordinates[0] = 3
			self.xcoordinates[1] = 3
			self.ycoordinates[0] = 0
			self.ycoordinates[1] = self.ycoordinates[1] + 0.5
			self.slope_direction = "vertical"
			self.addToStr("slope", direction="vertical")
			return self
	
	def show(self):
		# plt.axis(self.axes)
		if self.markers:
			plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), marker='o', linestyle='-', linewidth=2)	
			if self.shift == "increase":
				plt.plot(np.array(list(map(lambda x: x-1, self.xcoordinates))), np.array(list(map(lambda y: y-1, self.ycoordinates))), marker='o', linestyle='-', linewidth=2)	
			if self.shift == "decrease":
				plt.plot(np.array(list(map(lambda x: x+1, self.xcoordinates))), np.array(list(map(lambda y: y+1, self.ycoordinates))), marker='o', linestyle='-', linewidth=2)				
		else:
			plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), linewidth=2) 
			if self.shift == "increase":
				plt.plot(np.array(list(map(lambda x: x-1, self.xcoordinates))), np.array(list(map(lambda y: y-1, self.ycoordinates))), linewidth=2)	
			if self.shift == "decrease":
				plt.plot(np.array(list(map(lambda x: x+1, self.xcoordinates))), np.array(list(map(lambda y: y+1, self.ycoordinates))), linewidth=2)	
		plt.text((max(self.xcoordinates)) + .1, (min(self.ycoordinates)) + .1, self.text[2])
		if self.shift == "increase":
			plt.text((max(self.xcoordinates)) - 0.9, (min(self.ycoordinates)) - 0.9, r'D')
		if self.shift == "decrease":
			plt.text((max(self.xcoordinates)) + 1.1, (min(self.ycoordinates)) + 1.1, r'D')
		plt.ylabel('Price')
		plt.xlabel('Quantity')

	def addToStr(self, transformation, coords=None, direction=None):
		print("addToStr")
		# if self.shift != "none":
		if transformation == "shift":
			self.str += "." + str(direction) + "()"
		# if self.slope_direction != "none":
		if transformation == "slope":
			self.str += ".slope(" + str(direction) + ")"
		# if self.numLabels != 0:
		if transformation == "label":
			# for i in range (0, self.numLabels): 
			# 	tpl = str(self.labels[self.numLabels - 1])
			self.str += ".label_line" + str(coords)
		print(self.str)

	def __str__(self):
		return self.str

# Supply Curve
class SupplyCurve():
	
	def __init__(self):
		self.xcoordinates = [2,5]
		self.ycoordinates = [2,5]
		self.axes = [0, 10, 0, 10]
		self.text = [5.1, 5, r'S']
		self.markers = False
		self.shift = "none"

	def schedule(self, coordinates_list): 
		coordinates_dict = collections.OrderedDict(list(coordinates_list))
		x_coords = list(coordinates_dict.keys())
		y_coords = list(coordinates_dict.values())
		self.xcoordinates = x_coords
		self.ycoordinates = y_coords
		self.axes = [0, (max(self.xcoordinates)) + 2, 0, (max(self.ycoordinates)) + 2]
		self.markers = True
		return self

	def increase(self):				
		self.shift = "increase"
		self.xcoordinates =  list(map(lambda x: x+1, self.xcoordinates))
		self.ycoordinates =  list(map(lambda y: y-1, self.ycoordinates))
		self.text[2] = r'S"'
		return self

	def decrease(self):
		self.shift = "decrease"
		self.xcoordinates =  list(map(lambda x: x-1, self.xcoordinates))
		self.ycoordinates =  list(map(lambda y: y+1, self.ycoordinates))
		self.text[2] = r'S"'
		return self

	def slope(self, direction):
		if direction == "up":
			self.ycoordinates[0] = self.ycoordinates[0] - 1
			self.ycoordinates[1] = self.ycoordinates[1] + 1
			return self
		elif direction == "down": 
			self.ycoordinates[0] = self.xcoordinates[0] + 1
			self.ycoordinates[1] = self.xcoordinates[1] - 1
			return self
		elif direction == "horizontal": 
			self.ycoordinates[0] = 3
			self.ycoordinates[1] = 3
			self.xcoordinates[0] = self.xcoordinates[0] - 1
			self.xcoordinates[1] = self.xcoordinates[1] + 1
			return self
		elif direction == "vertical": 
			self.xcoordinates[0] = 3
			self.xcoordinates[1] = 3
			self.ycoordinates[0] = 0
			self.ycoordinates[1] = self.ycoordinates[1] + 1
			return self
	
	def label_line(self, x, y): 
		plt.plot(np.array([0,x]), np.array([y,y]), linewidth=1, linestyle='dashed', color='red')
		plt.plot(np.array([x, x]), np.array([0,y]), linewidth=1, linestyle='dashed', color='red')
		plt.text(x+.1, 0, r'Qs')
		return self

	def show(self): 
		plt.axis(self.axes)
		if self.markers:
			plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), marker='o', linestyle='-', linewidth=2)	
			if self.shift == "increase":
				plt.plot(np.array(list(map(lambda x: x-1, self.xcoordinates))), np.array(list(map(lambda y: y+1, self.ycoordinates))), marker='o', linestyle='-', linewidth=2)	
			if self.shift == "decrease":
				plt.plot(np.array(list(map(lambda x: x+1, self.xcoordinates))), np.array(list(map(lambda y: y-1, self.ycoordinates))), marker='o', linestyle='-', linewidth=2)				
		else:
			plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), linewidth=2) 
			if self.shift == "increase":
				plt.plot(np.array(list(map(lambda x: x-1, self.xcoordinates))), np.array(list(map(lambda y: y+1, self.ycoordinates))), linewidth=2)	
			if self.shift == "decrease":
				plt.plot(np.array(list(map(lambda x: x+1, self.xcoordinates))), np.array(list(map(lambda y: y-1, self.ycoordinates))), linewidth=2)	
		plt.text((max(self.xcoordinates)) + .1, (max(self.ycoordinates)) + .1, self.text[2])
		if self.shift == "increase":
			plt.text((max(self.xcoordinates)) - 0.9, (max(self.ycoordinates)) + 0.9, r'S')
		if self.shift == "decrease":
			plt.text((max(self.xcoordinates)) + 0.9, (max(self.ycoordinates)) - 0.9, r'S')
		plt.ylabel('Price')
		plt.xlabel('Quantity')

#https://www.youtube.com/watch?v=2izx5W1FAEU&list=PLA46DB4506062B62B&index=1
#PPC TODO: 
	# - Constant PPC by default
	# - Support "with favor consumer/capital goods"
	# - Label axes by default to consumer/capital
	# - "Capital investment" - Frontier shifts out but with same intersection on Y axis
	# - Axis endpoints/axes scale
class PPC():
	def __init__(self): 
		cir1 = patches.Circle((0,0), radius=0.5, fc='none')
		self.patches = [cir1]

	def unattainable_point(self):
		plt.plot(0.2, 0.1, 'o')
		return self

	def increase(self):
		cir2 = patches.Circle((0,0), radius=0.75, fc='none')
		arr = patches.Arrow(0.33, 0.45, 0.1, 0.1, width=0.1)
		self.patches.append(cir2)
		self.patches.append(arr)
		return self

	def decrease(self):
		cir2 = patches.Circle((0,0), radius=0.25, fc='none')
		arr = patches.Arrow(0.37, 0.25, -0.15, -0.1, width=0.1)
		self.patches.append(cir2)
		self.patches.append(arr)	
		return self

	def show(self): 
		ax = plt.axes(aspect=1)
		for patch in self.patches:
			ax.add_patch(patch)	
		plt.show()

# class SurplusOrShortage():
# 	def __init__(self, height):
# 		plt.plot([0,1,2,3,4,5], [height, height, height, height, height,height], linestyle='--')

class Schedule(): 
	def __init__(self, coordinates_list): 
		coordinates_dict = collections.OrderedDict(list(coordinates_list))
		x_coords = list(coordinates_dict.keys())
		y_coords = list(coordinates_dict.values())
		self.xcoordinates = x_coords
		self.ycoordinates = y_coords
		self.axes = [0, (max(self.xcoordinates)) + 2, 0, (max(self.ycoordinates)) + 2]
		self.markers = True
		self.text = [5.1, 2, r'D']

	def show(self): 
		plt.axis(self.axes)
		if self.markers:
			plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), marker='o', linewidth=2)
		else:
			plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), linewidth=2)