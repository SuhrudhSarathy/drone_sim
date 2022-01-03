"""This file logs all the sensor data and outputs into a log file if needed or plot seperately"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(projection="3d")


T = np.arange(0, 20, 0.01)
X = []
Y = []
Z = []
for t in T:
    plt.cla()
    ax.set_xlim3d([-5.0, 5.0])
    ax.set_ylim3d([-5.0, 5.0])
    ax.set_zlim3d([-5.0, 5.0])

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_title("Quadcopter Simulation")
    X.append(t)
    Y.append(np.sin(t))
    Z.append(np.cos(t))
    ax.plot(X, Y, Z)
    plt.pause(0.00001)