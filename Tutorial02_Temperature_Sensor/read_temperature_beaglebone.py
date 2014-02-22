"""
Measure temperature using TMP36 on Beaglebone Black.

David Larson
dplarson@ucsd.edu

"""

# import required packages
from Adafruit_BBIO import ADC
import time

# set the analog pin (that the TMP36 is connected to)
pin = 'P9_39'

# initialize the Beaglebone for measuring from the analog pins
ADC.setup()

# measure the analog output as a bit fraction (number of bits / 4096)
# NOTE: 4096 = 2^12 = 12-bit resolution
bit_fraction = ADC.read(pin)

# convert bit fraction to millivolts
# NOTE: 1800 mV is the max output of the Beaglebone analog pins
millivolts = bit_fraction * 1800

# convert millivolts to degrees C
# NOTE: 10 mV = 1 degree C and -500 mV is a calibration offset for the TMP36 sensor
temperature_C = (millivolts - 500) / 10

# convert C to F
temperature_F = (temperature_C * 9 / 5) + 32

# output the values
# simple formatting
print "{0}, {1} mV, {2} C, {3} F".format(bit_fraction, 
        millivolts, temperature_C, temperature_F)

# uncomment lines below for fancy formatting
#print "{0:.3f}, {1:.3f} V, {2:.2f} C, {3:.2f} F".format(bit_fraction,
#        millivolts, temperature_C, temperature_F)
