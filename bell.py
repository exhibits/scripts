#!/usr/bin/python
#########################################################
# Michael Godfrey
# 11/14/2014/
# Pushbutton program for Lighhouse bell push-to-play.
# AUTORUN:
# 	sudo nano ~/.config/lxsession/LXDE/autostart
# 	make sure that the python call is given superuser
#########################################################
import time
import datetime
import subprocess

import RPi.GPIO as GPIO
# Use Default Pin Numbers
GPIO.setmode(GPIO.BOARD)
# Disable warnings
GPIO.setwarnings(False)
# set pin 18 as input
GPIO.setup(18, GPIO.IN)

while True:	
	if GPIO.input(18):
		#ts = time.time()
		#st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
		#print("\nbutton pressed: ", st)
		subprocess.call(["omxplayer", "/home/pi/DrumPointLighthouseBell3Strikes.wav"])
	else:
		time.sleep(.1)

