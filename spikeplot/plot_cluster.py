# -*- coding: utf-8 -*-
#
# spikeplot - plot_cluster.py
#
# Philipp Meier <pmeier82 at googlemail dot com>
# 2011-09-29
#

"""scatter plot for clustering data"""
__docformat__ = 'restructuredtext'
__all__ = ['cluster']


##---IMPORTS

from common import COLOURS, save_figure, check_plotting_handle, mpl, plt


##---FUNCTION

def cluster(data, data_dim=(0, 1), plot_handle=None, plot_mean=True,
            colours=None, title=None, xlabel=None, ylabel=None, filename=None,
            show=True):
    """plot a set of clusters with different colors each

    :Parameters:
        data : object
            Preferably a dictionary with ndarray entries.
        data_dim : tuple
            A 2-tuple giving the dimension (entries per datapoint/columns) to
            use for the scatter plot of the cluster.
        plot_handle : figure or axis
            A reference to a figure or axis, or None if one has to be created.
        plot_mean : bool or float
            If False, do nothing. If True or positive integer,
            plot the cluster
            means with a strong cross, if positive float, additionally plot a
            unit circle of that radius (makes sense for prewhitened pca data),
            thus interpreting the value as the std of the cluster.
            Default=True
        colours : list
            List of colors in any matplotlib conform colour representation
            Default=None
        title : str
            A title for the plot. No title if None or ''.
        xlabel : str
            A label for the x-axis. No label if None or ''.
        ylabel : str
            A label for the y-axis. No label if None or ''.
        filename : str
            It given and a valid path on the local system, save the figure.
        show : bool
            If True, show the figure.
    :Returns:
        matplotlib.figure
            Reference th the figure plotted on
    """

    # colour list
    if colours is None:
        col_lst = COLOURS
    else:
        col_lst = colours

    # setup Figure if necessary
    fig, ax = check_plotting_handle(plot_handle)

    if not isinstance(data, dict):
        data = {'0':data}

    # plot single cluster members
    col_idx = 0
    for k in sorted(data.keys()):
        ax.plot(
            data[k][:, data_dim[0]],
            data[k][:, data_dim[1]],
            marker='.',
            lw=0,
            c=col_lst[col_idx % len(col_lst)])
        col_idx += 1

    # plot cluster means
    if plot_mean is not False:
        col_idx = 0
        for k in sorted(data.keys()):
            my_mean = data[k][:, data_dim].mean(axis=0)
            ax.plot(
                [my_mean[0]],
                [my_mean[1]],
                            lw=0,
                            marker='x',
                            mfc=col_lst[col_idx % len(col_lst)],
                            ms=10,
                            mew=1,
                            mec='k')

            # plot density estimates
            if plot_mean is not True:
                ax.add_artist(
                    mpl.patches.Ellipse(
                        xy=my_mean,
                        width=plot_mean * 2,
                        height=plot_mean * 2,
                        facecolor='none',
                        edgecolor=col_lst[col_idx % len(col_lst)]))
            col_idx += 1

    # fancy stuff
    if title is not None:
        ax.set_title(title)
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)

    # produce plots
    if filename is not None:
        save_figure(fig, filename, '')
    if show is True:
        plt.show()
    return fig

##---MAIN

if __name__ == '__main__':
    pass
