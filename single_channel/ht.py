
import os
import sys
import numpy                as np
import matplotlib.pyplot    as plt
import plotly.graph_objects as go
import plotly.express       as px

from scipy.signal           import hilbert, chirp
from plotly.subplots        import make_subplots



def delimit_vector(vec, limits = [0.1, 0.9]):
    
    n       = vec.shape[0]
    vec_dv  = vec[int(n * limits[0]) : int(n * limits[1])]

    return vec_dv


def parse_inputs(x0, y0):

    x = x0.copy()
    y = y0.copy()

    h       = np.diff(x)
    dy      = y
    N       = 1
    perm    = np.array([2, 1])

    return h, dy, N, perm


def diffxy(x0, y0):

    x = x0.copy()
    y = y0.copy()

    h, dy, N, perm = parse_inputs(x, y)
        
    n = h.shape[0]
    i1 = np.array(range(0, n-1))
    i2 = np.array(range(1, n))

    v = np.diff(dy) / h

    if n > 1:
        dy[i2] = (h[i1] * v[i2] + h[i2] * v[i1]) / (h[i1] + h[i2])
        dy[0] = 2 * v[0] - dy[1]
        dy[n] = 2 * v[n-1] - dy[n-1]


    return dy


def hilbert_transform(t, st, fs, index, print_chart, save_fig = None):

    himf    = hilbert(st)
    amp     = np.abs(himf)
    
    xr      = himf.real
    yr      = himf.imag
    dx      = diffxy(t, xr)
    dy      = diffxy(t, yr)

    omega_h = (xr * dy - yr * dx) / (xr ** 2 + yr ** 2)    
    freq_h  = omega_h / (2.0 * np.pi)
    dA      = diffxy(t, amp.copy())
    domega  = diffxy(t, omega_h)
    damp_h  = -(dA) / amp - domega / (2.0 * np.pi)  

    t_dv    = delimit_vector(t)
    amp_dv  = delimit_vector(amp)
    freq_dv = delimit_vector(freq_h)
    freq_av = np.mean(freq_dv)
    damp_dv = delimit_vector(damp_h)
    damp_av = np.mean(damp_dv)

    print('t = ', list(t))
    print('t_dv = ', list(t_dv))
    print('st = ', list(st))
    print('amp_dv = ', list(amp_dv))
    print('freq_h = ', list(freq_h))
    print('freq_dv = ', list(freq_dv))
    print('damp_h = ', list(damp_h))
    print('damp_dv = ', list(damp_dv))

    if print_chart:

        fig = make_subplots(rows = 3, cols = 1,
                    shared_xaxes = True,
                    vertical_spacing = 0.03,
                    )

        fig.append_trace(go.Scatter(x = t, y = st, name = '$\large s_'+index+'(t) \& \hat{s}_'+index+'(t)$', legendgroup = '1', line = dict(color = 'black', width = 3)), row=1, col=1)
        fig.append_trace(go.Scatter(x = t_dv, y = amp_dv, name = '$\large\hat{a}_'+index+'(t)$', legendgroup = '1', line = dict(color = 'red', width = 3, dash = 'dot')), row=1, col=1)
            
        fig.append_trace(go.Scatter(x = t, y = freq_h, name = '$\large \hat{f}_'+index+'(t)$', legendgroup = '2', line = dict(color = 'black', width = 3)), row=2, col=1)
        fig.append_trace(go.Scatter(x = t_dv, y = freq_dv, name = '$\large \hat{f}_'+index+'=' + str(round(freq_av, 2)) + '(Hz)$', legendgroup = '2', line = dict(color = 'red', width = 3, dash = 'dot')), row=2, col=1)

        fig.append_trace(go.Scatter(x = t, y = damp_h, name = '$\large \hat{\zeta}_'+index+'(t)$', legendgroup = '3', line = dict(color = 'black', width = 3)), row=3, col=1)
        fig.append_trace(go.Scatter(x = t_dv, y = damp_dv, name = '$\large \hat{\zeta}_'+index+'='+str(round(damp_av, 2)) + '(s^{-1})$',  legendgroup = '3', line = dict(color = 'red', width = 3, dash = 'dot')), row=3, col=1)

        fig.update_layout(
            font = dict(family = 'Times New Roman', color = 'black', size = 28),
            legend_tracegroupgap = 50,
            plot_bgcolor = 'white',
            width = 500,
            height = 500,
            showlegend = True,
            yaxis_range=[-2, 2],
            legend=dict(x = 0.55, y = 0.99, bgcolor = 'rgba(0,0,0,0)')
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


        fig.update_yaxes(title_text = 'Mag.', row=1, col=1)
        fig.update_yaxes(title_text = 'Freq.', row=2, col=1)
        fig.update_yaxes(title_text = 'Damp.', row=3, col=1)
        fig.update_xaxes(title_text = 'Time (s)', row=3, col=1)

        fig.update_traces(line = dict(width = 2.8))
        fig.show()

        if save_fig != None:
            fig.write_image(save_fig + '.png')

    return freq_av, damp_av



def main():

    time    = 50.0
    fs 	    = 30
    t       = np.linspace(0, time, int(fs * time))
    st 	    = np.exp(-0.03 * t) * np.cos(2.0 * np.pi * 0.33 * t)
    st      = st / np.max(st)

    hilbert_transform(t, st, fs, '1', True)



if __name__ == '__main__':
    main()