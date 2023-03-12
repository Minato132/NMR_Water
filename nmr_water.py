import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as py


def T1(t, a, b, c, d):
	y = np.exp(-1/b * t + c) + d
	return y

def param(ar1, ar2, func):
	a, b = py.curve_fit(func, ar1, ar2, method = 'trf')
	return a, b


with open('/home/minato132/Documents/Data/Water/WaterT2.csv') as file:
	data = pd.read_csv(file)

data['CH1'] = pd.to_numeric(data.loc[1:,'CH1'])

time = []
i = 0
x = data.iat[0,2]

while i < len(data['X']) - 1:
	time.append(x)
	x += data.iat[0,3]
	i += 1

time = pd.Series(time, index = np.arange(1, 1201))

d = {'time': time, 'amp' : data['CH1']}

data1 = pd.DataFrame(d)
data1.drop(0, axis = 0, inplace = True)

def t2(ar1, ar2, ar3, ar4, func):
	a, b = param(ar1, ar2, func)
	plt.scatter(ar3, ar4, label = 'Data')
	plt.plot(ar1, T1(ar1, *a), label = 'Fitted Curve', color = 'red')
	plt.xlabel('Delay Time (ms)')
	plt.ylabel('Max Amplitude')
	plt.title('T1 of Water')

	plt.legend()
	print(*a)






