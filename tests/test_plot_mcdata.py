import scipy as sp
from spikeplot import mcdata

ns, nc = 300 + 1000, 4
tf = 65
cut = (-int(sp.floor(tf / 2.0)), int(sp.ceil(tf / 2.0)))
mydata = sp.randn(ns, nc)
wf = sp.array([sp.sin(sp.linspace(0, 2 * sp.pi, tf)) * (i + 1)
               for i in xrange(nc)]).T
unit_ev = sp.array([50, 300, 750])
for i in unit_ev:
    mydata[i + cut[0]:i + cut[1], :] += wf
myother = sp.randn(ns, 4)
ep = sp.array([[150, 200], [800, 950]])
ev = {0:(wf, unit_ev), 1:unit_ev}

mcdata(
    mydata,
    other=myother,
    colours=None,
    epochs=ep,
    events=ev,
    x_offset=-100)
