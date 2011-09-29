# -*- coding: utf-8 -*-
#
# spikeval - plot.common.py
#
# Philipp Meier <pmeier82 at googlemail dot com>
# 2011-09-29
#

"""basic stuff for plotting"""
__author__ = 'Philipp Meier <pmeier82 at googlemail dot com>'
__docformat__ = 'restructuredtext'
__all__ = ['check_plotting_handle', 'save_figure', 'COLOURS', 'plt', 'mpl']


##---IMPORTS

import os
import matplotlib as mpl
from matplotlib import pyplot as plt


##---CONSTANTS

COLOURS = [(0, 0, 1), # blue
    (0, 1, 0), # green
    (1, 0, 0), # red
    (1, 0, 1), # fuchsia
    (0, 1, 1), # aqua
    (.5, .5, .5), # gray
    (1, 1, 0), # yellow
    (.5, .5, 0), #
    (1, .5, .5), (.5, 1, .5), (0, 0, .5), # navy
    (0, .5, 0), # green
    (.5, 0, 0), # maroon
    (0, .5, .5), # teal
    (.5, 0, .5), # purple
    (.5, .5, 0), # olive
    (.2, .5, .8), (1, .1, .1), (.3, .3, .3), (0, 0, 0), # black
    (.9, .2, .9), (.2, .9, .9), (.9, .9, .2)]
"""list of RGB tuples to use for unified colours across the plots

usage:
    for i in xrange(huge_number):
        ax.plot(myline[i], c=COLOURS[i%NCOL])
"""


##---FUNCTIONS

def check_plotting_handle(something, spid=(1, 1, 1), create_ax=True):
    """check if something is a valid axes or figure handle

    :Parameters:
        something : object
            object to be checked, can be None, a new figure will be created in
            this case
        spid : tuple
            subplot id in (col, row, id) notation
        create_ax : bool
            If True, create an axis.
    :Returns:
        matplotlib.figure
            Reference to the figure in question.
        matplotlib.axis
            Reference to the axis in question.
    """

    fig = ax = None
    if something is None:
        fig = plt.figure()
        if create_ax is True:
            ax = fig.add_subplot(*spid)
    elif isinstance(something, plt.Axes):
        ax = something
        fig = something.get_figure()
    elif isinstance(something, (list, tuple)):
        if isinstance(something[0], plt.Axes):
            ax = something
            fig = something[0].get_figure()
    elif isinstance(something, plt.Figure):
        fig = something
        if create_ax is True:
            ax = something.add_subplot(*spid)
    else:
        raise ValueError('Either figure or axes handle has to be given')
    return fig, ax


def save_figure(fig, file_name, file_dir='.', desc='', formats=('png',)):
    """save `fig` to `file_name` in each of the `formats` passed.

    :Parameters:
        fig : matplotlib.Figure
            The figure handle to save.
        file_name : str
            The file destination filename of the savefile.
        file_dir : str
            The directory where the figure is stored.
            Default='.'
        desc : str
            The desc string will be added to the filename to describe the
            figure.
            Default=''
        formats : (str, ..)
            A tuple of strings that are recognised by the savefig method.
            Leading
            to one file per format.
            Default=('png',)
    """

    save_path = os.path.join(os.path.abspath(file_dir),
                             ''.join([file_name, desc]))

    for file_format in formats:
        try:
            fig.savefig(''.join([save_path, '.', file_format]), format=format)
        except:
            pass

##---MAIN

if __name__ == '__main__':
    pass
