import os
import sys

import numpy                as np
import scipy.special        as sp
import plotly.graph_objects as go
import signal_data          as sd
import plotly.express       as px

def get_modes(ires):

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
st  = sd.st / np.max(sd.st)
#######################################
m   = 3
fb_zeros = 10
bessel_func = 0
#######################################

scale0 = np.array([x for x in range(1, fb_zeros + 1)])

res_enrgy0 = []
xvec = [x for x in range(300, 905, 5)]
for L in xvec:

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

    res_enrgy0.append([list(get_modes(ires)), L])

res_enrgy1 = []
for i in res_enrgy0:
    res_enrgy1.append((np.sum(i[0][:m]) / np.sum(i[0][:])) * 100)

res_enrgy2 = []
for i in res_enrgy0:
    res_enrgy2.append((i[0] / np.sum(i[0])) * 100)


# colors = px.colors.qualitative.Alphabet

# x = [x for x in range(1, fb_zeros + 1)]
# fig = go.Figure()
# for i in range(len(res_enrgy2)):
#     fig.add_trace(go.Scatter(x = x, y = res_enrgy2[i], line = dict(color=colors[i]), mode = 'lines+markers', name = 'L' + str(res_enrgy0[i][1])))

# fig.update_layout(
#     legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.70),
#     width = 700,
#     height = 650,
#     font = dict(family = 'Times New Roman', color = 'black', size = 40),
#     xaxis_title = 'Mono-components (k)',
#     yaxis_title = 'Energy (%)',
#     plot_bgcolor = 'white'
# )
# fig.update_xaxes(
#     mirror = True,
#     ticks = 'outside',
#     showline = True,
#     linecolor = 'black',
#     gridcolor = 'lightgrey',
#     griddash = 'dot'
# )
# fig.update_yaxes(
#     mirror = True,
#     ticks = 'outside',
#     showline = True,
#     linecolor = 'black',
#     gridcolor = 'lightgrey',
#     griddash = 'dot'
# )
# fig.update_traces(line = dict(width = 7), marker=dict(size=12))
# fig.write_image("L_mono.png")
# fig.show()


fig = px.line(x = xvec, y = res_enrgy1)
fig.update_layout(
    width = 700,
    height = 600,
    font = dict(family = 'Times New Roman', color = 'black', size = 40),
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
fig.update_traces(line = dict(width = 7, color = 'black'))
fig.write_image("L_res.png")
fig.show()

print("index:", xvec[list(res_enrgy1).index(max(res_enrgy1))],"value:", max(res_enrgy1))