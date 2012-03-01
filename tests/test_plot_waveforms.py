import scipy as sp
from spikeplot import waveforms

# get some data
my_data = {0:sp.randn(20, 50, 4), 1:sp.randn(10, 200) + 2}

# call the plot function on the axes
waveforms(
    my_data,
    tf=50,
    title='Test Plot',
    plot_mean=True,
    plot_single_waveforms=True,
    plot_separate=True)
