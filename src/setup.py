from setuptools import setup
from Cython.Build import cythonize

import os.path

dirname = os.path.dirname(__file__)

pyx_path = os.path.join(dirname, 'fib.pyx')

setup(ext_modules=cythonize(pyx_path))