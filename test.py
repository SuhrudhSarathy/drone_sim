from dynamics.drone import Drone
import matplotlib.pyplot as plt

from dynamics.parameters import RHO


drone = Drone()
drone.z = 5000
r = 4.9498
w1, w2, w3, w4 = 0.5*r, -2*r, 0.5*r, -2*r

X = []
Y = []
Z = []
R = []
P = []
Yaw = []


t = list(range(1000))

for i in range(1000):
    drone.__step__([w1, w2, w3, w4])
    X.append(drone.x)
    Y.append(drone.y)
    Z.append(drone.z)

    R.append(drone.phi)
    P.append(drone.theta)
    Yaw.append(drone.psi)

fig, (ax1, ax2, ax3) = plt.subplots(3, 1)
ax1.plot(t, X)
ax2.plot(t, Y)
ax3.plot(t, Z)


fig2, (ax21, ax22, ax23) = plt.subplots(3, 1)
ax21.plot(t, R)
ax22.plot(t, P)
ax23.plot(t, Yaw)

plt.show()


