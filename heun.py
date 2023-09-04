import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def euler(x0,y0,n,xf):
	h = (xf-x0)/n
	f = lambda x , y: -50*(y-np.cos(x))
	x = np.linspace(x0,xf,n+1)
	y = np.zeros(n+1)
	y[0] = y0
	for i in range(1,n+1):
		k1 = f(x[i-1],y[i-1])
		k2 = f(x[i],y[i-1]+h*k1)
		y[i] = round(y[i-1] + 0.5*h*(k1+k2),2)

	F = lambda x : (50/2501)*(np.sin(x)+50 *np.cos(x)) - (2500/(2501*np.exp(50*x)))
	R = F(x)
	Error = np.abs(R-y)
	D = np.linspace(x0,xf,100)
	df = pd.DataFrame({'x':x,'y':y,'error':Error})
	print(df.to_latex())

	plt.subplot(1,2,1)
	plt.plot(D,F(D),label='real')
	plt.plot(x,y,label='approx')
	plt.title('Metodo de Heun')
	plt.legend()

	plt.subplot(1,2,2)
	plt.plot(x,Error,label='error')
	plt.title('Error absoluto')
	plt.legend()
	plt.show()

euler(0,0,90,np.pi)