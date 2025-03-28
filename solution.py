import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os
import time

import constants as c

class SOLUTION:
    def __init__(self, nextAvailableID):
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
        self.myID = nextAvailableID

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B python simulate.py " + directOrGUI + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)

        f = open("fitness"+str(self.myID)+".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("del fitness"+str(self.myID)+".txt")


    def Mutate(self):
        randomRow = random.randint(0,c.numSensorNeurons-1)
        randomCol = random.randint(0,c.numMotorNeurons-1)

        self.weights[randomRow, randomCol] = random.random() * 2 - 1
    
    def Set_ID(self, ID):
        self.myID = ID

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-2.0,2.0, 0.5] , size=[1,1,1])
        pyrosim.End()   

    def Generate_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="Torso", pos=[0,0, 1] , size=[1,1,1])
        pyrosim.Send_Joint( name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", jointAxis = "1 0 0", position = [0,-0.5,1])
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", jointAxis = "1 0 0", position = [0,0.5,1])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,0.5,0] , size=[0.2,1,0.2])
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", jointAxis = "0 1 0", position = [-0.5,0,1])
        pyrosim.Send_Cube(name="LeftLeg", pos=[-0.5,0,0] , size=[1,0.2,0.2])
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", jointAxis = "0 1 0", position = [0.5,0,1])
        pyrosim.Send_Cube(name="RightLeg", pos=[0.5,0,0] , size=[1,0.2,0.2])

        pyrosim.Send_Joint( name = "BackLeg_BackLower" , parent= "BackLeg" , child = "BackLower" , type = "revolute", jointAxis = "1 0 0", position = [0,-1,0])
        pyrosim.Send_Cube(name="BackLower", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "FrontLeg_FrontLower" , parent= "FrontLeg" , child = "FrontLower" , type = "revolute", jointAxis = "1 0 0", position = [0,1,0])
        pyrosim.Send_Cube(name="FrontLower", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "LeftLeg_LeftLower" , parent= "LeftLeg" , child = "LeftLower" , type = "revolute", jointAxis = "0 1 0", position = [-1,0,0])
        pyrosim.Send_Cube(name="LeftLower", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        pyrosim.Send_Joint( name = "RightLeg_RightLower" , parent= "RightLeg" , child = "RightLower" , type = "revolute", jointAxis = "1 1 0", position = [1,0,0])
        pyrosim.Send_Cube(name="RightLower", pos=[0,0,-0.5] , size=[0.2,0.2,1])
        


        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 3, linkName = "RightLeg")
        pyrosim.Send_Sensor_Neuron(name = 4, linkName = "BackLower")
        pyrosim.Send_Sensor_Neuron(name = 5, linkName = "FrontLower")
        pyrosim.Send_Sensor_Neuron(name = 6, linkName = "LeftLower")
        pyrosim.Send_Sensor_Neuron(name = 7, linkName = "RightLower")
        pyrosim.Send_Motor_Neuron( name = 8, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron( name = 9, jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 10, jointName = "Torso_LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 11, jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 12, jointName = "BackLeg_BackLower")
        pyrosim.Send_Motor_Neuron( name = 12, jointName = "FrontLeg_FrontLower")
        pyrosim.Send_Motor_Neuron( name = 13, jointName = "LeftLeg_LeftLower")
        pyrosim.Send_Motor_Neuron( name = 14, jointName = "RightLeg_RightLower")
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])

        pyrosim.End()   

