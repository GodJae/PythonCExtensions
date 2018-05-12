from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension('stdcy',
                sources=[
                    'stdcy.pyx',
                    'std.cpp',
                ],
                language='c++',
                )

setup(name='std_performance_cy',
      version='1.0',
      description='Module for calculating standard deviation.',
      ext_modules=cythonize(ext))
