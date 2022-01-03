
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from drone_sim.sim.drone import Drone
from drone_sim.sim.parameters import NULL_ROT
from drone_sim.viz.body import Body
from drone_sim.viz.visualiser import Graphics

drone = Drone(True)

# Make a body
body = Body()
body.attach_to(drone)

# Make Graphics object
ui = Graphics()
ui.add_actor(drone)

drone.z = 2.5
r = NULL_ROT

w1, w2, w3, w4 = r, -r, r, -r

for i in range(1000):
    drone.__step__([w1, w2, w3, w4])
    ui.update()