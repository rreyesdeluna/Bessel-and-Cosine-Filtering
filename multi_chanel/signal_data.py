
import csv
import numpy as np
import matplotlib.pyplot as plt 

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

fs  = 60
seg = 50
t   = np.linspace(0, seg, seg * fs)
N   = len(t)

f1 = [0.260, 0.630, 0.940]
f2 = [0.259, 0.631, 0.939]
f3 = [0.261, 0.629, 0.943]

d1 = [0.062, 0.021, 0.043]
d2 = [0.061, 0.021, 0.041]
d3 = [0.060, 0.021, 0.045]

a1 = [17.9, 19.0, 20.0]
a2 = [18.1, 19.1, 20.1]
a3 = [18.2, 19.1, 20.0]

s1  = (
	    a1[0] * np.exp(-d1[0] * t) * np.sin(2 * np.pi * f1[0] * t) +
	    a1[1] * np.exp(-d1[1] * t) * np.sin(2 * np.pi * f1[1] * t) +
	    a1[2] * np.exp(-d1[2] * t) * np.sin(2 * np.pi * f1[2] * t)
	    )

s2  = (
	    a2[0] * np.exp(-d2[0] * t) * np.sin(2 * np.pi * f2[0] * t) +
	    a2[1] * np.exp(-d2[1] * t) * np.sin(2 * np.pi * f2[1] * t) +
	    a2[2] * np.exp(-d2[2] * t) * np.sin(2 * np.pi * f2[2] * t)
	    )

s3  = (
	    a3[0] * np.exp(-d3[0] * t) * np.sin(2 * np.pi * f3[0] * t) +
	    a3[1] * np.exp(-d3[1] * t) * np.sin(2 * np.pi * f3[1] * t) +
	    a3[2] * np.exp(-d3[2] * t) * np.sin(2 * np.pi * f3[2] * t)
	    )

# plt.plot(t, s1)
# plt.plot(t, s2)
# plt.plot(t, s3)
# plt.show()