# docker run -it --rm --name my-running-script -v C:\Users\OBAS\Documents\Python_Scripts\Python_Scripts\stableBaselines_examples:/usr/src/myapp -w /usr/src/myapp python:3.7 python RL_breakout_dqn.py

import subprocess

subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

import gym
import imageio
import numpy as np

env = gym.make('BreakoutDeterministic-v4', render_mode="rgb_array")
_ = env.reset()
writer = imageio.get_writer('test.mp4', fps=20)
for i in range(10):
    act = env.action_space.sample()

    obs = env.step(act)

    img = env.render()

    writer.append_data(img)

env.close()
#display_frames_as_gif(frames)
writer.close()