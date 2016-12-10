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
		self.ylabel = "Price"
		self.xlabel = "Quantity"
		self.title = ""
		self.curves = []

	def setAxes(self, xstart, xend, ystart, yend):
		self.xstart = xstart
		self.xend = xend
		self.ystart = ystart
		self.yend = yend
		self.axes = [xstart, xend, ystart, yend]

	def xLabel(self, label):
		self.xlabel = label
		
	def yLabel(self, label):
		self.ylabel = label

	def setTitle(self, title):
		self.title = title

	def setLabels(self, type):
		if type.__str__() == "Macro":
			self.ylabel = "Price Level"
			self.ylabel = "Output"
			self.ylabel = "Aggregate Supply and Demand"
		if type.__str__() == "MoneyMarket":
			self.ylabel = "Nominal Interest Rate"
			self.xlabel = "Quantity of Money"
			self.title = "Money Market"
		if type.__str__() == "LoanableFunds":
			self.ylabel = "Real Interest Rate"
			self.xlabel = "Quantity of Loanable Funds"
			self.title = "Loanable Funds Market"

	def annotate_point(self, message, point_coords, text_coords):
		plt.plot(point_coords[0], point_coords[1], marker='o')
		plt.annotate(message, xy=point_coords, xytext=text_coords, 
			arrowprops=dict(facecolor='black', shrink=0.05, width=0, headwidth=5))
		return self

	def mark_point(self, x, y): 
		plt.plot(x, y, marker='o')
		return self

	def plot(self, *args):
		for a in args:
			self.curves.append(a)
		self.show()

	def show(self):
		plt.plot()
		plt.axis(self.axes)
		for c in self.curves:
			c.translate(self.axes)
		plt.ylabel(self.ylabel)
		plt.xlabel(self.xlabel)
		plt.title(self.title)

class DemandCurve(object): 

	def __init__(self):	
		# Default axes scale
		self.xstart = 0
		self.xend = 10
		self.ystart = 0 
		self.yend = 10
		self.axes = [0, 10, 0, 10]
		self.scale = 2

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

		# Attributes for marking points
		self.numMarks = 0
		self.pointsToMark = list([])

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

	def trace_point(self, x, y):
		plt.plot(np.array([0,x]), np.array([y,y]), linewidth=1, linestyle='dashed', color='red')
		plt.plot(np.array([x, x]), np.array([0,y]), linewidth=1, linestyle='dashed', color='red')
		plt.text(x+.1, 0, r'Qd')
		self.numMarks += 1
		self.pointsToMark.append((x, y))
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
		self.numMarks = 0
		self.pointsToMark = list([])

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

	def trace_point(self, x, y): 
		plt.plot(np.array([0,x]), np.array([y,y]), linewidth=1, linestyle='dashed', color='red')
		plt.plot(np.array([x, x]), np.array([0,y]), linewidth=1, linestyle='dashed', color='red')
		plt.text(x+.1, 0, r'Qs')
		self.numMarks += 1
		self.pointsToMark.append((x, y))
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

class PPC():
	def __init__(self): 
		cir1 = patches.Circle((0,0), radius=0.5, fc='none')
		self.patches = [cir1]

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

	def translate(self, axes): 
		ax = plt.axes(aspect=1)
		for patch in self.patches:
			ax.add_patch(patch)
		ax.set_title("Production Possibilities Frontier")	
		ax.set_xlabel("Capital Goods")
		ax.set_ylabel("Consumer Goods")
		
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

	def translate(self, axes): 
		plt.axis(self.axes)
		if self.markers:
			plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), marker='o', linewidth=2)
		else:
			plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), linewidth=2)


class MoneyMarket():
	def __str__():
		return "MoneyMarket"

class LoanableFunds():
	def __str__():
		return "LoanableFunds"

class Macro():
	def __str__():
		return "Macro"