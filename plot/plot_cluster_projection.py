# -*- coding: utf-8 -*-
#
# spikeval - plot.plot_cluster_projection.py
#
# Philipp Meier <pmeier82 at googlemail dot com>
# 2011-09-29
#

"""scatter plot for clustering data"""
__author__ = 'Philipp Meier <pmeier82 at googlemail dot com>'
__docformat__ = 'restructuredtext'
__all__ = ['cluster_projection']


##---IMPORTS

import scipy as sp
from scipy import linalg as sp_la
from scipy.stats import norm
from common import COLOURS, save_figure, check_plotting_handle, plt


##---FUNCTION

def cluster_projection(data, colours=None, plot_handle=None, filename=None,
                       show=True):
    """produce a plot with the cluster projections according to [citation]

    :Parameters:
        data : dict
            dict with cluster data in one ndarray (one observation per row).
            This data has to be whitened so the distance measure actually make
            sense!
        colours : list
            List of colours in any matplotlib conform colour representation
            Default=None
        plot_handle : figure or axis
            A reference to a figure or axis, or None if one has to be created.
        filename : str
            It given and a valid path on the local system, save the figure.
        show : bool
            If True, show the figure.
    :Returns:
        matplotlib.figure
            Reference th the figure ploted on
    """

    # prepare data
    if not isinstance(data, dict):
        data = {'0':data}
    nu = len(data)
    if nu < 2:
        raise ValueError('only one unit passed!')

    # colour list
    if colours is None:
        col_lst = COLOURS
    else:
        col_lst = colours

    # setup figure if necessary
    fig, ax = check_plotting_handle(plot_handle, create_ax=False)
    fig.clear()

    # plot pairwise inter-cluster distributions
    GAUSS_UNIT_SIGMA = norm.pdf(sp.linspace(-4, 4, 51))
    axidx = 0
    for row in xrange(nu - 1):
        for col in xrange(nu - 1 - row):
            # create subplot at correct position
            myax = fig.add_subplot(nu - 1, nu - 1, row * nu + col + 1)
            axidx += 1
            # whiten data and calc cluster means and connecting vectors
            clusterA = data[sorted(data.keys())[row]]
            clusterAmean = clusterA.mean(axis=0)
            clusterAproj = sp.array(clusterA.shape[0])
            clusterB = data[sorted(data.keys())[row + col + 1]]
            clusterBmean = clusterB.mean(axis=0)
            clusterBproj = sp.array(clusterB.shape[0])
            # project on vector connecting the cluster means
            con = clusterAmean - clusterBmean
            con = con / sp_la.norm(con)
            clusterAproj = sp.dot(clusterA, con)
            clusterAmean_proj = sp.dot(clusterAmean, con)
            clusterBproj = sp.dot(clusterB, con)
            clusterBmean_proj = sp.dot(clusterBmean, con)
            # plot histos
            myax.hist(clusterAproj, 50, align='mid', normed=True,
                      facecolor=col_lst[row % len(col_lst)],
                      edgecolor=col_lst[row % len(col_lst)])
            myax.hist(clusterBproj, 50, align='mid', normed=True,
                      facecolor=col_lst[(row + col + 1) % len(col_lst)],
                      edgecolor=col_lst[(row + col + 1) % len(col_lst)])
            # plot gauss
            myax.plot(
                sp.linspace(clusterAmean_proj - 4, clusterAmean_proj + 4, 51),
                GAUSS_UNIT_SIGMA, color='k')
            myax.plot(
                sp.linspace(clusterBmean_proj - 4, clusterBmean_proj + 4, 51),
                GAUSS_UNIT_SIGMA, color='k')
            # jail yaxis
            myax.set_ybound(0.0, 0.5)
            myax.set_yticklabels([])

    # produce plots
    if filename is not None:
        save_figure(fig, filename, '')
    if show is True:
        plt.show()
    return fig

##---MAIN

if __name__ == '__main__':
    # get a figure
    f = plt.figure()

    # get some data
    my_data = {0:sp.randn(900, 2), 1:sp.randn(700, 2) + 5,
               2:sp.randn(500, 2) - 5, 3:sp.randn(300, 2) - 10,
               4:sp.randn(100, 2) + 10}

    # call the plot function on the axes
    f_ret = cluster_projection(my_data, plot_handle=f)
    print f == f_ret
