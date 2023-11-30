import matplotlib.pyplot as plt
import numpy as np

petal_count_k = int(input("Petal count : ")) / 2
radius = float(input("Radius : "))
phi = np.arange(0, 2 * np.pi, 0.01)
r = radius + abs(np.sin(petal_count_k * phi))

x = r * np.cos(phi)
y = r * np.sin(phi)
plt.plot(x, y, color="purple")

x_circ = radius * np.cos(phi)
y_circ = radius * np.sin(phi)
plt.plot(x_circ, y_circ, color="red")

plt.show()