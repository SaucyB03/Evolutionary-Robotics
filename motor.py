import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import constants as c

class MOTOR():
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        print(self.jointName)

        if self.jointName == b'Torso_BackLeg':
            self.frequency = c.frequency/2
        
        self.phaseOffset = c.phaseOffset

        self.increment = 2 * numpy.pi / c.RUNTIME * 5
        self.arr = numpy.array([(i * self.increment) for i in range(c.RUNTIME)])

        self.motorValues = self.amplitude * numpy.sin(self.frequency * self.arr + self.phaseOffset)

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName=self.jointName, controlMode= p.POSITION_CONTROL, targetPosition= self.motorValues[t], maxForce=c.MOTOR_MAX_FORCE)

    def Save_Values(self):
        numpy.save('data/'+self.jointName+'.npy', self.motorValues)