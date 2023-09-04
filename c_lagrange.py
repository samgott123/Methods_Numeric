import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

z = np.linspace(0.9,13.3,10)
x = np.array([0.9,1.3,1.9,2.1,2.6,3.0,3.9,4.4,4.7,5.0,6.0,7.0,8.0,9.2,10.5,11.3,11.6,12.0,12.6,13.0,13.3])
y = np.array([1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,2.1,2.25,2.3,2.25,1.95,1.4,0.9,0.7,0.6,0.5,0.4,0.25])

result = []

def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    
    return result

for i in z :
    interp_result = lagrange_interpolation(x, y, i)
    result.append(interp_result)

df = pd.DataFrame({'x':z,'P(x)':result})
print(df.to_latex())

plt.subplot(2,1,1)
plt.plot(x,y,label="real")
plt.legend()
plt.subplot(2,1,2)
plt.plot(z,result,label='interpolated')
plt.legend()
plt.show()
