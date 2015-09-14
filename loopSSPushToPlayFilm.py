#!/usr/bin/python
#######################################################################
# Michael Godfrey
# 9/14/2015
# Loops a screen saver until button input on pin12, then plays film.
# Set locations of desired film files below
#
# $ crontab -e
# @reboot ./home/pi/gitHub/exhibits/scripts/loopSSPushToPlayFilm.py
#######################################################################
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

screenSaver = None
#######################################################################
# Set Correct File Locations HERE:
#######################################################################
screenSaverLocation 	= '/home/pi/prepLabIntro.mp4'
filmLocation 		= '/opt/vc/src/hello_pi/hello_video/test.h264'
bgLocation		= '/home/pi/blackBG.jpg'
#######################################################################

def playScreenSaver():
	global screenSaver
	# If shell=True, then args should be one string, not a list
	screenSaver = subprocess.Popen(
		['omxplayer', '--loop', '--blank', '--no-osd', screenSaverLocation], 
		stdin=subprocess.PIPE, 
		stdout=subprocess.PIPE, 
		stderr=subprocess.STDOUT,
		shell=False
	)

# MAIN
# fbi can run without Xterm, use feh if Xterm
subprocess.Popen(['fbi', '-noverbose', bgLocation], shell=False) 
# non-blocking
playScreenSaver()

while True:	
	try:
		if GPIO.input(12):
			print('Killing Screen Saver.')
			# Interact with process: Send data to stdin, returns tubple (stdoutdata, stderrdata)
			screenSaver.communicate('q')
			print('Loading Film...')
			film = subprocess.Popen(
				['omxplayer', filmLocation], 
				stdin=subprocess.PIPE, 
				stdout=subprocess.PIPE, 
				stderr=subprocess.STDOUT,
				shell=False
			)
			film.wait()
			print("Film is OVER - Restarting ScreenSaver")
			playScreenSaver()
		else:
			time.sleep(.1)
	# End program cleanly with keyboard
	except KeyboardInterrupt:
		print "  Quit"
		# Reset GPIO settings
		GPIO.cleanup()
		# Exit py script
		sys.exit()

