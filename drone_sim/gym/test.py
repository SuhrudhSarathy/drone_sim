import gym
import numpy as np
from simple_drone_env import SimpleDroneEnv

env = SimpleDroneEnv()

for t in range(1000):
    action = np.array([1.0, 0.99, 0.99, 1.0])
    print(action)

    obs, reward, done, _ = env.step(action)
    #print(obs, done)

    print(reward)

    env.render()

    if done:
        break