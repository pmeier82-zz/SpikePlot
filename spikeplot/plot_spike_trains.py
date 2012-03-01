# -*- coding: utf-8 -*-
#
# spikeplot - plot_spike_trains.py
#
# Philipp Meier <pmeier82 at googlemail dot com>
# 2011-09-29
#

"""scatter plot for clustering data"""
__docformat__ = 'restructuredtext'
__all__ = ['spike_trains']


##---IMPORTS

import scipy as sp
from .common import COLOURS, save_figure, check_plotting_handle, plt


##---FUNCTION

def spike_trains(spiketrains, spiketrains2=None, alignment=None,
                 marker_width=3, samples_per_second=None, plot_handle=None,
                 filename=None, label1=None, label2=None, colours=None,
                 show=True):
    """plot one set of spike trains or two sets of spike trains with their
    inter-spike alignment

    :Parameters:
        spiketrains : dict
            Dict of 1d ndarray, holding the spike times.
        spiketrains2 : dict
            Dict of 1d ndarray, holding the spike times. If this is given an
            interspike assignment plot is created.
        alignment : list
            List of lists of tupels containing the pairwise spike alignments.
        marker_width : int
            Fancy parameter for the plot.
        samples_per_second : int
            Scale parameter for the axis.
        plot_handle : figure or axis
            A reference to a figure or axis, or None if one has to be created.
        filename : str
            If given and a valid path on the local system, save the figure.
        label1 : str
            Label for interspike alignment set 1.
        label2 : str
            Label for interspike alignment set 2.
        show : bool
            If True, show the figure.
    :Returns:
        matplotlib.figure
            Reference th the figure ploted on
    """

    # checks
    if not len(spiketrains):
        raise Exception('Provide at least one spiketrain in set 1!')

    # colour list
    if colours is None:
        col_lst = COLOURS
    else:
        col_lst = colours

    # setup figure if necessary
    fig, ax = check_plotting_handle(plot_handle)

    # init
    nneuron = len(spiketrains)
    if samples_per_second is None:
        srate = 1.0
    else:
        srate = float(samples_per_second)
    offset = 0
    if spiketrains2 is not None:
        nneuron += len(spiketrains2)
        offset = 1
    labels = []
    idx = 0

    # plot the spike trains
    my_max_timesample = 0
    my_min_timesample = spiketrains[spiketrains.keys()[0]][0]
    for unit in sorted(spiketrains.keys()):
        col = col_lst[idx % len(col_lst)]
        ax.plot(
            spiketrains[unit] / srate,
            sp.zeros_like(spiketrains[unit]) + nneuron - 1 - idx,
            marker='|',
            mec=col,
            mfc=col,
            mew=marker_width,
            ls='None',
            ms=13)
        labels.append('Unit %s' % unit)
        idx += 1
        my_max_timesample = max(my_max_timesample, spiketrains[unit].max())
        my_min_timesample = max(my_min_timesample, spiketrains[unit].min())

    if spiketrains2 is not None:
        labels.append('')
        ax.axhline(y=nneuron - 1 - idx, xmin=0, xmax=1)
        for unit in sorted(spiketrains2.keys()):
            col = col_lst[idx % len(col_lst)]
            ax.plot(spiketrains2[unit] / srate, sp.zeros_like(
                spiketrains2[unit]) + nneuron - 1 - idx - offset, marker='|',
                    mec=col,
                    mfc=col,
                    mew=marker_width,
                    ls='None',
                    ms=13)
            labels.append('Unit %s' % unit)
            idx += 1
            my_max_timesample = max(my_max_timesample,
                                    spiketrains2[unit].max())
            my_min_timesample = max(my_min_timesample,
                                    spiketrains2[unit].min())

    # plot alignment if provided
    if alignment is not None:
        if spiketrains2 is None:
            skeys = sorted(spiketrains.keys())

            for idx1 in xrange(len(skeys)):
                unit1 = skeys[idx1]
                for idx2 in xrange(idx1 + 1, len(skeys)):
                    unit2 = skeys[idx2]
                    for i in xrange(len(alignment[(unit1, unit2)])):
                        start = spiketrains[unit1][
                                alignment[(unit1, unit2)][i][0]] / srate
                        end = spiketrains[unit2][
                              alignment[(unit1, unit2)][i][1]] / srate
                        ax.plot(
                            (start, end),
                            (nneuron - idx1 - 1,
                             nneuron - idx2 - 1),
                                        c=(0, 0, 0),
                                        ls=":")
        else:
            skeys1 = sorted(spiketrains.keys())
            skeys2 = sorted(spiketrains2.keys())

            for idx1 in xrange(len(skeys1)):
                unit1 = skeys1[idx1]
                for idx2 in xrange(len(skeys2)):
                    unit2 = skeys2[idx2]
                    for i in xrange(len(alignment[(unit1, unit2)])):
                        start = spiketrains[unit1][
                                alignment[(unit1, unit2)][i][0]] / srate
                        end = spiketrains2[unit2][
                              alignment[(unit1, unit2)][i][1]] / srate
                        ax.plot(
                            (start, end),
                            (nneuron - idx1 - 1,
                             nneuron - len(skeys1) -
                             idx2 - 1 - offset),
                                        c=(0, 0, 0),
                                        ls=":")

    # plot spike labels if provided
    labelList = ['TP', 'TPO', 'FP', 'FPA', 'FPAO', 'FN', 'FNO']
    if label1 is not None:
        idx = 0
        for unit in sorted(spiketrains.keys()):
            for i in xrange(len(label1[unit])):
                if label1[unit][i] - 1 > 1:
                    stri = labelList[label1[unit][i] - 1]
                    ax.text(spiketrains[unit][i] / srate, nneuron - 1 - idx,
                            stri)
            idx += 1
    if label2 is not None and spiketrains2 is not None:
        for unit in sorted(spiketrains2.keys()):
            for i in xrange(len(label2[unit])):
                if label2[unit][i] - 1 > 1:
                    stri = labelList[label2[unit][i] - 1]
                    ax.text(spiketrains2[unit][i] / srate,
                            nneuron - 1 - idx - offset, stri)
            idx += 1

            # beautfy the figure
            #    fig_ax.set_title('spiketrains all units')
    if srate is 1:
        ax.set_xlabel('time in samples')
    else:
        ax.set_xlabel('time in seconds')
        #    ax.set_ylabel('')
    ax.set_yticks(sp.arange(nneuron + offset) - offset)
    ax.set_yticklabels(labels[::-1])
    ax.set_ylim((-0.5 - offset, nneuron - .5))
    #    ax.set_xlim((my_min_timesample-1, my_min_timesample+1))

    # produce plots
    if filename is not None:
        save_figure(fig, filename, '')
    if show is True:
        plt.show()
    return fig

##---MAIN

if __name__ == '__main__':
    pass
