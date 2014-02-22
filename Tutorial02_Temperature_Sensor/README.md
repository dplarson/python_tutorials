# Analog Temperature Sensor
Measuring temperature using an analog sensor connected to a Beaglebone Black.

## Requirements
- Python 2.7
- ``Adafruit_BBIO`` Python package
- TMP36 analog temperature sensor

## Setup
Connect the TMP36 sensor to the Beaglebone Black following the Adafruit guide: http://learn.adafruit.com/measuring-temperature-with-a-beaglebone-black/overview

**NOTE**: the code assumes the TMP36 is connected to:

- power (3.3V): P9_03
- ground: P9_34 (GNDA_ADC)
- analog output: P9_39 (AIN0)
