#EconGraph

## How to use the DSL
Install jupyter notebook from this link: https://jupyter.readthedocs.io/en/latest/install.html#installing-jupyter-using-anaconda-and-conda

It's essential to download from anaconda so you're able to use Python 3 notebooks.

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
DemandCurve().increase().show()
```

You should see a graph with two demand curves appear.   


