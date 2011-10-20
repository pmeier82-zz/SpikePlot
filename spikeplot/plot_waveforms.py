# -*- coding: utf-8 -*-
#
# spikeplot - plot_waveforms.py
#
# Philipp Meier <pmeier82 at googlemail dot com>
# 2011-09-29
#

"""scatter plot for clustering data"""
__docformat__ = 'restructuredtext'
__all__ = ['waveforms']


##---IMPORTS

import scipy as sp
from .common import COLOURS, save_figure, check_plotting_handle, plt


##---FUNCTION

def waveforms(waveforms, samples_per_second=None, tf=None, plot_mean=False,
              plot_single_waveforms=True, set_y_range=False,
              plot_separate=True, plot_handle=None, colours=None, title=None,
              filename=None, show=True):
    """plot one set of spiketrains or two sets of spkitrains with their
    interspike alignment

    :Parameters:
        waveforms : dict
            Dict of ndarray, holding the waveforms for different units.
        plot_handle : figure or axis
            A reference to a figure or axis, or None if one has to be created.
        samples_per_second : int
            Scale factor for the axis.
        tf : int
            The template length of the waveforms
        plot_mean : bool
            If True, plot the mean-waveform per unit.
        plot_single_waveforms : bool
            If True, plot the single waveforms per unit.
        plot_separate : bool
            If True, plot each units waveforms in a separate axis.
        set_y_range : bool
            Adjust the y-axis range so waveforms fit in nicely.
        colours : list
            A list of matplotlib conform color values (rgb 3-tuples). If None
            the common.plot.COLORS set is used.
        title : str
            Title for the plot. No title if None or ''.
        filename : str
            If given and a valid path on the local system, save the figure.
        show : bool
            If True, show the figure.
    :Returns:
        matplotlib.figure
            Reference th the figure ploted on
        matplotlib.axis
            Reference to the axis ploted on
    """

    # setup figure if necessary
    fig, ax = check_plotting_handle(plot_handle, create_ax=not plot_separate)
    if plot_separate is True:
        fig.clear()
        ax = None

    # checks and inits
    if type(waveforms) is not dict:
        waveforms = {'0':waveforms}
    if colours is None:
        col_lst = COLOURS
    else:
        col_lst = colours
    srate = 1.0
    if samples_per_second is not None:
        srate = samples_per_second
    for k in waveforms.keys():
        if waveforms[k].ndim == 3:
            waveforms[k] = sp.vstack(
                [sp.hstack(
                    [waveforms[k][i, :, j]
                     for j in xrange(waveforms[k].shape[-1])])
                 for i in xrange(waveforms[k].shape[0])])
    firstKey = waveforms.keys()[0]
    nunits = len(waveforms)
    my_ymin = waveforms[firstKey].min()
    my_ymax = waveforms[firstKey].max()
    my_xmax = waveforms[firstKey].shape[1] - 1

    nc = 1
    if tf is not None:
        nc = int(waveforms[firstKey].shape[1] / tf)

    # plot single wave forms
    if plot_single_waveforms is True:
        col_idx = 0
        for u, k in enumerate(sorted(waveforms.keys())):
            if plot_separate is True:
                ax = fig.add_subplot(nunits, 1, u + 1, sharex=ax, sharey=ax)
            nsample = waveforms[k].shape[1]
            my_ymin = min(my_ymin, waveforms[k].min())
            my_ymax = max(my_ymax, waveforms[k].max())
            my_xmax = max(my_xmax, waveforms[k].shape[1] - 1)
            col = col_lst[col_idx % len(col_lst)]
            if plot_mean is True:
                col = 'gray'
            for i in xrange(waveforms[k].shape[0]):
                ax.plot(sp.arange(nsample) / srate, waveforms[k][i, :],
                        color=col)
            col_idx += 1

    # plot cluster means
    if plot_mean is True:
        col_idx = 0
        for u, k in enumerate(sorted(waveforms.keys())):
            if plot_separate is True:
                ax = fig.axes[u]
            my_mean = waveforms[k].mean(axis=0)
            my_ymin = min(my_ymin, my_mean.min())
            my_ymax = max(my_ymax, my_mean.max())
            my_xmax = max(my_xmax, my_mean.size - 1)
            ax.plot(sp.arange(nsample) / srate, my_mean,
                    c=col_lst[col_idx % len(col_lst)], lw=2)
            col_idx += 1

    # if multichannel waveforms, plot vertical lines at channel borders
    if tf is not None:
        for i in xrange(1, nc):
            for a in fig.axes:
                a.axvline((tf * i) / srate, ls='dashed', color='y')

    # fancy stuff
    if title is not None:
        fig.suptitle(title)
    if samples_per_second is not None:
        ax.set_xlabel('time in seconds')
    else:
        ax.set_xlabel('time in samples')
    ax.set_xlim(0, my_xmax)
    ax.set_ylabel('amplitude')
    if set_y_range is True:
        ax.set_ylim((1.01 * my_ymin, 1.01 * my_ymax))

    # produce plots
    if filename is not None:
        save_figure(fig, filename, '')
    if show is True:
        plt.show()
    return fig

##--- MAIN

if __name__ == '__main__':
    pass
