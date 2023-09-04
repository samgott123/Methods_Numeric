import numpy as np
def pontfix(x0,nmax,tol):
    g = lambda x : -(1/36)*x**3-(1/6)*x**2+x+(2/9)
    x1 = g(x0)
    i=1
    while not(i > nmax):
        if (np.abs(x1-x0) < tol):
            print(f"rraiz r = {x1}")
            break
        else :
            x0 = x1
            x1 = g(x0)
        i+=1
    return print(x1)

pontfix(3,20,10**(-4))