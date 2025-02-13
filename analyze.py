import numpy
import matplotlib.pyplot

backLegSensorValues = numpy.load('./data/BLSensVal.npy')
frontLegSensorValues = numpy.load('./data/FLSensVal.npy')

matplotlib.pyplot.plot(backLegSensorValues, label="Back Leg", linewidth=3)
matplotlib.pyplot.plot(frontLegSensorValues, label="Front Leg")
matplotlib.pyplot.legend(loc="upper right")
matplotlib.pyplot.show()