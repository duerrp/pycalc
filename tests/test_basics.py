"""Tests the basic functionality of pycalc
"""

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import

import unittest

# pylint: disable=no-name-in-module
from pycalc import sp
from pycalc import x, y, z, alpha, beta, gamma
from pycalc import np
from pycalc import sc


class PycalcBasics(unittest.TestCase):
    """Basic tests for pycalc
    """
    def test_sympy_module(self):
        """Test if sympy module is working"""
        self.assertEqual(sp.factorint(257), {257: 1})

    def test_sympy_vars(self):
        """Test if sympy variables are there"""
        self.assertEqual(x**2, x*x)
        self.assertEqual(x * y / x, y)
        self.assertEqual(sp.simplify(sp.sin(z)**2 + sp.cos(z)**2), 1)
        self.assertEqual(sp.simplify(gamma / 3 * 3 / gamma), 1)
        self.assertEqual(sp.simplify(alpha**0), 1)
        self.assertEqual(sp.simplify(beta**2), beta * beta)

    def test_numpy(self):
        """Test if numpy is available"""
        self.assertTrue(np.all(np.ones(10) > np.zeros(10)))

    def test_scipy(self):
        """Test if scipy is available"""
        self.assertTrue(sc.e > 0)


if __name__ == '__main__':
    unittest.main()
