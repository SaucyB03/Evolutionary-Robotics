import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('./data/BLSensVal.npy')
frontLegSensorValues = numpy.load('./data/FLSensVal.npy')
FtargetAngles = numpy.load('./data/frontLegtargetAngles.npy')
BtargetAngles = numpy.load('./data/backLegtargetAngles.npy')

# matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=3)
# matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg")
# matplotlib.pyplot.legend(loc="upper right")
# matplotlib.pyplot.show()

matplotlib.pyplot.plot(FtargetAngles, label="Front Leg Targ Ang", linewidth = 4)
matplotlib.pyplot.plot(BtargetAngles, label="Back Leg Targ Ang")
matplotlib.pyplot.legend(loc="upper right")
matplotlib.pyplot.show()