import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import time
import random
import sys

import constants as c
from simulation import SIMULATION

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.run()
simulation.Get_Fitness()
simulation.__del__()
