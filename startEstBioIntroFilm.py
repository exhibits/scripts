#!/usr/bin/


import os
import time
import threading
from subprocess import Popen, PIPE, STDOUT, call

time.sleep(1)

bgImage = Popen(["feh", "-F", "/home/pi/blackBG.jpg"])

# mouse x,y
mouse = os.popen("xdotool getmouselocation")
mouse = str(mouse.read())

# create a timer
t = None
omxSlide = None
mouse = None
oMouse = None

def playSlideShow():
	global t
	global omxSlide
	os.popen("sudo pkill omxplayer") #attempts to close any omxplayers
	time.sleep(0.2)		# added time.sleep(0.2)
	omxSlide = Popen(["omxplayer", "/home/pi/slideShowIntro.mp4"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
	t = threading.Timer(107, playSlideShow) # adjust to length of file to be played
	t.start()

playSlideShow()
time.sleep(0.5)

while True:
	oMouse = mouse
	time.sleep(0.2)
	mouse = os.popen("xdotool getmouselocation")
	mouse = str(mouse.read())

	if oMouse != mouse:
		# close slide show
		omxSlide.communicate(input='q')[0]
		time.sleep(0.2)	# added time.sleep(0.2)	
		t.cancel() #stop the playSlideShow timer reapeat

		# play film		
		call(["omxplayer", "-o", "hdmi", "/home/pi/main.mp4"])

		# reset mouse position
		mouse = os.popen("xdotool getmouselocation")
		mouse = str(mouse.read())

		# restart slide show
		playSlideShow()

