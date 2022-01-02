import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from sim import Drone

class UI:
    def __init__(self, actors=list):
        self.figure = plt.figure()
        self.ax = self.figure.add_subplot(projection="3d")
        self.N = 1000

        self.actors = actors

        # For now, just plot a 3d spiral
        t = np.linspace(0, 2*np.pi, self.N)
        self.coords = np.empty((len(t), 3))
        for i in range(len(t)):
            self.coords[i, :] = np.array([np.sin(t[i]), np.cos(t[i]), 0.1*t[i]])

        self.i = 0
        self.coords = self.coords.T
        # Just do this after you initialise the plot
        # self.initialise_plot()

        self.line = self.ax.plot(0, 0, 0)[0]
        self.ax.set_xlim3d([-0.5, 0.5])
        self.ax.set_xlabel('X')

        self.ax.set_ylim3d([-0.5, 0.5])
        self.ax.set_ylabel('Y')

        self.ax.set_zlim3d([0.0, 3.0])
        self.ax.set_zlabel('Z')

        self.ax.set_title('3D Test')

        self.animation = animation.FuncAnimation(self.figure, self.animate, self.N, interval=1000/self.N, blit=False)

    def animate(self, num):
        self.line.set_data(self.coords[0:2, :num])
        self.line.set_3d_properties(self.coords[2, :num])

        return self.line

if __name__ == "__main__":
    ui = UI()

    plt.show()
