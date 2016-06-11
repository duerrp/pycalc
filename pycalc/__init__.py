"""Pcalc, use python as a calculator - from pycalc import *

Written by Peter Duerr
"""
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import os
import dill
import __main__ as _main_module
import six

if six.PY2:
    PYCALC_SESSION_NAME = os.path.expanduser("~/.pycalc_session")
elif six.PY3:
    PYCALC_SESSION_NAME = os.path.expanduser("~/.pycalc3_session")
else:
    print("Python version not supported")

try:
    dill.load_session(PYCALC_SESSION_NAME)
except IOError:
    print("Re-loading pycalc modules...")
    import numpy as np
    _main_module.np = np

    import scipy as sc
    _main_module.sc = sc

    import sympy as sp
    import sympy.physics
    _main_module.sp = sp
    _main_module.u = sp.physics.units
    _main_module.u.B = sympy.physics.units.Unit('byte', 'B')
    _main_module.u.b = sympy.Rational(1, 8) * sympy.physics.units.B
    _main_module.u.KiB = 1024 * sympy.physics.units.B
    _main_module.u.MiB = 1024**2 * sympy.physics.units.B

    import pandas as pd
    _main_module.pd = pd

    from matplotlib import pyplot as plt
    _main_module.plt = plt

    import seaborn as sns
    _main_module.sns = sns

    dill.dump_session(PYCALC_SESSION_NAME, main=_main_module)


def setup_plotting():
    """Better defaults for plotting
    """
    import matplotlib
    import seaborn as sns

    font = {'family': 'normal',
            'weight': 'normal',
            'size': 14}

    matplotlib.rc('font', **font)

    matplotlib.rc('text', usetex=True)
    matplotlib.rc('lines', linewidth=4)
    matplotlib.rc('figure', facecolor='white')

    label_size = 14
    matplotlib.rc('xtick', labelsize=label_size)
    matplotlib.rc('ytick', labelsize=label_size)

    sns.set_style('darkgrid')
    sns.set_palette('colorblind',
                    desat=0.6)
