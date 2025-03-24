import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

import os

from sensor import SENSOR
from motor import MOTOR

class ROBOT():
    def __init__(self, ID):
        self.sensors = {}
        self.motors = {}
        self.myID = ID
        self.robot = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain"+str(self.myID)+".nndf")
        os.system("del brain"+str(self.myID)+".nndf")

    def Prepare_To_Sense(self):
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Prepare_To_Act(self):
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)
    
    def Sense(self, t):
        for sens in self.sensors.values():
            sens.Get_Value(t)

    def Think(self):
        self.nn.Update()

    def Act(self):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self.robot, desiredAngle)

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robot,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordinateOfLinkZero = positionOfLinkZero[0]

        f = open("tmp"+str(self.myID)+".txt", "w")
        f.write(str(xCoordinateOfLinkZero))
        f.close()

        os.rename("tmp"+str(self.myID)+".txt", "fitness"+str(self.myID)+".txt")