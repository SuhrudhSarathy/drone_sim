
"""Tests a multidrone simulation"""
from drone_sim.sim import Drone
from drone_sim.viz import Body
from drone_sim.viz import Graphics
from drone_sim.sim.parameters import *

from time import time

import numpy as np

def calculate_rotor_vels(f, tphi, ttheta, tpsi):
    b = np.array([f, tphi, ttheta, tpsi]).reshape(-1, 1)

    a = np.array(
        [
            [K, K, K, K],
            [L*K, 0, 0, -L*K],
            [0, L*K, -L*K, 0],
            [B, -B, B, -B]
        ]
    )
    
    x = np.linalg.solve(a, b)

    return x

drone = Drone(True)
drone.z = 2.5

drone.phi = 1
print(drone.phi)

# Make a body
body = Body()
body.attach_to(drone)


# Make Graphics object
ui = Graphics()
ui.add_actor(drone)

T = (AX * 5)/np.sin(drone.phi)
print(T)

for i in range(1050):
    x = calculate_rotor_vels(T, 0, 0, 0)
    # w1, w2, w3, w4 = x[0][0], x[1][0], x[2][0], x[3][0]

    if i < 25:

        w1, w2, w3, w4 = NULL_ROT, NULL_ROT, NULL_ROT, 1.1*NULL_ROT
    else:
        w1, w2, w3, w4 = NULL_ROT, NULL_ROT, NULL_ROT, NULL_ROT
    # print(drone.vx)

    time_ = time()
    drone.step([w1, w2, w3, w4])
    ui.update()