import numpy as np
import matplotlib.pyplot as plt

# Datos de ejemplo (puedes reemplazar estos valores con tus propios datos)
x = np.array([0.9,1.3,1.9,2.1,2.6,3.0,3.9,4.4,4.7,5.0,6.0,7.0,8.0,9.2,10.5,11.3,11.6,12.0,12.6,13.0,13.3])
y = np.array([1.3,1.5,1.85,2.1,2.6,2.7,2.4,2.15,2.05,2.1,2.25,2.3,2.25,1.95,1.4,0.9,0.7,0.6,0.5,0.4,0.25])
# Calcula los coeficientes de los splines naturales cúbicos
n = len(x)
h = np.diff(x)
alpha = np.zeros(n)
for i in range(1, n - 1):
    alpha[i] = 3 / h[i] * (y[i + 1] - y[i]) - 3 / h[i - 1] * (y[i] - y[i - 1])

l = np.zeros(n)
mu = np.zeros(n)
z = np.zeros(n)
l[0] = 1
mu[0] = 0
z[0] = 0

for i in range(1, n - 1):
    l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]
    mu[i] = h[i] / l[i]
    z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

l[n - 1] = 1
z[n - 1] = 0
c = np.zeros(n)
b = np.zeros(n)
d = np.zeros(n)
c[n - 1] = 0
for j in range(n - 2, -1, -1):
    c[j] = z[j] - mu[j] * c[j + 1]
    b[j] = (y[j + 1] - y[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
    d[j] = (c[j + 1] - c[j]) / (3 * h[j])

# Genera puntos para la curva suave
x_smooth = np.linspace(min(x), max(x), 100)
y_smooth = np.zeros_like(x_smooth)

for i in range(n - 1):
    mask = (x_smooth >= x[i]) & (x_smooth <= x[i + 1])
    y_smooth[mask] = (
        y[i]
        + b[i] * (x_smooth[mask] - x[i])
        + c[i] * (x_smooth[mask] - x[i]) ** 2
        + d[i] * (x_smooth[mask] - x[i]) ** 3
    )

# Grafica los puntos de datos y la curva suave resultante
plt.figure(figsize=(8, 6))
plt.scatter(x, y, label='Datos', color='red', marker='o')
plt.plot(x_smooth, y_smooth, label='Spline Natural Cúbico', color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.title('Spline Natural Cúbico')
plt.show()
