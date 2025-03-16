import os
import pybullet

for i in range(5):
    os.system("python generate.py")
    os.system("python simulate.py")