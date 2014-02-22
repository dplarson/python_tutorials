"""
Example that does not require a Beaglebone.

David Larson
dplarson@ucsd.edu

"""

# open data file for reading
data_file = open('example_data.txt', 'r')

# read value out [bits], making sure to convert value from string to float
# (so we can do calculations)
bits = float(data_file.read())

# close file
data_file.close()

# convert to bit fraction
bit_fraction = bits / 4096

# convert to millivolts
millivolts = bit_fraction * 1800

# convert to degrees C
temperature_C = (millivolts - 500) / 10

# convert to degrees F
temperature_F = (temperature_C * 9 / 5) + 32

# print results
print "{:.0f} bits".format(bits)
print "{:.3f} bit fraction".format(bit_fraction)
print "{:.3f} V".format(millivolts / 1.0E3)
print "{:.2f} C".format(temperature_C)
print "{:.2f} F".format(temperature_F)
