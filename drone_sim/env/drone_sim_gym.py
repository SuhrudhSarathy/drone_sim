import gym
from drone_sim.sim import Drone
from drone_sim.sim import PositionTracker, IMU
from drone_sim.sim.parameters import *
from drone_sim.viz import Graphics
from drone_sim.viz import Body

class DroneSimEnv(gym.Env):
    metadata = {'render.modes': ["human"]}

    def __init__(self) -> None:
        super(DroneSimEnv, self).__init__()

        # Initialise the Drone class, attach body and sensors, and make the Graphics object
        self.drone = Drone(0, 0, 2)
        self.body = Body()
        self.imu = IMU()
        self.gps = PositionTracker()
        
        self.body.attach_to(self.drone)
        self.imu.attach_to(self.drone)
        self.gps.attach_to(self.drone)

        self.ui = Graphics()
        self.ui.add_actor(self.drone)
        
        # Define action and observation space
