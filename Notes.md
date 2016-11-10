# EconGraph Notes

## Graphs to support 
production possibilities

(aggregate) supply
(aggregate) demand
long run supply

money market
investment demand

phillips curve
utility curve

default Monopoly graph:
marginal cost, average cost, marginal revenue, demand = average revenue



##Potential syntaxes

```
import EconGraph

graph = econgraph.Graph() // Create graph object

graph.SupplyCurve() // Creates default supply curve
	.slope(up)	// Supply curve slope steeper
	.shift(increase) // Supply shifts out (increase in supply), sets slope of supply curve

graph.SupplyCurve() // Creates default supply curve
	.slope(vertical) // Vertical supply (LR supply)

graph.Axes()
	.yscale(1, 5)
	.xscale(1,5)
```

Graph object is just some object that stores the different curves/axes set.
Implementation would be some object curve that has methods slope, shift, etc.,
which are setters on a curve object.
Then all curves would extend curve object


```
import EconGraph


Jupyter 'magic'

