# -*- coding: utf-8 -*-
#
# spikeplot - plot_mcdata.py
#
# Philipp Meier <pmeier82 at googlemail dot com>
# 2011-09-29
#

"""scatter plot for clustering data"""
__docformat__ = "restructuredtext"
__all__ = ["mcdata"]

## IMPORTS

import scipy as sp
from .common import COLOURS, save_figure, check_plotting_handle, plt, mpl

## FUNCTIONS

def mcdata(data, other=None, x_offset=0, div=2, zero_line=True, events=None,
           epochs=None, plot_handle=None, colours=None, title=None,
           filename=None, show=True):
    """plot multichanneled data

    -> general plot parameter

    :type data: ndarray
    :param data: The base data to plot with observations(samples) on the rows
        and variables(channels) on the columns. This data will be plotted on in
        the n topmost axes.
    :type other: ndarray
    :param other: Other data that augments the base data. The other data will
        be plotted in one axe visibly divided from the base data.
        Default=None
    :type x_offset: int
    :param x_offset: A offset value for the x-axis(samples). This allows for
        the x-axis to show proper values for windows not starting at x=0. All
        values for events and epochs etc. will not be shown if they do not
        fall into the frame defined.
        Default=0
    :type div: float
    :param div: Percentage of the figure height to use as divider for the
        others plot.
        Default=1
    :type zero_line: bool
    :param zero_line: if True, mark the zero line for the data channels
        Default=True
    :type events: dict
    :param events: dict of events from [x_offset, x_offset+len(data)]. If the
        dict entries are lists/ndarrays, vertical markers will be placed at
        these samples. If the dict entries are tuples of length 2, like
        (ndarray,ndarray), the first is interpreted as the waveform, and the
        second as the events. Each unit will be coloured according to the
        'colours' vector.
        Default={}
    :type epochs: dict
    :param epochs: dict of epochs from [x_offset, x_offset+len(data)]. Epochs
        with numeric keys will be interpreted as belonging to the unit with
        that key and will be coloured according to the '' vector. All other
        epochs will appear in grey colour. Epochs are passed as a 2dim vector,
        like [[start,stop]].
        Default={}
    """

    # checks
    if not isinstance(data, sp.ndarray):
        raise ValueError("data is no ndarray!")
    if data.ndim != 2:
        raise ValueError("data is not dim=2!")
    fig, ax = check_plotting_handle(plot_handle, create_ax=False)

    # init
    fig.clear()
    has_other = other is not None
    ns, nc = data.shape
    x_vals = sp.arange(ns) + x_offset
    if colours is None:
        col_lst = COLOURS
    elif colours == 'black':
        col_lst = ['k'] * nc
    else:
        col_lst = colours
    ax_spacer = div * 0.01

    # prepare axes
    if has_other:
        ax_height = (0.8 - (nc + 1) * ax_spacer) / (nc + 1)
    else:
        ax_height = (0.8 - (nc - 1) * ax_spacer) / nc
    for c in xrange(nc):
        ax_size = (
            0.1, 0.9 - (c + 1) * ax_height - c * ax_spacer, 0.8, ax_height)
        ax = fig.add_axes(ax_size, sharex=ax, sharey=ax)
        ax.set_ylabel('CH %d' % c)
        if c != nc - 1:
            plt.setp(ax.get_xticklabels(), visible=False)
            #ax.set_xticklabels([tl.get_text() for tl in ax.get_xticklabels()], visible=False)
            #ax.set_xlim(x_vals[0], x_vals[-1])
            #ax.set_ylim(data.min() * 1.1, data.max() * 1.1)
    if has_other:
        ax = fig.add_axes((0.1, 0.1, 0.8, ax_height), sharex=ax)
        ax.set_ylabel('OTHER')
        #ax.set_xlim(x_vals[0], x_vals[-1])
        #ax.set_ylim(-other.max() * 1.1, other.max() * 1.1)

    # plot data
    for c, a in enumerate(fig.axes[:nc]):
        a.add_collection(
            mpl.collections.LineCollection(
                [sp.vstack((x_vals, data[:, c])).T], colors=[(0, 0, 0)]))

    # plot other
    if has_other:
        fig.axes[-1].add_collection(mpl.collections.LineCollection(
            [sp.vstack((x_vals, other[:, c])).T for c in
             xrange(other.shape[1])], colors=col_lst))

    # plot events
    if events is not None:
        for u in sorted(events):
            try:
                col = col_lst[u % len(col_lst)]
            except:
                col = 'gray'
            if isinstance(events[u], tuple):
                if len(events[u]) != 2:
                    raise ValueError('Event entry for unit %s is not a tuple '
                                     'of length 2' % u)
                u_wf, u_ev = events[u]
                if not u_wf.shape[1] == nc:
                    raise ValueError('Waveform for unit %s has mismatching '
                                     'channel count' % u)
                cut = int(sp.floor(u_wf.shape[0] / 2.0))
                for c, a in enumerate(fig.axes[:nc]):
                    a.add_collection(
                        mpl.collections.LineCollection(
                            [sp.vstack((sp.arange(u_wf.shape[0]) - cut + u_ev[i],
                                        u_wf[:, c])).T
                             for i in xrange(u_ev.size)], colors=[col]))
                if has_other:
                    for e in u_ev:
                        fig.axes[-1].axvline(e, c=col)
            elif isinstance(events[u], (list, sp.ndarray)):
                for a in fig.axes:
                    for e in events[u]:
                        a.axvline(e, c=col)
            else:
                raise ValueError('events for unit %s are messed up' % u)

    # plot epochs
    if epochs is not None:
        for u in sorted(epochs):
            try:
                col = col_lst[u % len(col_lst)]
            except:
                col = 'gray'
            for ep in epochs[u]:
                for a in fig.axes:
                    a.axvspan(ep[0], ep[1], fc=col, alpha=0.2)

    # zero lines
    if zero_line:
        for a in fig.axes:
            a.add_collection(
                mpl.collections.LineCollection(
                    [sp.vstack(([x_vals[0], x_vals[-1]], sp.zeros(2))).T],
                    linestyles='dashed',
                    colors=[(0, 0, 0)]))

    # scale axes
    fig.axes[0].set_xlim(x_vals[0], x_vals[-1])
    fig.axes[0].set_ylim(sp.nanmin(data) * 1.05, sp.nanmax(data) * 1.05)
    if has_other:
        fig.axes[-1].set_ylim(sp.nanmin(other) * 1.1, sp.nanmax(other) * 1.1)

    # figure title
    if title is not None:
        fig.suptitle(title)

    # produce plot
    if filename is not None:
        save_figure(fig, filename, '')
    if show is True:
        plt.show()

    # return
    return fig

##--- MAIN

if __name__ == '__main__':
    pass
