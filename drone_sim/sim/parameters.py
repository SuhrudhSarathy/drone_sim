"""File to Store common parameters for the drone"""

#! -- Simulation parameters --!
DT = 0.002
#! -- ********* --!

#! -- Drone parameters --!
MASS = 0.468
RADIUS_PROP = 0.1
K = 2.980e-6
B = 1.140e-7
L = 0.225
G = 9.8

NULL_ROT = 620.2943

# Inertia
IXX = 4.856e-3
IYY = 4.856e-3
IZZ = 8.801e-3

# Drag
AX = 0.25
AY = 0.25
AZ = 0.25

#! -- ********* --!

#! -- Sensor Parameters --!
# GPS
GPS_MEAN = 0
GPS_STDDEV = 0.1

# IMU
IMU_MEANS = {
    "accelx": 0,
    "accely": 0,
    "accelz": 0,

    "gyrox": 0,
    "gyroy": 0,
    "gyroz": 0
}
IMU_STDDEV = {
    "accelx": 0.1,
    "accely": 0.1,
    "accelz": 0.1,

    "gyrox": 0.1,
    "gyroy": 0.1,
    "gyroz": 0.1
}
#! -- ********* --!

#! -- Plotting Params --!
PLT_PAUSE = 1e-6