#EconGraph

## Installation & Setup
Make sure you've downloaded python3

Install jupyter notebook following instructions from this link: https://jupyter.readthedocs.io/en/latest/install.html#installing-jupyter-using-anaconda-and-conda

Run `jupyter notebook` in your terminal, which will launch the notebook in your
browser.  You'll be taken to a UI that lists your local files.

Install matplotlib: http://matplotlib.org/users/installing.html#mac-osx-using-pip

Click the "New" dropdown menu on the top right of the notebook UI, and select
"Python (default)".  Save the file `EconGraph.py` in the same directory as your
notebook.  


In the first cell of your notebook, copy and paste the following code:
```
%matplotlib inline
from EconGraph import *
``` 
Then press `Shift+Enter` to run the cell.

Now you should be able to use any of the functions in the DSL.   
To verify that it works, copy and paste the following code and run the cell:

```
g = Graph()
g.plot(
	DemandCurve().increase().show()
	)
```

You should see a graph showing an increase in demand (two demand curves).   
# Example programs

See [notebooks/Test.ipynb](notebooks/Test.ipynb) for example programs.

# API

## Graph
Each graph is created by the `Graph()` object.  When creating a new graph, always create
a `Graph()`.  Here's how to create a Graph() that we're calling g: 

```
g = Graph()
```

`Graph()` allows you to customize your graph.  Specifically, it wil allow you to
customize the title, axes scales, axes labels, and mark and annotate points.
Most importantly, `Graph()` allows you to add curves to your graph. 


Here is a list of methods you can use with Graph().  Each example assumes that the Graph() object is represented by a variable `g`:

### setTitle("title")
`setTitle()` takes in words inside quotes (also called a "string") as input. 
This will add the title you input at the top of your graph. 
```
g.setTitle("Graph of Donut Supply and Demand")
```

### setAxes(xstart, xend, ystart, yend)
`setAxes` sets the axes range for the x and y axes.  It takes in 4 numbers as input. The first number is the starting value on the x-axis.  The second number is the last value on the x-axis.  The third is the first value on the y-axis.  The fourth is the last value on the y-axis.  The axes are set to (0, 10, 0, 10) by default, so only use this if you want to use a different scale.
```
g.setAxes(0, 100, 0, 100)
```
### xLabel("label")
`xLabel` sets the label for the x-axis.  It takes in a string as input. 
```
g.xLabel("Quantity of donuts")
```

### yLabel("label")
`yLabel` sets the label for the y-axis.  It takes in a string as input. 
```
g.yLabel("Price of donuts")
```
### setLabels(graphType)
`setLabels` sets the labels for the title, x-axis, and y-axis.  Use this method when you know the type of graph you want to create, so you don't have to set the labels and title through using three different methods.  The options for the type of graph are: 
- `MoneyMarket` where the title will be set to "Money Market", the x-label will be "Quantity of Money", and the y-label will be "Nominal Interest Rate"
- `LoanableFunds` where the title will be set to "Loanable Funds Market", the x-label will be 
"Quantity of Loanable Funds", and the y-label will be set to "Real Interest Rate".
- `Macro` where the title will be "Aggregate Supply and Demand", the x-label will be "Output", and the y-label will be "Price Level"
```
g.yLabel("Price of donuts")
```
### annotate_point("text", (x, y), (x, y))
`annotate_point` adds text and an arrow pointing to a specific point.  This method takes in a string for the text to be added, a set of x and y coordinates (Ex: (1,2)where the arrow should point, and another set of x and y coordinates for where the text should appear on the graph.  

```
annotate_point("original equilibrium", (50, 50), (30, 10))
```

### mark_point(x, y)
`mark_point` adds a dot to a specific point on the graph.  It takes in two numbers that represent the x and y coordinates of where the point should be added.
```
mark_point(1, 2)
```

### plot(*curves)
`plot` takes in an arbitrary number of curve objects.  This method will plot the curves on to the graph object

## DemandCurve
`DemandCurve()` will add a demand curve to the graph.

### decrease()
`decrease()` will add a demand curve showing a decrease in demand to the graph.

### increase()
`increase()` will add a demand curve showing an incerase in demand to the graph.
### slope_up()
`slope_up()` will increase (make steeper) the slope of the demand curve.
### slope_down()
`slope_down()` will decrease (make flatter) the slope of the demand curve.
### slope_vertical()
`slope_vertical()` will make the slope of the demand curve vertical.
### slope_horizontal()
`slope_horizontal()` will make the slope of the demand curve horizontal.
### trace_point(x, y)
`trace_point` takes in two numbers representing the x and y coordinates of a point.  It will draw a dashed line from the point to the x- and y-axis.


## SupplyCurve()
`SupplyCurve()` will add a supply curve to be plotted on the graph.

### decrease()
`decrease()` will add a supply curve showing a decrease in demand to the graph.
### increase()
`increase()` will add a supply curve showing an incerase in demand to the graph.
### slope_up()
`slope_up()` will increase (make steeper) the slope of the supply curve.
### slope_down()
`slope_down()` will decrease (make flatter) the slope of the suppply curve.
### slope_vertical()
`slope_vertical()` will make the slope of the supply curve vertical.
### slope_horizontal()
`slope_horizontal()` will make the slope of the supply curve horizontal.
### trace_point(x, y)
`trace_point` takes in two numbers representing the x and y coordinates of a point.  It will draw a dashed line from the point to the x- and y-axis.

## Schedule()
`Schedule()` takes in a list of coordinates and plots a line based on the points given.
A list is denoted by square brackets: `[]`.
A single set of coordinates is denoted by parentheses consisting of two numbers: `(1, 2)`
```
# This will draw a line that consists of points (1,2), (3,4), (5,6). 
Schedule([(1,2), (3,4), (5,6)])
```

## PPC 
`PPC()` adds a production possibilities curve to the graph.  `PPC()` should not be used with `SupplyCurve()` or `DemandCurve()` on the same graph.
### increase()
`increase()` adds a PPC to the graph showing an increased production possibilities curve.
### decrease()
`decrease()` adds a PPC to the graph showing a decreased proudction possibilities curve.