
"""Tests a multidrone simulation"""
from drone_sim.sim import Drone
from drone_sim.sim.parameters import NULL_ROT
from drone_sim.viz import Body
from drone_sim.viz import Graphics

drone = Drone(True)
drone.z = 2.5
drone.vx = 0

drone2 = Drone(x=2,z=2,enable_death=True)

# Make a body
body = Body()
body.attach_to(drone)

body2 = Body()
body2.attach_to(drone2)

# Make Graphics object
ui = Graphics()
ui.add_actor(drone)
ui.add_actor(drone2)

r = NULL_ROT

w1, w2, w3, w4 = r, r, r, r

for i in range(1050):

    drone.step([w1, w2, w3, w4])
    ui.update()