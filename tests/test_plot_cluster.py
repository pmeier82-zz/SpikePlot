import scipy as sp
from spikeplot import cluster

# get some data
my_data = {0:sp.randn(500, 2), 1:sp.randn(300, 2) + 2}

# call the plot function on the axes
cluster(
    my_data,
    title='Test Plot',
    plot_mean=2)
