import scipy as sp
from spikeplot import spike_trains

# inits
mytrains = {0:sp.array([1, 3, 40, 50, 56]) * 100,
            1:sp.array([5, 33, 38, 43, 66, 68]) * 100}
alignment = {(0, 1):[(1, 1), (2, 3), (4, 2)]}

# plot
spike_trains(
    mytrains,
    alignment=alignment,
    samples_per_second=24000)
