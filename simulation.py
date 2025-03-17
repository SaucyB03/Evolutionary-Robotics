import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time

from world import WORLD
from robot import ROBOT

class SIMULATION:

    def __init__(self, directOrGUI):
        self.directOrGUI = directOrGUI
        if self.directOrGUI == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        elif self.directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0, c.GRAVITY)

        self.world = WORLD()
        self.robot = ROBOT()

        pyrosim.Prepare_To_Simulate(self.robot.robot)
        
        self.robot.Prepare_To_Sense()
        self.robot.Prepare_To_Act()
        


    def run(self):
        for t in range(c.RUNTIME):
            p.stepSimulation()
            self.robot.Sense(t)
            self.robot.Think()
            self.robot.Act()

            if self.directOrGUI == "GUI":
                time.sleep(c.TIME_STEP)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()