import os
import sys
import csv
import time
import math
import numpy                as np
import scipy.special        as sp
import matplotlib.pyplot    as plt
import plotly.graph_objects as go
import signal_data          as sd
import plotly.express       as px

def get_modes(tres, ires, scale0, energy_threshold):

    vec_modes = [x for x in range(1, ires.shape[0] + 1)]
    vec_enrgy = np.zeros([ires.shape[0]])
    for i in range(ires.shape[0]):
        vec_enrgy[i] = np.sum(ires[i , :] ** 2)

    vec_enrgy0 = vec_enrgy[:]
    vec_enrgy1 = np.sort(vec_enrgy)[::-1]

    return vec_enrgy1


#######################################
# SIGNAL 
fs  = sd.fs
seg = sd.seg
t   = sd.t
N   = sd.N
st  = sd.s1 / np.max(sd.s1)
#######################################
m   = 3
#######################################


fb_zeros = 15
bessel_func = 0
scale0 = np.array([x for x in range(1, fb_zeros + 1)])

res_enrgy0 = []
xvec = [x for x in range(300, 700, 5)]
for L in xvec:
    print(L)

    z = np.linspace(-np.pi, np.pi, L)
    fb = np.zeros([fb_zeros , z.shape[0]])

    for n in range(fb_zeros):
        fb[n,:] = np.cos(z * scale0[n])

    X = fb.T
    ps = np.linalg.inv(X.T @ X) @ X.T

    ires = np.zeros([fb_zeros , N - L])
    tres = np.linspace(0, (N - L) / fs, N - L)

    for n in range(N-L):
        ist = st[n : n + L]
        xcn = ps @ ist
        ires[: , n] = xcn.T

    res_enrgy0.append([list(get_modes(tres, ires, scale0, 99)), L])

# x = [1,2,3,4,5,6,7,8,9,10]
# fig = go.Figure()
# for i in res_enrgy0:
#     fig.add_trace(go.Scatter(x = x, y = i[0], mode='lines+markers', name=i[1]))
# fig.show()
# print('max', np.max(i[0]))

res_enrgy1 = []
for i in res_enrgy0:
    res_enrgy1.append((np.sum(i[0][:m]) / np.sum(i[0][:])) * 100)

print(xvec)
print(res_enrgy1)


fig = px.line(x = xvec, y = res_enrgy1, width = 700, height = 400)

fig.update_layout(
    font = dict(family = 'Times New Roman', color = 'black', size = 22),
    xaxis_title = 'Sampling (L)',
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

fig.update_traces(line = dict(width = 2.8, color = 'black'))
fig.write_image("calc_L.png")
fig.show()

print("index:", xvec[list(res_enrgy1).index(max(res_enrgy1))],"value:", max(res_enrgy1))