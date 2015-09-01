#!/usr/bin/
######################################################
# Michael Godfrey
# 11/14/2014/
# pushbutton player for Paleo Prep Lab
# AUTORUN:
# 	sudo nano ~/.config/lxsession/LXDE/autostart
# 	make sure that the python call is given superuser
# SCREEN RESOLUTION:
# 1184x624 720p (who knew...)
######################################################
# this should be a cronjob on boot, me thinks
######################################################
# UPDATE 9/1/2015
# Dependancies:
# sudo apt-get install fbi 

import time
import subprocess 

import RPi.GPIO as GPIO
# Use Default Pin Numbers
GPIO.setmode(GPIO.BOARD)
# Disable warnings
GPIO.setwarnings(False)
# set pin 18 as input
GPIO.setup(18, GPIO.IN)

t = None
omxSlide = None

# fbi does not require xterm, '-noverbose' removes image info text 
bgImage = subprocess.Popen(["fbi", "-noverbose", "blackBG.jpg"])

def playSlideShow():
	global omxSlide
	global t

	# test video file
	omxSlide = subprocess.Popen(["omxplayer", "/opt/vc/src/hello_pi/hello_video/test.h264"])
	#omxSlide = subprocess.Popen(["omxplayer", "/home/pi/prepLabIntro.mp4"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)

	# There is a better way to do this... should not need a timer.
	t = threading.Timer(60, playSlideShow)
	t.start()

playSlideShow()

while True:	
	if GPIO.input(18):
		# close slide show
		omxSlide.communicate(input='q')[0]
		t.cancel() #stop the playSlideShow timer reapeat

		# play film		
		subprocess.call(["omxplayer", "/home/pi/prepLabFilm.mp4"])

		# restart slide show
		playSlideShow()
	else:
		time.sleep(.1)

