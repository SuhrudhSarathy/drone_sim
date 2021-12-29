import numpy as np
from numpy import sin as s, cos as c, tan as t
import matplotlib.pyplot as plt
from numpy.core.numerictypes import sctype2char


class Drone:
    def __init__(self):
        # Position
        self.x, self.y, self.z = 0, 0, 0

        # Roll Pitch Yaw
        self.phi, self.theta, self.psi = 0, 0, 0

        # Linear velocities
        self.vx, self.vy, self.vz = 0, 0, 0

        # Angular Velocities
        self.p, self.q, self.r = 0, 0, 0

        self.linear_position_vector = lambda: np.array([self.x, self.y, self.z]).reshape(3, 1)
        self.angular_position_vector = lambda: np.array([self.phi, self.theta, self.psi]).reshape(3, 1)
        self.linear_velocity = lambda: np.array([self.vx, self.vy, self.vz]).reshape(3, 1)
        self.angular_velocity = lambda: np.array([self.p, self.q, self.r]).reshape(3, 1)

        # Constants
        self.k = 0.1
        self.b = 0.2
        self.l = 0.5

        # Omegas
        self.w1 = 0
        self.w2 = 0
        self.w3 = 0
        self.w4 = 0

        # Thrust Vector
        self.thrust = np.array(
            [
                [0],
                [0],
                [self.k*(self.w1**2 + self.w2**2 + self.w3**2 + self.w4**2)]
            ])

        # Torque Vector
        self.torque = np.array(
            [
                [self.l*self.k*(-self.w2**2 + self.w4**2)],
                [self.l*self.k*(-self.w1**2 + self.w3**2)],
                [self.b*(self.w1**2 + self.w2**2 + self.w3**2 + self.w4**2)]
            ]
        )

        # Transformation Matrices
        self.R = np.array(
            [c(self.phi)*c(self.theta), c(self.phi)*s(self.theta)*s(self.phi)-s(self.psi)*c(self.phi), c(self.phi)*s(self.theta)*s(self.phi)+s(self.psi)*c(self.phi)],
            [s(self.psi)*c(self.theta), s(self.psi)*s(self.theta)*s(self.phi)+c(self.psi)*c(self.phi), s(self.psi)*s(self.theta)*s(self.phi)+c(self.psi)*c(self.phi)],
            [-s(self.theta), c(self.theta)*s(self.psi), c(self.theta)*c(self.phi)]
        )

        self.W =np.array(
            [
                [1, 0, -s(self.theta)],
                [0, c(self.phi), c(self.theta)*s(self.phi)],
                [0, -s(self.phi), c(self.theta)*c(self.phi)]
            ]
        )

    # All State Update functions
    def __update_thrust_and_torque(self, w1, w2, w3, w4):
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.w4 = w4

        self.thrust = np.array(
            [
                [0],
                [0],
                [self.k*(self.w1**2 + self.w2**2 + self.w3**2 + self.w4**2)]
            ])

        # Torque Vector
        self.torque = np.array(
            [
                [self.l*self.k*(-self.w2**2 + self.w4**2)],
                [self.l*self.k*(-self.w1**2 + self.w3**2)],
                [self.b*(self.w1**2 + self.w2**2 + self.w3**2 + self.w4**2)]
            ]
        )




        
