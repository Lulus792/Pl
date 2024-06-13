import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data

# set up a figure twice as wide as it is tall
fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={'projection': '3d'})

# =============
# First subplot
# =============
# set up the Axes for the first plot

def Voltage(theta, r):
    return np.sin(theta)**2 / r**2

# plot a 3D surface like in the example mplot3d/surface3d_demo
theta = np.arange(0, 2*np.pi, 0.01) 
X = np.linspace(-30, 30, num=200)
Y = np.linspace(-30, 30, num=200)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.array([np.sin(angel)**2 / radius**2 for angel, radius in zip(theta, R)])
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
#ax.set_zlim(min(Z), max(Z))
fig.colorbar(surf, shrink=0.5, aspect=10)

# ==============
# Second subplot
# ==============
# set up the Axes for the second plot
#ax = fig.add_subplot(1, 2, 2, projection='3d')

# plot a 3D wireframe like in the example mplot3d/wire3d_demo
#X, Y, Z = get_test_data(0.05)
#ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()
