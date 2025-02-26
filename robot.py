import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

from sensor import SENSOR
from motor import MOTOR

class ROBOT():
    def __init__(self):
        self.sensors = {}
        self.motors = {}
        self.robot = p.loadURDF("body.urdf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Sense(self, t):
        for sens in self.sensors.values():
            sens.Get_Value(t)

    def Act(self, t):
        for motor in self.motors.values():
            motor.Set_Value(self.robot, t)