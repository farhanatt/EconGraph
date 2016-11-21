#EconGraph

## How to use the DSL
Install jupyter notebook from this link: http://jupyter.org/install.html

Run `jupyter notebook` in your terminal, which will launch the notebook in your
browser.  You'll be taken to a UI that lists your local files.

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


