#!/usr/bin/python
######################################################
# Michael Godfrey
# 09/14/2015/
# AUTORUN:
######################################################
import time
import datetime
import subprocess

try:
	import RPi.GPIO as GPIO
except:
	print "Error importing RPI.GPIO! Are you super? Has the module been installed?"

# Use Default Pin Numbers
GPIO.setmode(GPIO.BOARD)
# Disable warnings
#GPIO.setwarnings(False)
# set pin 18 as input
GPIO.setup(18, GPIO.IN)
#GPIO.setup(channel, GPIO.OUT)

while True:	
	if GPIO.input(18):

		ts = time.time()

		subprocess.call(["omxplayer", "/home/pi/DrumPointLighthouseBell3Strikes.wav"])
	else:
		time.sleep(.1)

