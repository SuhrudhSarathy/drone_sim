"""Tests a multidrone simulation"""
from drone_sim.sim import Drone
from drone_sim.viz import Body
from drone_sim.viz import Graphics, Logger
from drone_sim.sim.parameters import *

from time import time

import numpy as np


drone = Drone(enable_death=True)
drone.z = 2.5
drone.phi = 0


# Make a body
body = Body()
body.attach_to(drone)


# Make Graphics object
# ui = Graphics(set_limits=True)
# ui.add_actor(drone)

logger = Logger(drone=drone)


for i in range(100):
    # w1, w2, w3, w4 = x[0][0], x[1][0], x[2][0], x[3][0]
    w1, w2, w3, w4 = 0.8*NULL_ROT, 0.7*NULL_ROT, 0.8*NULL_ROT, 0.9*NULL_ROT
    # print(drone.vx)

    time_ = time()
    drone.step([w1, w2, w3, w4])
    logger.update()
    # ui.update()
    # print(drone.angular_position())
logger.plot()
print("Done")