import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import matplotlib.markers as markers


# TODO: Check if there is some way in matplotlib to store all the curves in a figure/graph
# first.  Currently, when we instantiate a curve object, it will instantly plot, which we
# may not necessarily want in all cases.  We may want to have default coordinates, but 
# not want it plotted first so we can adjust the slope before it appears.  However, we 
# also need to show the curve if there are no transformations.  Could be done with a 
# "show()" method, but would rather not have it if possible

class DemandCurve(object): 

	def __init__(self):
		self.xcoordinates = [4, 1]
		self.ycoordinates = [1, 4]
		self.axes = [-1, 6, -1, 6]
		self.text = [4.1, 1, r'D']

	def increase(self):				
		DemandCurve().show()
		self.xcoordinates =  list(map(lambda x: x+1, self.xcoordinates))
		self.ycoordinates =  list(map(lambda y: y+1, self.ycoordinates))
		self.text[2] = r'D"'
		return self

	def decrease(self):
		DemandCurve().show()
		self.xcoordinates =  list(map(lambda x: x-1, self.xcoordinates))
		self.ycoordinates =  list(map(lambda y: y-1, self.ycoordinates))
		self.text[2] = r'D"'
		return self
	
	def label_line(self, x, y): 
		plt.plot(np.array([-1,x]), np.array([y,y]), linewidth=1, linestyle='dashed', color='red')
		plt.plot(np.array([x, x]), np.array([-1,y]), linewidth=1, linestyle='dashed', color='red')
		return self

	def slope(self, direction):
		if direction == "up":
			self.ycoordinates[0] = self.ycoordinates[0] - 0.5
			self.ycoordinates[1] = self.ycoordinates[1] + 0.5
			self.xcoordinates[0] = self.xcoordinates[0] - 0.5
			self.xcoordinates[1] = self.xcoordinates[1] + 0.5
			return self
		elif direction == "down": 
			self.ycoordinates[0] = self.ycoordinates[0] + 0.5
			self.ycoordinates[1] = self.ycoordinates[1] - 0.5
			return self
		elif direction == "horizontal": 
			self.ycoordinates[0] = 3
			self.ycoordinates[1] = 3
			self.xcoordinates[0] = self.xcoordinates[0] + 0.5
			self.xcoordinates[1] = self.xcoordinates[1] - 0.5
			return self
		elif direction == "vertical": 
			self.xcoordinates[0] = 3
			self.xcoordinates[1] = 3
			self.ycoordinates[0] = self.ycoordinates[0] - 0.5
			self.ycoordinates[1] = self.ycoordinates[1] + 0.5
			return self
	
	def show(self): 
		plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), linewidth=2)
		plt.axis(self.axes)
		plt.text(self.xcoordinates[1] + .1, self.ycoordinates[1] + .1, self.text[2])

# Supply Curve
class SupplyCurve(): 
	
	def __init__(self):
		self.xcoordinates = [1,4]
		self.ycoordinates = [1,4]
		self.axes = [-1, 6, -1, 6]
		self.text = [4.1, 4, r'S']


	def increase(self):				
		SupplyCurve().show()
		self.xcoordinates =  list(map(lambda x: x+1, self.xcoordinates))
		self.ycoordinates =  list(map(lambda y: y-1, self.ycoordinates))
		self.text[2] = r'S"'
		return self

	def decrease(self):
		SupplyCurve().show()
		self.xcoordinates =  list(map(lambda x: x-1, self.xcoordinates))
		self.ycoordinates =  list(map(lambda y: y+1, self.ycoordinates))
		self.text[2] = r'S"'
		return self

	def slope(self, direction):
		if direction == "up":
			self.ycoordinates[0] = self.ycoordinates[0] - 0.5
			self.ycoordinates[1] = self.ycoordinates[1] + 0.5
			return self
		elif direction == "down": 
			self.ycoordinates[0] = self.xcoordinates[0] + 0.5
			self.ycoordinates[1] = self.xcoordinates[1] - 0.5
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
			self.ycoordinates[0] = self.ycoordinates[0] - 1
			self.ycoordinates[1] = self.ycoordinates[1] + 1
			return self
	
	def label_line(self, x, y): 
		plt.plot(np.array([-1,x]), np.array([y,y]), linewidth=1, linestyle='dashed', color='red')
		plt.plot(np.array([x, x]), np.array([-1,y]), linewidth=1, linestyle='dashed', color='red')
		return self

	def show(self): 
		plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), linewidth=2)
		plt.axis(self.axes)
		plt.text(self.xcoordinates[1] + .1, self.ycoordinates[1], self.text[2])


class PPF():
	
	def __init__(self): 
		cir1 = patches.Circle((0,0), radius=0.5, fc='none')
		self.patches = [cir1]
		
	# def unattainable_point(self):
	# 	# plt.plot(0.2, 0.2,
 #  #        marker='o',
 #  #        fillstyle='full',
 #  #        markeredgecolor='red',
 #  #        markeredgewidth=1)
 #  		pt = patches.Patch((0.2, 0.2), fill=True, facecolor='b')
 #  		self.patches.append(pt)
 #  		return self

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
		ax.add_line()
		plt.show()
