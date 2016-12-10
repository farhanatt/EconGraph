import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.markers as markers
import collections
  
class Graph(object):

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
		self.show()

	def show(self):
		plt.plot()
		plt.axis(self.axes)
		for c in self.curves:
			c.translate(self.axes)


# DemandCurve TODO: Change in quantity demanded
class DemandCurve(object): 

	def __init__(self):	
		# Default axes scale
		self.xstart = 0
		self.xend = 10
		self.ystart = 0 
		self.yend = 10
		self.axes = [0, 10, 0, 10]
		self.scale = 2
		self.xlabel = "Quantity"
		self.ylabel = "Price"

		# Coordinates for curve
		self.xcoordinates = [self.xend - 2, self.xstart + 2]
		self.ycoordinates = [self.ystart + 2, self.yend - 2]

		# Text for curve
		self.text = [5.1, 2, r'D']
		# Attributes for transformations
		self.markers = False

		#Attribute for shift
		self.shift = "none"

		# Attributes for slope
		self.slope_direction = "none"
		self.slope_scale = 0

		# Attributes for labelling lines
		self.numLabels = 0
		self.labels = list([])

		# Attribute holding list of transformations
		self.transformations = []		

	# Adjust coordinates based on graph axes
	def translate(self, axes): 
		# Set axes
		self.xstart = axes[0]
		self.xend = axes[1]
		self.ystart = axes[2]
		self.yend = axes[3]
		self.axes = axes

		# Set coordinates relative to axes
		self.coords_scale = (self.xend - self.xstart) * 0.2
		self.xcoordinates = [self.xend - self.coords_scale, self.xstart + self.coords_scale]
		self.ycoordinates = [self.ystart + self.coords_scale, self.yend - self.coords_scale]

		# Set slope scale 
		self.slope_scale = (self.yend-self.ystart) * .10
		self.transform()
		return self

	def decrease(self):
		self.transformations.append(self._decrease)
		return self

	def _increase(self):			
		self.shift = "increase"
		self.text[2] = r'D'
		return self

	def increase(self):
		self.transformations.append(self._increase)
		return self

	def _decrease(self):
		self.shift = "decrease"
		self.text[2] = r'D'
		return self
	
	def label_line(self, x, y):
		plt.plot(np.array([0,x]), np.array([y,y]), linewidth=1, linestyle='dashed', color='red')
		plt.plot(np.array([x, x]), np.array([0,y]), linewidth=1, linestyle='dashed', color='red')
		plt.text(x+.1, 0, r'Qd')
		self.numLabels += 1
		self.labels.append((x, y))
		return self

	def slope_up(self):
		self.transformations.append(self._slope_up)
		return self

	def _slope_up(self):
		self.ycoordinates[0] = self.ycoordinates[0] - self.slope_scale
		self.ycoordinates[1] = self.ycoordinates[1] + self.slope_scale
		self.xcoordinates[0] = self.xcoordinates[0] - self.slope_scale
		self.xcoordinates[1] = self.xcoordinates[1] + self.slope_scale
		self.slope_direction = "up"
		return self

	def slope_down(self):
		self.transformations.append(self._slope_down)
		return self

	def _slope_down(self):
		self.ycoordinates[0] = self.ycoordinates[0] + self.slope_scale
		self.ycoordinates[1] = self.ycoordinates[1] - self.slope_scale
		self.xcoordinates[0] = self.xcoordinates[0] + self.slope_scale
		self.xcoordinates[1] = self.xcoordinates[1] - self.slope_scale
		self.slope_direction = "down"
		return self

	def slope_horizontal(self):
		self.transformations.append(self._slope_horizontal)
		return self

	def _slope_horizontal(self):
		self.ycoordinates[0] = (max(self.axes[2], self.axes[3]) + min(self.axes[2], self.axes[3]))/2
		self.ycoordinates[1] = (max(self.axes[2], self.axes[3]) + min(self.axes[2], self.axes[3]))/2
		self.xcoordinates[0] = self.xcoordinates[0] + 0.5
		self.xcoordinates[1] = self.xcoordinates[1] - 0.5
		self.slope_direction = "horizontal"
		return self
	
	def slope_vertical(self):
		self.transformations.append(self._slope_vertical)
		return self

	def _slope_vertical(self):
		self.xcoordinates[0] = (max(self.axes[0], self.axes[1]) + min(self.axes[0], self.axes[1]))/2
		self.xcoordinates[1] = (max(self.axes[0], self.axes[1]) + min(self.axes[0], self.axes[1]))/2
		self.ycoordinates[0] = 0
		self.ycoordinates[1] = self.ycoordinates[1] + 0.5
		self.slope_direction = "vertical"
		return self
	
	def transform(self):
		for transformation in self.transformations:
			transformation()
		self.show()
		return self

	def show(self):
		plt.axis(self.axes)
		shift_scale = (self.axes[3] + self.axes[2]) * 0.1
		if self.markers:
			plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), marker='o', linestyle='-', linewidth=2)	
			if self.shift == "increase":
				plt.plot(np.array(list(map(lambda x: x-1, self.xcoordinates))), np.array(list(map(lambda y: y-1, self.ycoordinates))), marker='o', linestyle='-', linewidth=2)	
			if self.shift == "decrease":
				plt.plot(np.array(list(map(lambda x: x+1, self.xcoordinates))), np.array(list(map(lambda y: y+1, self.ycoordinates))), marker='o', linestyle='-', linewidth=2)				
		else:
			plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), linewidth=2) 
			if self.shift == "decrease":
				plt.plot(np.array(list(map(lambda x: x-shift_scale, self.xcoordinates))), np.array(list(map(lambda y: y-shift_scale, self.ycoordinates))), linewidth=2)	
			if self.shift == "increase":
				plt.plot(np.array(list(map(lambda x: x+shift_scale, self.xcoordinates))), np.array(list(map(lambda y: y+shift_scale, self.ycoordinates))), linewidth=2)		
		plt.text((max(self.xcoordinates)) + 0.2, (min(self.ycoordinates)) + 0.2, self.text[2])
		if self.shift == "decrease":
			plt.text((max(self.xcoordinates)) - shift_scale, (min(self.ycoordinates)) - shift_scale - (shift_scale * 0.2), r'D"')
		if self.shift == "increase":
			plt.text((max(self.xcoordinates)) + shift_scale, (min(self.ycoordinates)) + shift_scale + (shift_scale * 0.2), r'D"')
		plt.ylabel(self.ylabel)
		plt.xlabel(self.xlabel)

# Supply Curve
class SupplyCurve():
	
	def __init__(self):
		# Default axes scale
		self.xstart = 0
		self.xend = 10
		self.ystart = 0 
		self.yend = 10
		self.axes = [0, 10, 0, 10]
		self.scale = 2
		self.xlabel = "Quantity"
		self.ylabel = "Price"

		# Coordinates for curve
		self.xcoordinates = [self.xend - 2, self.xstart + 2]
		self.ycoordinates = [self.yend - 2, self.ystart + 2]

		# Text for curve
		self.text = [5.1, 5, r'S']
		# Attributes for transformations
		self.markers = False

		#Attribute for shift
		self.shift = "none"

		# Attributes for slope
		self.slope_direction = "none"
		self.slope_scale = 0

		# Attributes for labelling lines
		self.numLabels = 0
		self.labels = list([])

		# Attribute holding list of transformations
		self.transformations = []

	def translate(self, axes): 
		# Set axes
		self.xstart = axes[0]
		self.xend = axes[1]
		self.ystart = axes[2]
		self.yend = axes[3]
		self.axes = axes

		# Set coordinates relative to axes
		self.coords_scale = (self.xend - self.xstart) * 0.2
		self.xcoordinates = [self.xstart + self.coords_scale, self.xend - self.coords_scale]
		self.ycoordinates = [self.ystart + self.coords_scale, self.yend - self.coords_scale]

		# Set slope scale 
		self.slope_scale = (self.yend-self.ystart) * .10
		self.transform()
		return self

	def decrease(self): 
		self.transformations.append(self._decrease)
		return self 

	def _decrease(self):
		self.shift = "decrease"
		self.text[2] = r'S'
		return self

	def increase(self): 
		self.transformations.append(self._increase)
		return self 

	def _increase(self):
		self.shift = "increase"
		self.text[2] = r'S'
		return self
	
	def slope_up(self):
		self.transformations.append(self._slope_up)
		return self
	
	def _slope_up(self):
		self.ycoordinates[0] = self.ycoordinates[0] - self.slope_scale
		self.ycoordinates[1] = self.ycoordinates[1] + self.slope_scale
		return self

	def slope_down(self):
		self.transformations.append(self._slope_down)
		return self

	def _slope_down(self):
		self.ycoordinates[0] = self.xcoordinates[0] + self.slope_scale
		self.ycoordinates[1] = self.xcoordinates[1] - self.slope_scale
		return self

	def slope_horizontal(self):
		self.transformations.append(self._slope_horizontal)
		return self

	def _slope_horizontal(self): 
		self.ycoordinates[0] = (max(self.axes[2], self.axes[3]) + min(self.axes[2], self.axes[3]))/2
		self.ycoordinates[1] = (max(self.axes[2], self.axes[3]) + min(self.axes[2], self.axes[3]))/2
		self.xcoordinates[0] = self.xcoordinates[0] - self.slope_scale
		self.xcoordinates[1] = self.xcoordinates[1] + self.slope_scale
		return self

	def slope_vertical(self):
		self.transformations.append(self._slope_vertical)
		return self

	def _slope_vertical(self):
		self.xcoordinates[0] = (max(self.axes[0], self.axes[1]) + min(self.axes[0], self.axes[1]))/2
		self.xcoordinates[1] = (max(self.axes[0], self.axes[1]) + min(self.axes[0], self.axes[1]))/2
		self.ycoordinates[0] = 0
		self.ycoordinates[1] = self.ycoordinates[1] + self.slope_scale
		return self
	
	def label_line(self, x, y): 
		plt.plot(np.array([0,x]), np.array([y,y]), linewidth=1, linestyle='dashed', color='red')
		plt.plot(np.array([x, x]), np.array([0,y]), linewidth=1, linestyle='dashed', color='red')
		plt.text(x+.1, 0, r'Qs')
		return self

	def transform(self):
		for transformation in self.transformations:
			transformation()
		self.show()
		return self

	def show(self): 
		plt.axis(self.axes)
		shift_scale = (self.axes[3] + self.axes[2]) * 0.1				
		if self.markers:
			plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), marker='o', linestyle='-', linewidth=2)	
			if self.shift == "increase":
				plt.plot(np.array(list(map(lambda x: x-1, self.xcoordinates))), np.array(list(map(lambda y: y+1, self.ycoordinates))), marker='o', linestyle='-', linewidth=2)	
			if self.shift == "decrease":
				plt.plot(np.array(list(map(lambda x: x+1, self.xcoordinates))), np.array(list(map(lambda y: y-1, self.ycoordinates))), marker='o', linestyle='-', linewidth=2)				
		else:
			plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), linewidth=2) 
			if self.shift == "decrease":
				plt.plot(np.array(list(map(lambda x: x-shift_scale, self.xcoordinates))), np.array(list(map(lambda y: y+shift_scale, self.ycoordinates))), linewidth=2)	
			if self.shift == "increase":
				plt.plot(np.array(list(map(lambda x: x+shift_scale, self.xcoordinates))), np.array(list(map(lambda y: y-shift_scale, self.ycoordinates))), linewidth=2)	
		plt.text((max(self.xcoordinates)) + .1, (max(self.ycoordinates)) + .1, self.text[2])
		if self.shift == "decrease":
			plt.text((max(self.xcoordinates)) - shift_scale, (max(self.ycoordinates)) + shift_scale + (shift_scale * 0.2), r'S"')
		if self.shift == "increase":
			plt.text((max(self.xcoordinates)) + shift_scale, (max(self.ycoordinates)) - shift_scale + (shift_scale * 0.2), r'S"')
		plt.ylabel(self.ylabel)
		plt.xlabel(self.xlabel)

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