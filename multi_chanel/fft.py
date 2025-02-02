import os
import sys
import csv
import math
import matplotlib

import numpy 				as np
import plotly.express       as px
import plotly.graph_objects as go
import matplotlib.pyplot 	as plt

from scipy.fftpack 			import fft, fftfreq, fftshift


def dossignal_FFT(t_vec, y_vec, h_vec = [], x_axis = [0, 1], save_fig = None):

	if len(h_vec) == 0:
		for i in range(y_vec.shape[1]):
			h_vec.append('s' + str(1 + i))

	can 	= y_vec.shape[1]
	medf 	= len(y_vec[:,0])
	dt 		= t_vec[1] - t_vec[0]
	y_z 	= np.zeros([2**14 , 1]) 

	S0 = np.zeros([len(y_z) + medf , can])
	Es = np.zeros([len(y_z) + medf , can], dtype = complex)

	for i in range(can):
		S0[: , i] = np.concatenate((y_vec[: , i], y_z), axis = None)
		Es[: , i] = fftshift(fft(S0[: , i]))

	fx = np.linspace(-1.0 / (2.0 * dt), 1.0 / (2.0 * dt), len(S0[: , 0]))

	fig = go.Figure()
	# for i in range(can):
	# 	fig.add_trace(go.Scatter(x = fx, y = abs(Es[: , i]), name = h_vec[i]))

	fig.add_trace(go.Scatter(x = fx, y = abs(Es[: , 0])/(max(abs(Es[: , 0]))), name = 'Signal', line = dict(color = 'red', width = 3)))
	fig.add_trace(go.Scatter(x = fx, y = abs(Es[: , 1])/(max(abs(Es[: , 1]))), name = 'Estimation', line = dict(color = 'black', width = 3, dash = 'dot')))

	fig.update_layout(
		width = 700,
		height = 400,
	    font = dict(family = 'Times New Roman', color = 'black', size = 25),
	    xaxis_title = 'Frequency (Hz.)',
	    yaxis_title = 'Magnitude (pu)',
	    xaxis_range = [x_axis[0], x_axis[1]],
	    plot_bgcolor = 'white',
	    legend=dict(x = 0.7, y = 0.99)
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
	fig.show()
	
	if save_fig != None:
		fig.write_image(save_fig + '.png')



def multisignal_FFT(t_vec, y_vec, h_vec = [], x_axis = [0, 1], save_fig = None):

	colors = px.colors.qualitative.Alphabet

	if len(h_vec) == 0:
		for i in range(y_vec.shape[1]):
			h_vec.append('s' + str(1 + i))

	can 	= y_vec.shape[1]
	medf 	= len(y_vec[:,0])
	dt 		= t_vec[1] - t_vec[0]
	y_z 	= np.zeros([2**14 , 1]) 

	S0 = np.zeros([len(y_z) + medf , can])
	Es = np.zeros([len(y_z) + medf , can], dtype = complex)

	for i in range(can):
		S0[: , i] = np.concatenate((y_vec[: , i], y_z), axis = None)
		Es[: , i] = fftshift(fft(S0[: , i]))

	fx = np.linspace(-1.0 / (2.0 * dt), 1.0 / (2.0 * dt), len(S0[: , 0]))

	fig = go.Figure()
	for i in range(can):
		# fig.add_trace(go.Scatter(x = fx, y = abs(Es[: , i])/(np.max(abs(Es))), line = dict(color=colors[i]), name = h_vec[i]))
		fig.add_trace(go.Scatter(x = fx, y = abs(Es[: , i])/(np.max(abs(Es))), line = dict(color='black'), name = h_vec[i]))

	fig.update_layout(
		width = 700,
		height = 600,
	    font = dict(family = 'Times New Roman', color = 'black', size = 40),
	    xaxis_title = 'Frequency (Hz.)',
	    yaxis_title = 'Magnitude (pu)',
	    xaxis_range = [x_axis[0], x_axis[1]],
	    plot_bgcolor = 'white',
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
	fig.show()
	
	if save_fig != None:
		fig.write_image(save_fig + '.png')
	



def singlesignal_FFT(t_vec, y_vec, x_axis, save_fig = None):

	medf 	= len(y_vec)
	dt 		= t_vec[1] - t_vec[0]
	y_z 	= np.zeros([2**14 , 1]) 

	S0 = np.zeros([len(y_z) + medf])
	Es = np.zeros([len(y_z) + medf], dtype = complex)

	S0 = np.concatenate((y_vec, y_z), axis = None)
	Es = fftshift(fft(S0))
	max_es = np.max(abs(Es))
	fx = np.linspace(-1.0 / (2.0 * dt), 1.0 / (2.0 * dt), len(S0))


	fig = px.line(x = fx, y = abs(Es) / max_es, width = 700, height = 600)
	fig.update_layout(
	    font = dict(family = 'Times New Roman', color = 'black', size = 40),
	    xaxis_title = 'Frequency (Hz.)',
	    yaxis_title = 'Magnitude (pu)',
	    xaxis_range = [x_axis[0], x_axis[1]],
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
	fig.show()

	if save_fig != None:
		fig.write_image(save_fig + '.png')



def main():

	# fs  = 60
	# seg = 50
	# t   = np.linspace(2, seg, seg * fs)
	# N   = len(t)
	# st  = (
	#     20 * np.exp(-0.01 * t) * np.sin(2 * np.pi * 0.2 * t) +
	#     10 * np.exp(-0.10 * t) * np.sin(2 * np.pi * 0.6 * t) +
	#     5 * np.exp(-0.015 * t) * np.sin(2 * np.pi * 0.8 * t)
	#     )

	# singlesignal_FFT(t_vec = t, y_vec = st, x_axis = [0, 1])
	
	row_data 	= []
	csvrow_data = csv.reader(open('Datos_ringdown.csv'))
	for column in csvrow_data:
		row_data.append(column)

	h_vec = row_data[0]
	t, y = [], []
	for index, irow_data in enumerate(row_data[1:]):
		t.append(float(irow_data[0]))
		y.append([])

		for jrow_data in irow_data[1:]:
			y[index].append(float(jrow_data))

	y_vec = np.array(y)
	t_vec = np.array(t)
	t_vec = t_vec - t_vec[0]

	# y_vec = y_vec[: , 0:2]

	for i in range(y_vec.shape[1]):
		y_vec[: , i] = y_vec[: , i] - np.mean(y_vec[: , i])

	dossignal_FFT(t_vec = t_vec, y_vec = y_vec, x_axis = [0, 2])



if __name__ == '__main__':
	main()


