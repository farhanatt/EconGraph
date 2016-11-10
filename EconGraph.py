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
# "show()" method, but would rather not have it if possible.

class DemandCurve(object): 

	def __init__(self):
		self.coordinates = ([4, 3, 2, 1], [1, 2, 3, 4])
		self.axes = [0, 5, 0, 5]

		plt.plot(np.array(self.coordinates[0]), np.array(self.coordinates[1]), linewidth=2)
		plt.axis([0, 5, 0, 5])
		plt.text(4.1, 1, r'D')

	# TODO: Is there a way to make the parameters not strings? Maybe an create empty class
	# or object that would make it valid to say shift(Down) or shift(Up) in the DSL? 
	def shift(self, direction):				
		if direction == "up": 
			plt.plot(np.array([5,4,3,2]), np.array([2, 3, 4, 5]), linewidth=2)
			plt.axis([0,6,0,6])			
			plt.text(5.1, 2, r'D"')
		elif direction == "down":
			plt.plot(np.array([3,2,1,0]), np.array([0, 1, 2, 3]), linewidth=2)
			plt.axis([-1, 6, -1, 6])			
			plt.text(3.1, 0, r'D"')

	# TODO: Implement slope function.  Need to figure out how to do method chaining, though.


# # Demand Curve
# def DemandCurve():
# 	plt.plot(np.array([4,3,2,1]), np.array([1, 2, 3, 4]), linewidth=2)
# 	plt.axis([0, 5, 0, 5])
# 	plt.text(4.1, 1, r'D')

# Supply Curve
class SupplyCurve(): 
	def __init__(self):
		plt.plot(np.array([1,2,3,4]), np.array([1, 2, 3, 4]), linewidth=2)
		plt.axis([0, 5, 0, 5])
		plt.text(4.1, 4, r'S')

	def shift(self, direction):				
		if direction == "up": 
			plt.plot(np.array([2,3,4,5]), np.array([0, 1, 2, 3]), linewidth=2)
			plt.axis([-1,6,-1,6])			
			plt.text(5.1, 3, r'S"')
		elif direction == "down":
			plt.plot(np.array([0, 1, 2, 3]), np.array([2, 3, 4, 5]), linewidth=2)
			plt.axis([-1, 6, -1, 6])			
			plt.text(3.1, 5, r'S"')


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
