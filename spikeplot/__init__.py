# -*- coding: utf-8 -*-
#
# spikeval - spikeplot.__init__.py
#
# Philipp Meier <pmeier82 at googlemail dot com>
# 2011-09-29
#

"""plotting package for spike sorting"""
__author__ = 'Philipp Meier <pmeier82 at googlemail dot com>'
__docformat__ = 'restructuredtext'


##---MATPLOTLIB

import matplotlib
import neo
import os

if os.getenv('DISPLAY') is None:
    # we need to use AGG backend here!
    matplotlib.use('Agg')

del matplotlib, neo, os


##---PACKAGE

from .common import *
from .plot_cluster import *
from .plot_cluster_projection import *
from .plot_mcdata import *
from .plot_spike_trains import *
from .plot_waveforms import *
from .plot_xvf import *


##---MAIN

if __name__ == '__main__':
    pass
