"""Main Logger class that displays all Flight Data"""
import matplotlib.pyplot as plt
from drone_sim.sim import Drone

class Logger:
    def __init__(self, drone: Drone):
        self.drone = drone
        self.pos_fig, self.pos_axs =  plt.subplots(2, 3)
        self.vel_fig, self.vel_axs = plt.subplots(2, 3)
        self.accel_fig, self.accel_axs = plt.subplots(3, 1)
        self.rotor_fig, self.rotor_axs = plt.subplots(4, 1)

        self.pos_fig.suptitle("Positions")
        self.vel_fig.suptitle("Velocities")
        self.accel_fig.suptitle("Accelerations")
        self.rotor_fig.suptitle("Rotor Velocities")

        # Add Titles
        self.pos_axs[0, 0].set_title("X-Position")
        self.pos_axs[0, 1].set_title("Y-Position")
        self.pos_axs[0, 2].set_title("Z-Position")
        self.pos_axs[1, 0].set_title("Roll-Position")
        self.pos_axs[1, 1].set_title("Pitch-Position")
        self.pos_axs[1, 2].set_title("Yaw-Position")

        self.vel_axs[0, 0].set_title("Vx")
        self.vel_axs[0, 1].set_title("Vy")
        self.vel_axs[0, 2].set_title("Vz")
        self.vel_axs[1, 0].set_title("P")
        self.vel_axs[1, 1].set_title("Q")
        self.vel_axs[1, 2].set_title("R")

        self.accel_axs[0].set_title("Ax")
        self.accel_axs[1].set_title("Ay")
        self.accel_axs[2].set_title("Az")

        self.rotor_axs[0].set_title("w1")
        self.rotor_axs[1].set_title("w2")
        self.rotor_axs[2].set_title("w3")
        self.rotor_axs[3].set_title("w4")

        # Store the data for the flight
        self.x, self.y, self.z = [], [], []
        self.phi, self.theta, self.psi = [], [], []

        self.vx, self.vy, self.vz = [], [], []
        self.p, self.q, self.r = [], [], []

        self.ax, self.ay, self.az = [], [], []
        self.w1, self.w2, self.w3, self.w4 = [], [], [], []

    def update(self):
        ax, ay, az = self.drone.acceleration[0][0], self.drone.acceleration[1][0], self.drone.acceleration[2][0]
        self.x.append(self.drone.x)
        self.y.append(self.drone.y)
        self.z.append(self.drone.z)
        self.phi.append(self.drone.phi)
        self.theta.append(self.drone.theta)
        self.psi.append(self.drone.psi)
        
        self.vx.append(self.drone.vx)
        self.vy.append(self.drone.vy)
        self.vz.append(self.drone.vz)
        self.p.append(self.drone.p)
        self.q.append(self.drone.q)
        self.r.append(self.drone.r)

        self.ax.append(ax)
        self.ay.append(ay)
        self.az.append(az)
        
        self.w1.append(self.drone.w1)
        self.w2.append(self.drone.w2)
        self.w3.append(self.drone.w3)
        self.w4.append(self.drone.w4)

    def plot(self):
        self.pos_axs[0, 0].plot(self.x)
        self.pos_axs[0, 1].plot(self.y)
        self.pos_axs[0, 2].plot(self.z)

        self.pos_axs[1, 0].plot(self.phi)
        self.pos_axs[1, 1].plot(self.theta)
        self.pos_axs[1, 2].plot(self.psi)

        self.vel_axs[0, 0].plot(self.vx)
        self.vel_axs[0, 1].plot(self.vy)
        self.vel_axs[0, 2].plot(self.vz)

        self.vel_axs[1, 0].plot(self.p)
        self.vel_axs[1, 1].plot(self.q)
        self.vel_axs[1, 2].plot(self.r)

        self.accel_axs[0].plot(self.ax)
        self.accel_axs[1].plot(self.ay)
        self.accel_axs[2].plot(self.az)

        self.rotor_axs[0].plot(self.w1)
        self.rotor_axs[1].plot(self.w2)
        self.rotor_axs[2].plot(self.w3)
        self.rotor_axs[3].plot(self.w4)

        plt.show()



