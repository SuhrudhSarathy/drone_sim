from sim.drone import Drone
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

drone = Drone()
drone.z = 5
r = 620.2943
w1, w2, w3, w4 = r, r, r, r

X = []
Y = []
Z = []
R = []
P = []
Yaw = []

V = []


t = list(range(1000))

for i in range(1000):
    drone.__step__([w1, w2, w3, w4])
    X.append(drone.x)
    Y.append(drone.y)
    Z.append(drone.z)

    R.append(drone.phi)
    P.append(drone.theta)
    Yaw.append(drone.psi)

    V.append(drone.acceleration[2][0])


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.plot(X, Y, Z)
ax.set_xlim3d([-1.0, 5.0])
ax.set_xlabel('X')

ax.set_ylim3d([-1.0, 5.0])
ax.set_ylabel('Y')

ax.set_zlim3d([0.0, 10.0])
ax.set_zlabel('Z')

fig2, (ax21, ax22, ax23) = plt.subplots(3, 1)
ax21.plot(t, R)
ax22.plot(t, P)
ax23.plot(t, Yaw)

fig3, ax31 = plt.subplots(1, 1)
ax31.plot(t, V)
plt.show()


