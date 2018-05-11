# PythonCExtensions
Using a Python C extension and comparing its performance to NumPy and Python

You need to build the C extension before running this. To build and install the extension run:

```python
python setup.py install
```

stdtest.py has a main method which will compare Python, NumPy and the C extension for small arrays and plot the performance with matplotlib.

*I've modified the wrapper to work both Python 2 and 3.*

## Results
![](https://user-images.githubusercontent.com/1250095/39925817-1b2ae5fa-5568-11e8-9fc9-e2fd57108030.png)