
# PIP
import os
import sys
import numpy                as np
import scipy.special        as sp
import plotly.graph_objects as go
import plotly.express       as px
from plotly.subplots        import make_subplots

# LOCAL
import fft_chart



fb_zeros = 6
bessel_func = 0
scale0 = np.array([x for x in range(1, fb_zeros + 1)])

t = np.linspace(0, 5 * np.pi, 1000)
fb = np.zeros([fb_zeros , t.shape[0]])

colors = px.colors.qualitative.G10


fig = go.Figure()
for n in range(fb_zeros):
    fb[n,:] = sp.jv(n, t)
    fig.add_trace(go.Scatter(x = t, y = fb[n,:], line = dict(color=colors[n])))

fig.update_layout(
    font = dict(family = 'Times New Roman', color = 'black', size = 40),
    xaxis_title = 'Time (s)',
    yaxis_title = 'Magnitude (pu)',
    plot_bgcolor = 'white',
    width = 700, height = 600,
    showlegend = False
)
fig.update_xaxes(
    mirror = True,
    ticks = 'outside',
    showline = True,
    linecolor = 'black',
    gridcolor = 'lightgrey',
    griddash = 'dot'
)
fig.update_yaxes(
    mirror = True,
    ticks = 'outside',
    showline = True,
    linecolor = 'black',
    gridcolor = 'lightgrey',
    griddash = 'dot'
)

fig.update_traces(line = dict(width = 2.8))
# fig.write_image("bessel_spetra.png")
fig.show()
fft_chart.multisignal_FFT(t_vec = t, y_vec = fb.T, x_axis = [0, 1])

