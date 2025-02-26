import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class SENSOR():
    def __init__(self, linkName):
        self.linkName = linkName
        self.Prepare_To_Sense()
        
    def Prepare_To_Sense(self):
        self.values = numpy.zeros(c.RUNTIME)

    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

    def Save_Values(self):
        numpy.save('data/'+self.linkName+'.npy', self.values)