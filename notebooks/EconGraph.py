import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches


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

		# plt.plot(np.array(self.coordinates[0]), np.array(self.coordinates[1]), linewidth=2)
		# plt.axis([0, 5, 0, 5])
		# plt.text(4.1, 1, r'D')

	# TODO: Is there a way to make the parameters not strings? Maybe an create empty class
	# or object that would make it valid to say shift(Down) or shift(Up) in the DSL? 
	def shift(self, direction):				
		if direction == "up": 
			DemandCurve().show()
			self.xcoordinates =  list(map(lambda x: x+1, self.xcoordinates))
			self.ycoordinates =  list(map(lambda y: y+1, self.ycoordinates))
			self.text[2] = r'D"'
			return self
		elif direction == "down":
			self.xcoordinates =  list(map(lambda x: x-1, self.xcoordinates))
			self.ycoordinates =  list(map(lambda y: y-1, self.ycoordinates))
			self.text[2] = r'D"'
			return self
			# plt.plot(np.array([3,2,1,0]), np.array([0, 1, 2, 3]), linewidth=2)
			# plt.axis([-1, 6, -1, 6])			
			# plt.text(3.1, 0, r'D"')
	
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


# # Demand Curve
# def DemandCurve():
# 	plt.plot(np.array([4,3,2,1]), np.array([1, 2, 3, 4]), linewidth=2)
# 	plt.axis([0, 5, 0, 5])
# 	plt.text(4.1, 1, r'D')

# Supply Curve
class SupplyCurve(): 
	def __init__(self):
		self.xcoordinates = [1,4]
		self.ycoordinates = [1,4]
		self.axes = [-1, 6, -1, 6]
		self.text = [4.1, 4, r'S']


	def shift(self, direction):				
		if direction == "up": 
			SupplyCurve().show()
			self.xcoordinates =  list(map(lambda x: x+1, self.xcoordinates))
			self.ycoordinates =  list(map(lambda y: y-1, self.ycoordinates))
			# self.axes = [self.axes[0]-1, self.axes[1]+1, self.axes[2]-1, self.axes[3]+1]
			self.text[2] = r'S"'
			return self
			# plt.plot(np.array([2,3,4,5]), np.array([0, 1, 2, 3]), linewidth=2)
			# plt.axis([-1,6,-1,6])			
			# plt.text(5.1, 3, r'S"')
		elif direction == "down":
			SupplyCurve().show()
			self.xcoordinates =  list(map(lambda x: x-1, self.xcoordinates))
			self.ycoordinates =  list(map(lambda y: y+1, self.ycoordinates))
			self.text[2] = r'S"'
			return self

	def slope(self, direction):
		if direction == "up":
			self.ycoordinates[0] = self.ycoordinates[0] - 0.5
			self.ycoordinates[1] = self.ycoordinates[1] + 0.5
			# plt.plot(np.array([1, 1.5, 2, 2.5]), np.array([1, 2, 3, 4]))
			# plt.axis([0, 5, 0, 5])
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

	def show(self): 
		plt.plot(np.array(self.xcoordinates), np.array(self.ycoordinates), linewidth=2)
		plt.axis(self.axes)
		plt.text(self.xcoordinates[1] + .1, self.ycoordinates[1], self.text[2])


class PPF():
	def __init__(self): 
		cir1 = patches.Circle((0,0), radius=0.75, fc='w')
		self.patches = [cir1]
		
	
	def increase(self):
		cir2 = patches.Circle((0,0), radius=0.5, fc='w')
		arr = patches.Arrow(0.33, 0.45, 0.1, 0.1, width=0.1)
		self.patches.append(cir2)
		self.patches.append(arr)
		return self

	def decrease(self):
		cir2 = patches.Circle((0,0), radius=0.5, fc='w')
		arr = patches.Arrow(0.57, 0.45, -0.15, -0.1, width=0.1)
		self.patches.append(cir2)
		self.patches.append(arr)
		return self

	def show(self): 
		ax = plt.axes(aspect=1)
		for patch in self.patches:
			ax.add_patch(patch)	
		plt.show()
	
# class SupplyCurve(): 
# 	def __init__(self):
# 		self.xcoordinates = [1,2,3,4]
# 		self.ycoordinates = [1,2,3,4]
# 		self.axes = [0,5,0,5]
# 		plt.plot(np.array([1,2,3,4]), np.array([1, 2, 3, 4]), linewidth=2)
# 		plt.axis([0, 5, 0, 5])
# 		plt.text(4.1, 4, r'S')

# 	def shift(self, direction):				
# 		if direction == "up": 
# 			plt.plot(np.array([2,3,4,5]), np.array([0, 1, 2, 3]), linewidth=2)
# 			plt.axis([-1,6,-1,6])			
# 			plt.text(5.1, 3, r'S"')
# 		elif direction == "down":
# 			plt.plot(np.array([0, 1, 2, 3]), np.array([2, 3, 4, 5]), linewidth=2)
# 			plt.axis([-1, 6, -1, 6])			
# 			plt.text(3.1, 5, r'S"')

# 	def slope(self, direction):
# 		if direction == "up": 
# 			plt.plot(np.array([1, 1.5, 2, 2.5]), np.array([1, 2, 3, 4]))
# 			plt.axis([0, 5, 0, 5])
# 		elif

# def SupplyCurve(): 
# 	plt.plot(np.array([1,2,3,4]), np.array([1, 2, 3, 4]), linewidth=2)
# 	plt.axis([0, 5, 0, 5])
# 	plt.text(4.1, 4, r'S')

def SupplyDemand(): 
	# Demand Curve
	plt.plot(np.array([4,3,2,1]), np.array([1, 2, 3, 4]), linewidth=2)
	# Supply Curve
	plt.plot(np.array([1,2,3,4]), np.array([1, 2, 3, 4]), linewidth=2)
	plt.axis([0, 6, 0, 6])
	plt.text(4.1, 4, r'S')
	plt.text(5.1, 2, r'D"')
	plt.text(4.1, 1, r'D')

def SupplyDemandIncreaseDemand():
	# Demand Curve
	plt.plot(np.array([4,3,2,1]), np.array([1, 2, 3, 4]), linewidth=2)
	# Demand Curve shifted out
	plt.plot(np.array([5,4,3,2]), np.array([2, 3, 4, 5]), linewidth=2)
	# Supply Curve
	plt.plot(np.array([1,2,3,4]), np.array([1, 2, 3, 4]), linewidth=2)
	plt.axis([0, 6, 0, 6])
	plt.text(4.1, 4, r'S')
	plt.text(5.1, 2, r'D"')
	plt.text(4.1, 1, r'D')
