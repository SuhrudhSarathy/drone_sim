import gym
from gym import spaces
from drone_sim.sim import Drone
from drone_sim.sim import PositionTracker, IMU
from drone_sim.sim.parameters import *
from drone_sim.viz import Graphics
from drone_sim.viz import Body

import numpy as np

class SimpleDroneEnv(gym.Env):
    metadata = {'render.modes': ["human"]}

    def __init__(self, goal_position=[0, 5, 5]) -> None:
        super(SimpleDroneEnv, self).__init__()

        # Initialise the Drone class, attach body and sensors, and make the Graphics object
        # Reset will be manually called in the step function
        self.drone = Drone(0, 0, 2, enable_death=False)
        self.body = Body()

        self.body.attach_to(self.drone)

        self.ui = Graphics()
        self.ui.add_actor(self.drone)

        self.goal_position = goal_position
        self.init_position = [0, 0, 2]
        # Gym
        self.obs_low = -np.inf
        self.obs_high = -np.inf
        
        # Define action and observation space
        # We will use a continous action space for the values of the motor's rotation
        self.action_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)
        self.observation_space = spaces.Box(low=self.obs_low, high=self.obs_high, shape=(3, 3), dtype=np.float32)
        self.reward_range = (0, 100)

        # Some rotation values
        self.NULL_ROT = NULL_ROT

    def step(self, action):
        assert self.action_space.contains(action), f"{action} doesnot exist in the action space"

        # The action is of the type (w1, w2, w3, w4)
        self.drone.step(action*NULL_ROT)


        # Function has to return the observations
        observation = np.array(
            [
                [self.drone.x, self.drone.y, self.drone.z],
                [self.drone.acceleration[0][0], self.drone.acceleration[1][0], self.drone.acceleration[2][0]],
                [self.drone.p, self.drone.q, self.drone.r]
            ]
        )

        # Reward is calculated as the ratio of 1 - (dist(present, goal)/dist(start, goal))
        dist_to_go = self.dist([self.drone.x, self.drone.y, self.drone.z], [self.init_position[0], self.init_position[1], self.init_position[2]])
        total_dist = self.dist([self.goal_position[0], self.goal_position[1], self.goal_position[2]], [self.init_position[0], self.init_position[1], self.init_position[2]])

        reward = 1 - dist_to_go/total_dist

        # Termination condition
        if abs(self.drone.phi) > np.radians(60.0) or abs(self.drone.theta) > np.radians(60):
            done = True
            self.drone.__reset__()
            reward -= 5

        # Condition 2: If the z altitude goes negative, we reset the simulation
        elif self.drone.z < 0:
            done = True
            self.drone.__reset__()
            reward -= 5

        elif dist_to_go < 0.01:
            done = True
            reward += 10
        
        else:
            done = False


        return observation, reward, done, {}

    def reset(self):
        # Function to reset the simulation
        self.drone.__reset__()
        observation = np.array(
            [
                [self.drone.x, self.drone.y, self.drone.z],
                [self.drone.acceleration[0][0], self.drone.acceleration[1][0], self.drone.acceleration[2][0]],
                [self.drone.p, self.drone.q, self.drone.r]
            ]
        )

        return observation

    def render(self):
        # Function to render the simulation
        self.ui.update()

    # Helper functions
    def dist(self, x1, x2):
        x, y, z = x1
        X, Y, Z = x2

        return np.sqrt((x-X)**2 + (y-Y)**2 + (z-Z)**2)
