#!/usr/bin/env python
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(name="smallscript",
      py_modules=["smallscript", "functions_smsc", "readLogs", "OPA"],
      ext_modules=cythonize([Extension("Dusch_unrest", ["Dusch_unrest.pyx"]),
         Extension("Btree" ,["Btree.pyx"]),
         Extension("broaden", ["broaden.pyx"])]),
         #Extension("OPA", ["OPA.pyx"]),
      author='Tobias Moehle ',
      version='0.8',
      description='program package to calculate vibronic spectra using g09-log files. Besides the common FC-picture, also several Duschinsky-rotated approaches are implemented.',
      author_email='tobias.moehle@uni-rostock.de',
      url='https://github.com/BalticPinguin/smallscript',
     )
