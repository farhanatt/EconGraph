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

## API 