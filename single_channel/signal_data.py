
import csv
import numpy as np


####################################################################################

# row_data    = []
# csvrow_data = csv.reader(open('Datos_ringdown.csv'))
# for column in csvrow_data:
#     row_data.append(column)

# h_vec = row_data[0]
# t, y = [], []
# for index, irow_data in enumerate(row_data[1:]):
#     t.append(float(irow_data[0]))
#     y.append([])
#     for jrow_data in irow_data[1:]:
#         y[index].append(float(jrow_data))

# y_vec = np.array(y)
# t_vec = np.array(t)
# t_vec = t_vec - t_vec[0]

# for i in range(y_vec.shape[1]):
#     y_vec[: , i] = y_vec[: , i] - np.mean(y_vec[: , i])

# st  = y_vec[: , 0]
# t   = t_vec
# N   = len(st)
# fs  = int(N / t_vec[-1])
# seg = t_vec[-1]

####################################################################################

# fs  = 60
# seg = 50
# t   = np.linspace(2, seg, seg * fs)
# N   = len(t)
# st  = (
# 	    20 * np.exp(-0.01 * t) * np.sin(2 * np.pi * 0.2 * t) +
# 	    10 * np.exp(-0.10 * t) * np.sin(2 * np.pi * 0.6 * t) +
# 	    5 * np.exp(-0.015 * t) * np.sin(2 * np.pi * 0.8 * t)
# 	    )

####################################################################################

fs  = 60
seg = 50
t   = np.linspace(2, seg, seg * fs)
N   = len(t)
st  = (
	    20 * np.exp(-0.02 * t) * np.sin(2 * np.pi * 0.20 * t) +
	    15 * np.exp(-0.05 * t) * np.sin(2 * np.pi * 0.50 * t) +
	    10 * np.exp(-0.09 * t) * np.sin(2 * np.pi * 0.90 * t)
	    )

####################################################################################

# fs  = 60
# seg = 50
# t   = np.linspace(2, seg, seg * fs)
# N   = len(t)
# st  = (
# 	    1 * np.exp(-0.01 * t) * np.sin(2 * np.pi * 0.33 * t) +
# 	    1 * np.exp(-0.03 * t) * np.sin(2 * np.pi * 0.79 * t)
# 	    )

####################################################################################


# fs  = 60
# seg = 50
# t   = np.linspace(2, seg, seg * fs)
# N   = len(t)
# st  = 10 * np.exp(-0.01 * t) * np.sin(2 * np.pi * 0.33 * t)

####################################################################################
