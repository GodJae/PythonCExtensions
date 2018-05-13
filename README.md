# PythonCExtensions
Using a Python C extension and comparing its performance to NumPy and Python

You need to build the C extension before running this. To build and install the extension run:

```
$ python3 setup.py install
```

stdtest.py has a main method which will compare Python, NumPy and the C extension for small arrays and plot the performance with matplotlib.

*I've modified the wrapper to work both Python 2 and 3.*

## Results
<img src="https://user-images.githubusercontent.com/1250095/39965454-da4df776-56d3-11e8-9205-ca02d1d18726.png" width="70%" />

<img src="https://user-images.githubusercontent.com/1250095/39965456-da7554ec-56d3-11e8-8951-88c1889e9293.png" width="70%" />

<img src="https://user-images.githubusercontent.com/1250095/39965457-da9be8be-56d3-11e8-8f32-e74dcc68db7c.png" width="70%" />

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
- [NumPy와 C++ Extensions의 성능 비교](http://docs.likejazz.com/python-numpy-extensions/)
