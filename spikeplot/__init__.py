# -*- coding: utf-8 -*-
#
# spikeplot - __init__.py
#
# Philipp Meier <pmeier82 at googlemail dot com>
# 2011-09-29
#

"""plotting package for spike sorting"""
__docformat__ = 'restructuredtext'
__version__ = '0.1.4'

## MATPLOTLIB

import matplotlib
import os
import platform

if platform.system() == 'Windows':
    matplotlib.use('TkAgg')
else:
    if os.getenv('DISPLAY') is None:
        # we need to use AGG backend here!
        matplotlib.use('Agg')
del matplotlib, os, platform

## PACKAGE

from .common import check_plotting_handle, save_figure, COLOURS, plt, mpl
from .plot_cluster import cluster
from .plot_cluster_projection import cluster_projection
from .plot_mcdata import mcdata
from .plot_spike_trains import spike_trains
from .plot_waveforms import waveforms
from .plot_xvf_tensor import xvf_tensor

## MAIN

if __name__ == '__main__':
    pass

## EOF
