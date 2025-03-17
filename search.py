import os
import pybullet
from hillclimber import HILLCLIMBER

hc = HILLCLIMBER()
hc.Evolve()
hc.Show_Best()