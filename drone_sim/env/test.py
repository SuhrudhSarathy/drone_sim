import gym
from simple_drone_env import SimpleDroneEnv

env = SimpleDroneEnv()

for t in range(100):
    action = [env.NULL_ROT, 0, env.NULL_ROT, 0]

    obs, reward, done, _ = env.step(action)

    print(reward)

    env.render()

    if done:
        break