from distutils.core import setup, Extension

ext = Extension('std', 
        sources=[
            'std.cpp',
            'std-wrapper.cpp',
            ],
        )

setup(name='std_performance',
      version='1.0',
      description='Module for calculating standard deviation.',
      ext_modules=[ext])
