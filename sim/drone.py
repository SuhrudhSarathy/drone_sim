import numpy as np
from numpy import sin as s, cos as c, tan as t
from sim.parameters import *
from sim.sensors import Sensor


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

        self.linear_position = lambda: np.array([self.x, self.y, self.z]).reshape(3, 1)
        self.angular_position = lambda: np.array([self.phi, self.theta, self.psi]).reshape(3, 1)
        self.linear_velocity = lambda: np.array([self.vx, self.vy, self.vz]).reshape(3, 1)
        self.angular_velocity = lambda: np.array([self.p, self.q, self.r]).reshape(3, 1)

        # Omegas
        self.w1 = 0
        self.w2 = 0
        self.w3 = 0
        self.w4 = 0

        # Inertia Matrix
        self.inertia = np.diag([IXX, IYY, IZZ])
        
        # Drag Matrix
        self.drag = np.diag([AX, AY, AZ])

        # Thrust Vector
        self.thrust = np.array(
            [
                [0],
                [0],
                [K*(self.w1**2 + self.w2**2 + self.w3**2 + self.w4**2)]
            ])

        # Torque Vector
        self.torque = np.array(
            [
                [L*K*(-self.w2**2 + self.w4**2)],
                [L*K*(-self.w1**2 + self.w3**2)],
                [B*(self.w1**2 + self.w2**2 + self.w3**2 + self.w4**2)]
            ]
        )
        # Drag Force Vector
        self.fd = self.drag@np.square(self.linear_velocity())

        # Gravity Vector
        self.gravity = np.array([0, 0, -G]).reshape(-1, 1)

        # Transformation Matrices
        self.R_phi = np.array(
            [
                [c(self.phi), -s(self.phi), 0],
                [s(self.phi), c(self.phi), 0],
                [0, 0, 1]
            ]
        )

        self.R_theta = np.array(
            [
                [1, 0, 0],
                [0, c(self.theta), -s(self.theta)],
                [0, s(self.theta), c(self.theta)]
            ]
        )

        self.R_psi = np.array(
            [
                [c(self.psi), -s(self.psi), 0],
                [s(self.psi), c(self.psi), 0],
                [0, 0, 1]
            ]
        )

        self.R = self.R_phi @ self.R_theta @ self.R_psi

        self.W =np.array(
            [
                [1, 0, -s(self.theta)],
                [0, c(self.phi), c(self.theta)*s(self.phi)],
                [0, -s(self.phi), c(self.theta)*c(self.phi)]
            ]
        )

        self.acceleration = np.zeros((3, 1))

        self.sensors = []
    # Function to step, i.e. set the angular velocties, to be called externally by the user
    def __step__(self, velocities):
        self.w1, self.w2, self.w3, self.w4 = velocities[0], velocities[1], velocities[2], velocities[3]
        # Decide on this, whether, you need to update as soon as you step or not
        self.update()

    # All State Update functions
    def __update_transformations__(self):
        self.R_phi = np.array(
            [
                [c(self.phi), -s(self.phi), 0],
                [s(self.phi), c(self.phi), 0],
                [0, 0, 1]
            ]
        )

        self.R_theta = np.array(
            [
                [1, 0, 0],
                [0, c(self.theta), -s(self.theta)],
                [0, s(self.theta), c(self.theta)]
            ]
        )

        self.R_psi = np.array(
            [
                [c(self.psi), -s(self.psi), 0],
                [s(self.psi), c(self.psi), 0],
                [0, 0, 1]
            ]
        )

        self.R = self.R_phi @ self.R_theta @ self.R_psi
        
        self.W =np.array(
            [
                [1, 0, -s(self.theta)],
                [0, c(self.phi), c(self.theta)*s(self.phi)],
                [0, -s(self.phi), c(self.theta)*c(self.phi)]
            ]
        )

    def __update_thrust_and_torque__(self):
        self.thrust = np.array(
            [
                [0],
                [0],
                [K*(self.w1**2 + self.w2**2 + self.w3**2 + self.w4**2)]
            ])

        # Torque Vector
        self.torque = np.array(
            [
                [L*K*(self.w1**2 - self.w3**2)],
                [L*K*(self.w2**2 - self.w4**2)],
                [B*(self.w1**2 - self.w2**2 + self.w3**2 - self.w4**2)]
            ]
        )

        # Drag Force Vector
        self.fd = self.drag @ np.square(self.linear_velocity())

    def __update_acceleration__(self):
        """Uses the omegas to update acceleration"""
        self.acceleration = self.gravity + (1/MASS)*self.R@self.thrust #- (1/MASS)*self.fd

    def __update_omega_dot__(self):
        """Updates omega_dot to calculate final state vector"""
        ang_vel = self.angular_velocity()
        cross_pdt = np.cross(ang_vel.reshape(3,), (self.inertia@ang_vel).reshape(3,)).reshape(3, 1)
        MM = self.torque - cross_pdt

        w_dot = np.linalg.inv(self.inertia)@MM
        
        self.p = w_dot[0][0]
        self.q = w_dot[1][0]
        self.r = w_dot[2][0]
    
    def update(self):
        """This function is called everytime to update the state of the system"""
        # At this point, we assume that the angular velocities are set and hence we go on to update
        # simulation step. This will finally be updated as a gym environment, hence we can easily call the 
        # functions defined in the gym environment to update the velocities.
        self.__update_transformations__()
        self.__update_thrust_and_torque__()
        self.__update_acceleration__()
        self.__update_omega_dot__()

        angle = self.angular_position() + self.angular_velocity() * DT

        # Set the angles
        self.phi = self.normalise_theta(angle[0][0])
        self.theta = self.normalise_theta(angle[1][0])
        self.psi = self.normalise_theta(angle[2][0])

        vel = self.linear_velocity() + self.acceleration * DT

        # set the velocities
        self.vx = vel[0][0]
        self.vy = vel[1][0]
        self.vz = vel[2][0]

        position = self.linear_position() + self.linear_velocity() * DT

        # set the positions
        self.x = position[0][0]
        self.y = position[1][0]
        self.z = position[2][0]

    #!--- Helper functions ---!
    def normalise_theta(self, angle):
        """This is used normalise the angle within -pi to pi"""
        if angle > np.pi:
            while angle > np.pi:
                angle -= 2*np.pi
            return angle
        elif angle < -np.pi:
            while angle < np.pi:
                angle += 2*np.pi
            return angle
        return angle

    #!--- Attaching Sensors ---!
    def attach_sensor(self, sensor: Sensor):
        self.sensors.append(sensor)
    
    def list_sensors(self):
        for sensor in self.sensors:
            print(sensor.__class__.__name__)