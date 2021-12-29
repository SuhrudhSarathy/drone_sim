import numpy as np
from numpy import sin as s, cos as c, tan as t

theta = 0.2
phi = 0.5

Wn_inv = np.array(
    [
        [1, s(phi)*t(theta), c(phi)*t(theta)],
        [0, c(phi), -s(phi)],
        [0, s(phi)/c(theta), c(phi)/c(theta)]
    ]
)

Wn = np.array(
    [
        [1, 0, -s(theta)],
        [0, c(phi), c(theta)*s(phi)],
        [0, -s(phi), c(theta)*c(phi)]
    ]
)

