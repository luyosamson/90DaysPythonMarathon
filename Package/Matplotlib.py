import matplotlib.pyplot as plt
import numpy as np

# create data
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)

# create plot
plt.plot(x, y)
plt.title("Sin Wave")
plt.xlabel("X")
plt.ylabel("Y")

# display plot
plt.show()
