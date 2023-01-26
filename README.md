# pythonDocker
Using docker as alternative to gym atari issue on Windows


# Docker command
```
docker run -it --rm --name my-running-script -v %cd%:/usr/src/myapp -w /usr/src/myapp python:3.7 python RL_breakout_dqn_test.py
```
