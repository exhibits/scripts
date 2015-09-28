#!/usr/bin/python
######################################################
# Michael Godfrey
# 9/14/2015
######################################################
import time
import subprocess
import sys

import RPi.GPIO as GPIO
# Use Default Pin Numbers
GPIO.setmode(GPIO.BOARD)
# Disable warnings
GPIO.setwarnings(False)
# Set pin 12 as Input - (GPIO18)
GPIO.setup(12, GPIO.IN)

while True:	
	try:
		if GPIO.input(12):
			print("--Button Pressed--")
			# Do stuff here. 
			time.sleep(1)
		else:
			time.sleep(.1)

	# End program cleanly with keyboard
	except KeyboardInterrupt:
		print "  Quit"
		# Reset GPIO settings
		GPIO.cleanup()
		# Exit py script
		sys.exit()

