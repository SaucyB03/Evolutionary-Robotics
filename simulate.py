import sys

import constants as c
from simulation import SIMULATION

directOrGUI = sys.argv[1]
solutionID = int(sys.argv[2])
simulation = SIMULATION(directOrGUI, solutionID)
simulation.run()
simulation.Get_Fitness()
simulation.__del__()
