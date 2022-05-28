"""File to Store common parameters for the drone"""

#! -- Simulation parameters --!
DT = 0.01
#! -- ********* --!

#! -- Drone parameters --!
MASS = 0.65
RADIUS_PROP = 0.1
KF = 3.13e-5
KM = 7.5e-7
GAMMA = KM/KF
L = 0.23
G = 9.8

NULL_ROT = ((MASS*G/(4*KF))**0.5)

# Inertia
IXX = 7.5e-3
IYY = 7.5e-3
IZZ = 1.3e-2

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