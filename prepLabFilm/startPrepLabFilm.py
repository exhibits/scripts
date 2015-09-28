#!/usr/bin/python
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
from subprocess import Popen, PIPE, call
from threading import Timer

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
bgImage = Popen(["fbi", "-noverbose", "blackBG.jpg"])

def playSlideShow():
	global omxSlide
	global t

	# test video file
	#omxSlide = Popen(["omxplayer", "/opt/vc/src/hello_pi/hello_video/test.h264"], stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
	omxSlide = Popen(["omxplayer", "/home/pi/prepLabIntro.mp4"], stdout=PIPE, stdin=PIPE, stderr=PIPE)

	# slide show is 60 + 1 for delay
	t = Timer(61, playSlideShow)
	t.start()

playSlideShow()

while True:	
	if GPIO.input(18):
		# close slide show
		omxSlide.stdin.write('q')
		t.cancel() #stop the playSlideShow timer reapeat

		# play film		
		call(["omxplayer", "/home/pi/prepLabFilm.mp4"])

		# restart slide show
		playSlideShow()
	else:
		time.sleep(.1)

