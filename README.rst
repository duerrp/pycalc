PyCalc
======

|Version| |Python Version| |Build Status| |Coverage Status|

Python libraries such as numpy, sympy, and matplotlib in combination with
IPython make for an excellent desktop calculator. Unfortunately, however,
starting up an ipython session with all the necessary imports takes quite a
while. Pycalc provides a way to quickly setup all the libraries necessary for a
powerful calculator without incurring a prohibitive start up time.

Setup
-----

Pycalc can be installed from pypi by issuing ``pip install --user pycalc``.
Pycalc does not require for all it's dependencies to be installed. To get the
full pycalc experience though, run ``pip install --user -r
recommended_requirements.txt``.

Usage
-----

Pycalc can be used from the command line or in interactive mode. The command
line mode evaluates any expression given as an argument and prints the result.
The interactive mode launches an IPython session with pycalc loaded and ready to
go.


.. |Development Status| image:: https://img.shields.io/pypi/status/pycalc.svg
   :target: https://pypi.python.org/pypi/pycalc/
.. |Version| image:: https://img.shields.io/pypi/v/pycalc.svg
   :target: https://pypi.python.org/pypi/pycalc/
.. |Python Version| image:: https://img.shields.io/badge/python--version-2.7%203.2%203.3%203.4-blue.svg
   :target: https://pypi.python.org/pypi/pycalc/
.. |Build Status| image:: https://travis-ci.org/duerrp/pycalc.svg?branch=master
   :target: https://travis-ci.org/duerrp/pycalc
.. |Coverage Status| image:: https://coveralls.io/repos/duerrp/pycalc/badge.svg
   :target: https://coveralls.io/r/duerrp/pycalc
