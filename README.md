# PythonCExtensions
Using a Python C extension and comparing its performance to NumPy and Python

You need to build the C extension before running this. To build and install the extension run:

```python
$ python3 setup.py install
```

stdtest.py has a main method which will compare Python, NumPy and the C extension for small arrays and plot the performance with matplotlib.

*I've modified the wrapper to work both Python 2 and 3.*

## Results
100 ~ 1,000 elements

<img src="https://user-images.githubusercontent.com/1250095/39954390-9a5fed02-55f9-11e8-842b-b430bb2c3d5b.png" width="70%" />

100 ~ 50,000 elements

<img src="https://user-images.githubusercontent.com/1250095/39954391-9a870180-55f9-11e8-9758-4b5650429e6e.png" width="70%" />

## Dependencies
### Cython
```
$ pip3 install Cython
```
### Pybind11
```
$ brew install pybind11
```

## References
- [Speeding up Python and NumPy: C++ing the Way](https://medium.com/coding-with-clarity/speeding-up-python-and-numpy-c-ing-the-way-3b9658ed78f4)
