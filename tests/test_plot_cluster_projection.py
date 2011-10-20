import scipy as sp
from spikeplot import cluster_projection

# get some data
my_data = {
    0:sp.randn(900, 2),
    1:sp.randn(700, 2) + 5,
    2:sp.randn(500, 2) - 5,
    3:sp.randn(300, 2) - 10,
    4:sp.randn(100, 2) + 10}

# call the plot function on the axes
cluster_projection(my_data)
