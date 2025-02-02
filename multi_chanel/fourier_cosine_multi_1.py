
# PIP
import os
import sys
import csv
import time
import math
import numpy                as np
import scipy.special        as sp
import matplotlib.pyplot    as plt
import plotly.graph_objects as go
import plotly.express       as px

from scipy.fftpack          import fft, fftfreq, fftshift
from plotly.subplots        import make_subplots

# LOCAL
import signal_data          as sd
import ht                   as ht
import fft_chart


def repos_vector(a):

    m = a.shape[0]
    n = a.shape[1]
    b = np.zeros([m * n])

    for i in range(n):
        b[(0 + i * m) : (m + i * m)] = a[: , i]

    return b


def get_modes(tres, ires, scale0, energy = None, modes = None):

    if ((energy == None) and (modes == None)) or ((energy != None) and (modes != None)):
        print('ERROR, definir correctamente get_modes...')
        sys.exit()

    vec_modes = [x for x in range(1, ires.shape[0] + 1)]
    vec_enrgy = np.zeros([ires.shape[0]])
    for i in range(ires.shape[0]):
        vec_enrgy[i] = np.sum(ires[i , :] ** 2)

    vec_enrgy0 = vec_enrgy[:]
    vec_enrgy1 = np.sort(vec_enrgy)[::-1]

    sum_e   = np.sum(vec_enrgy1)
    sum_et  = 0.0
    for imode, i in enumerate(vec_enrgy1,  start = 1):
        sum_et      = sum_et + i
        pc_sum_et   = (sum_et / sum_e) * 100.0
        if (energy != None) and (pc_sum_et > float(energy)): break
        if (modes != None) and (modes == imode): break

    iires = np.zeros([imode , tres.shape[0]])
    iindx = []
    for i in range(imode):
        indx = (np.where(vec_enrgy1[i] == vec_enrgy0))[0][0]
        iires[i , :] = ires[indx , :]
        iindx.append(indx)

    fig = px.line(x = vec_modes, y = (100 * vec_enrgy1 / sum_et), markers = True, width = 700, height = 400)

    fig.update_layout(
        font = dict(family = 'Times New Roman', color = 'black', size = 22),
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

    fig.update_traces(line = dict(width = 2.8, color = 'black'), marker = dict(color = "white", size = 8, line = dict(width = 2, color = 'black')))
    fig.write_image("modes.png")
    #fig.show()

    return iindx, iires


#########################################################################################
# SIGNAL 

fs  = sd.fs
seg = sd.seg
t   = sd.t
N   = sd.N
s1  = sd.s1 / np.max(sd.s1)
s2  = sd.s2 / np.max(sd.s2)
s3  = sd.s3 / np.max(sd.s3)

st = np.zeros([t.shape[0], 3])
st[: , 0] = s1
st[: , 1] = s2
st[: , 2] = s3

# REMAIN ONE CHANNEL
# st = st[: , 0]
###########################################################################################

colors = px.colors.qualitative.Alphabet

fig = go.Figure()

fig.add_trace(go.Scatter(x = t, y = s1, name = 's1', line = dict(color = colors[0])))
fig.add_trace(go.Scatter(x = t, y = s2, name = 's2', line = dict(color = colors[1])))
fig.add_trace(go.Scatter(x = t, y = s3, name = 's3', line = dict(color = colors[2])))

fig.update_layout(
    font = dict(family = 'Times New Roman', color = 'black', size = 40),
    xaxis_title = 'Time (s)',
    yaxis_title = 'Magnitude (pu)',
    plot_bgcolor = 'white',
    width = 700,
    height = 600,
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

fig.update_traces(line = dict(width = 7))
fig.write_image("signal.png")
fig.show()

fft_chart.multisignal_FFT(t_vec = t, y_vec = st, h_vec = ['s1', 's2', 's3'], x_axis = [0, 1], save_fig = 'fft1')
sys.exit()

#########################################################################################
# SEVERAL FREQUENCIES OF COSINE FUNCTIONS

fb_zeros = 15
bessel_func = 0
L = 560
modes = 15

scale0 = np.array([x for x in range(1, fb_zeros + 1)])

if N - L < 0:
    print('*** STOP ***', 'N - L: ' + str(N - L), sep = '\n')
    sys.exit()

z = np.linspace(0, 2 * np.pi, L)
fb = np.zeros([fb_zeros , z.shape[0]])

fig = go.Figure()
for n in range(fb_zeros):
    fb[n,:] = np.cos(z * scale0[n])
    fig.add_trace(go.Scatter(x = z, y = fb[n,:], line = dict(color=colors[n]), name = 's' + str(n + 1)))

fig.update_layout(
    font = dict(family = 'Times New Roman', color = 'black', size = 40),
    xaxis_title = 'Time (s)',
    yaxis_title = 'Magnitude (pu)',
    plot_bgcolor = 'white',
    width = 700,
    height = 600,
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
# fig.write_image("cosines.png")
# fig.show()

# sys.exit()

#########################################################################################
# BI-ORTHOGONALITY (GRAGAM MATRIX)
X = fb.T
ps = np.linalg.inv(X.T @ X) @ X.T

fig = go.Figure()
for n in range(fb_zeros):
    fig.add_trace(go.Scatter(x = z, y = ps[n,:], name = 's' + str(n + 1)))

fig.update_layout(
    title = 'biortho_basec',
    font = dict(family = 'Times New Roman', color = 'black', size = 22),
    xaxis_title = 'Time (s)',
    yaxis_title = 'Magnitude (pu)',
    plot_bgcolor = 'white',
    width = 700, height = 400
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
# fig.write_image("biortho_basec.png")
# fig.show()

# fft_chart.multisignal_FFT(t_vec = z, y_vec = ps.T, x_axis = [0, 3], save_fig = 'fourier_2c')

#########################################################################################
# GET MONO-COMPONENTS

ires = np.zeros([fb_zeros * st.shape[1] , N - L])
jres = np.zeros([N - L])
mres = np.zeros([N - L])
serr = np.zeros([N - L])
tres = np.linspace(0, (N - L) / fs, N - L)
rst  = st[:(N - L)]

i = 0
for n in range(N-L):
    ist = st[n : n + L , :]
    xcn = ps @ ist
    ires[: , n] = repos_vector(xcn)

print('ist', ist.shape)
print('ps', ps.shape)
print('xcn', xcn.shape)
print('ires', ires.shape)

iindx, iires = get_modes(tres, ires, scale0, energy = None, modes = modes)
modes = iires.shape[0]

fig = make_subplots(rows = 2, cols = 1,
                    shared_xaxes = True,
                    vertical_spacing = 0.14
                    )

for i in range(ires.shape[0]):
    fig.append_trace(go.Scatter(x = tres, y = ires[i , :], name = 's' + str(i + 1), legendgroup = '1'), row=1, col=1)
    
for i in range(modes):
    fig.append_trace(go.Scatter(x = tres, y = iires[i , :], name = 's' + str(iindx[i] + 1), legendgroup = '2'), row=2, col=1)

fig.update_layout(
    font = dict(family = 'Times New Roman', color = 'black', size = 40),
    plot_bgcolor = 'white',
    width = 700,
    height = 600,
    showlegend=False
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

fig.update_xaxes(title_text = 'Time (s)', row=2, col=1)
fig.update_yaxes(title_text = 'Mag. (pu)', row=1, col=1)
fig.update_yaxes(title_text = 'Mag. (pu)', row=2, col=1)

fig.update_traces(line = dict(width = 2.8))
fig.write_image("monocomponents_c.png")
fig.show()

# for i in range(N-L):
#     jres[i] = sum(ires[: , i])

for i in range(N-L):
    mres[i] = sum(iires[: , i])

# yerr0 = np.sqrt(abs(rst ** 2 - jres ** 2))
# serr0 = np.round(np.sum(yerr0 / fs),3)
# yerr1 = np.sqrt(abs(rst ** 2 - mres ** 2))
# serr1 = np.round(np.sum(yerr1 / fs),3)

# fig = make_subplots(rows = 2, cols = 1,
#                     shared_xaxes = True,
#                     vertical_spacing = 0.1
#                     )
# fig.add_trace(go.Scatter(x = tres, y = rst, legendgroup = 1, name = 'Signal', line = dict(color = 'black', width = 3)), row=1, col=1)
# fig.add_trace(go.Scatter(x = tres, y = jres, legendgroup = 1, name = str(fb_zeros) + ' modes', line = dict(color = 'red', width = 3, dash = 'dot')), row=1, col=1)

# fig.add_trace(go.Scatter(x = tres, y = rst, legendgroup = 2, name = 'Signal', line = dict(color = 'black', width = 3)), row=2, col=1)
# fig.add_trace(go.Scatter(x = tres, y = mres, legendgroup = 2, name = str(modes) + ' modes', line = dict(color = 'red', width = 3, dash = 'dot')), row=2, col=1)
    
# fig.update_layout(
#     font = dict(family = 'Times New Roman', color = 'black', size = 40),
#     legend_tracegroupgap = 60,
#     plot_bgcolor = 'white',
#     width = 700,
#     height = 600
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

# fig.update_xaxes(title_text = 'Time (s)', row=2, col=1)
# fig.update_yaxes(title_text = 'Mag. (pu)', row=1, col=1)
# fig.update_yaxes(title_text = 'Mag. (pu)', row=2, col=1)

# fig.update_traces(line = dict(width = 2.8))
# fig.write_image("aprox_c.png")
# fig.show()


for i in range(modes):
    freq_av, damp_av = ht.hilbert_transform(t = tres, st = iires[i,:], fs = fs, index = str(i + 1), print_chart = False, save_fig = 'hilbert_' + str(i))
    freq_av, damp_av = round(freq_av, 3), round(damp_av, 3)
    print(i, 'freq: ' + str(freq_av), ' / damp: ' + str(damp_av))

# y_vec = np.zeros([jres.shape[0], 2])
# y_vec[: , 0] = rst
# y_vec[: , 1] = mres
# fft_chart.dossignal_FFT(t_vec = tres, y_vec = y_vec, h_vec = ['Signal', 'Estimation'], x_axis = [0, 1], save_fig = 'fourier_3c')
