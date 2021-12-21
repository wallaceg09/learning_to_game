import uuid

import gym
from gym import wrappers
from pyvirtualdisplay import Display

if __name__ == '__main__':
    virtual_display = Display(visible=False, size=(1400, 900))
    virtual_display.start()

    env = gym.make('CartPole-v0')
    env = wrappers.Monitor(env, f"tmp/{uuid.uuid4()}")

    try:
        env.reset()
        for _ in range(1000):
            env.render()
            env.step(env.action_space.sample())  # take a random action
    finally:
        env.close()
        print("Finished")
