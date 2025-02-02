import os
import sys
import numpy                as np
import plotly.graph_objects as go
import plotly.express       as px


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
yb = [6.10363170e+01, 2.77995524e+01, 1.11641305e+01, 7.73235572e-01, 1.39773212e-01, 5.23317617e-02, 2.66263811e-02, 2.49793302e-02, 1.61737069e-02, 1.11227261e-02, 9.41496875e-03, 8.46210998e-03, 7.07682670e-03, 6.97900676e-03, 6.56301528e-03]
yc = [8.19189612e+01, 1.57271059e+01, 2.35393291e+00, 1.73568603e-01, 	 1.37857966e-01, 9.82542931e-02, 8.82682325e-02, 5.77304832e-02, 	 4.69562351e-02, 3.12936694e-02, 1.17248466e-02, 5.12757160e-03, 	 2.81047312e-03, 1.74014705e-03, 1.16348801e-03]


fig = go.Figure()

fig.add_trace(go.Scatter(x = x, y = yb, name = 'Bessel',  line = dict(color = 'black', width = 3)))
fig.add_trace(go.Scatter(x = x, y = yc, name = 'Cosine',  line = dict(color = 'black', width = 3, dash = 'dot')))

fig.update_layout(
    font = dict(family = 'Times New Roman', color = 'black', size = 25),
    width = 800,
	height = 400,
    xaxis_title = 'Mode',
    yaxis_title = 'Energy (%)',
    plot_bgcolor = 'white'
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
fig.update_layout(legend=dict(yanchor="top", y=0.95, xanchor="left", x=0.75))
fig.update_traces(line = dict(width = 7, color = 'black'), marker = dict(color = "white", size = 8, line = dict(width = 2, color = 'black')))
fig.write_image("modes.png")
fig.show()