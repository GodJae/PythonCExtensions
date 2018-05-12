from setuptools import setup, Extension

import pybind11

ext = Extension(
    'stdpy',
    ['stdpy.cpp'],
    include_dirs=[
        pybind11.get_include(),
        pybind11.get_include(True),
    ],
    language='c++',
    extra_compile_args=['-std=c++11', '-stdlib=libc++'],
)

setup(name='std_performance_py',
      version='1.0',
      description='Module for calculating standard deviation.',
      install_requires=['pybind11>=2.2'],
      ext_modules=[ext])
