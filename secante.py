import numpy as np

def secante(x0,x1,nmax,tol):
	f = lambda r, h, a : (np.pi/3)*(2*r-h)**2*(3*r-(2*r-h))\
					+ 10*(r**2*np.arccos((r-(2*r-h))/r)- \
						(r-(2*r-h))*np.sqrt(2*r*(2*r-h)-(2*r-h)**2)) -\
						(a/100)*(159.1740)

	l =[x0,x1]
	i=2
	while not(i > nmax):
		if (np.abs(x1-x0) < tol):
			print(f"rraiz r = {x1}")
			break
		else :
			x2 = x1 - f(2,x1,25)*(x1-x0)*(f(2,x1,25)-f(2,x0,25))**(-1)
			l.append(x2)
			x0=x1
			x1 = x2
		i+=1
	return x2,i
print(secante(0,4,30,10**(-4)))
