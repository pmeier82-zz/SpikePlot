# -*- coding: utf-8 -*-
# This file is part of the package SpikePy that provides signal processing
# algorithms tailored towards spike sorting. 
#
# Authors: Philipp Meier and Felix Franke
# Affiliation:
#   Bernstein Center for Computational Neuroscience (BCCN) Berlin
#     and
#   Neural Information Processing Group
#   School for Electrical Engineering and Computer Science
#   Berlin Institute of Technology
#   FR 2-1, Franklinstrasse 28/29, 10587 Berlin, Germany
#   Tel: +49-30-314 26756
#
# Date: 2011-02-25
# Copyright (c) 2011 Philipp Meier, Felix Franke & Technische Universität Berlin
# Acknowledgement: This work was supported by Deutsche Forschungs Gemeinschaft
#                  (DFG) with grant GRK 1589/1 and Bundesministerium für Bildung
#                  und Forschung (BMBF) with grants 01GQ0743 and 01GQ0410.
#
#______________________________________________________________________________
#
# This is free software; you can redistribute it and/or modify it under the
# terms of version 1.1 of the EUPL, European Union Public Licence.
# The software is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the EUPL for more details.
#______________________________________________________________________________
#


"""plot the xi vs f tensor in a grid"""
__docformat__ = 'restructuredtext'


##---ALL

__all__ = [
    'xvf_tensor'
]


##---IMPORTS

from plot import P, save_figure, check_plotting_handle
from common import mcvec_to_conc


##---FUNCTION

def xvf_tensor(
    # xvf_tensor
    data,
    nc=4,
    data_trans=None,
    # plot
    plot_handle=None,
    title='Xi vs F Tensor',
    filename=None,
    show=True
):
    """plots xcorrs tensor for a templates-filter set

    :Parameters:
        # xvf_tensor parameters
        data : list
            List holding [templates, filters, xvft]. Templates and filters
            are in the channel concatenated representation. xvft has dimensions
            as [time, filters, templates]
        nc : int
            Channel count for templates, and filters.
        data_trans : func
            If not None, it has to be a data transformation function or lambda
            that can be applied to the xvf tensor data.
        
        # plot parameters
        plot_handle : figure or axis
            A reference to a figure or axis, or None if one has to be created.
        title : str
            A title for the plot. No title if None or ''.
        filename : str
            If given and a valid path on the local system, save the figure.
        show : bool
            If True, show the figure.
    :Returns:
        matplotlib.figure
            Reference th the figure plotted on
        matplotlib.axis
            Reference to the axis plotted on
    """

    # checks
    fig = check_plotting_handle(plot_handle, create_ax=False)[0]
    fig.clear()
    err_str = 'data expected to be a list of ndarrays: [templates, filters, xvf-tensor data]'
    if not isinstance(data, list):
        raise TypeError(err_str)
    if len(data) != 3:
        raise ValueError(err_str)
    temps, filts, xvft = data
    if temps.shape != filts.shape:
        raise ValueError('inconsistent shapes for templates and filters')
    nitem = temps.shape[0]

    # apply data transformation
    if data_trans is not None:
        xvft = data_trans(xvft)

    # produce plot
    n1 = nitem + 1
    fmin, fmax = filts.min() * 1.1, filts.max() * 1.1
    xmin, xmax = temps.min() * 1.1, temps.max() * 1.1
    xvftmin, xvftmax = xvft.min() * 1.1, xvft.max() * 1.1
    for j in xrange(nitem):
        # j-th filter
        ax_fj = fig.add_subplot(n1, n1, n1 * (j + 1) + 1)
        ax_fj.plot(mcvec_to_conc(filts[j]))
        ax_fj.set_ylim(fmin, fmax)
        ax_fj.set_xlim((0, mcvec_to_conc(temps[0]).size))
        # j-th xi
        ax_uj = fig.add_subplot(n1, n1, j + 2)
        ax_uj.plot(mcvec_to_conc(temps[j]))
        ax_uj.set_ylim(xmin, xmax)
        ax_uj.set_xlim((0, mcvec_to_conc(temps[0]).size))
        # xcorrs
        for i in xrange(nitem):
            # the filter output of the j-th filter with the i-th unit
            ax_xcij = fig.add_subplot(n1, n1, n1 * (j + 1) + i + 2)
            ax_xcij.plot(xvft[i, j, :])
            ax_xcij.set_ylim(xvftmin, xvftmax)
            ax_xcij.set_xlim((0, xvft[i, j, :].size))

    # fancy stuff
    if title is not None:
        fig.suptitle(title)

    # produce plot
    if filename is not None:
        save_figure(fig, filename, '')
    if show is True:
        P.show()

    # return
    return fig


##---MAIN

if __name__ == '__main__':
    pass
