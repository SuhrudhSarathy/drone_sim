"""This file contains drawing of the body"""
from sim.parameters import *
from sim.drone import Drone
import numpy as np

class Body:
    def __init__(self, viz_ax=None):
        self.drone = None
        self.viz_ax = viz_ax
        # Store all the endpoints in an array
        # We have the drone as with 5 important coordinates
        # Left front rotor, Right front Rotor
        #               Main Body
        # Left Rear rotor, Right read Rotor
        self.d = L/np.sqrt(2)
        self.coords = np.array(
            [
                [0, self.d, -self.d, -self.d, self.d],
                [0, self.d, self.d, -self.d, -self.d],
                [0, 0, 0, 0, 0]
            ]
        )
    
    def attach_to(self, drone):
        self.drone = drone
        self.drone.attach_body(self)

    def plot_body(self):
        assert self.drone is not None, "Add the body to a Drone"
        assert self.viz_ax is not None, "Don't know where to plot. Pass the axes when constructing the Object"

        # First transform all the points to the global frame
        coords = self.drone.R @ self.coords + self.drone.linear_position()

        origin = coords[:, 0]
        rf = coords[:, 1]
        lf = coords[:, 2]
        lr = coords[:, 3]
        rr = coords[:, 4]

        self.viz_ax.plot([origin[0], rf[0]], [origin[1], rf[1]], [origin[2], rf[2]], color="red")
        self.viz_ax.plot([origin[0], lf[0]], [origin[1], lf[1]], [origin[2], lf[2]], color="blue")
        self.viz_ax.plot([origin[0], lr[0]], [origin[1], lr[1]], [origin[2], lr[2]], color="black")
        self.viz_ax.plot([origin[0], rr[0]], [origin[1], rr[1]], [origin[2], rr[2]], color="green")

        self.viz_ax.scatter([origin[0]], [origin[1]], origin[2], color="yellow", s=2)

