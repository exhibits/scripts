#!/usr/bin/python
#######################################################################
# Michael Godfrey
# 9/14/2015
#
# Needs xdotool to capture mouse/touch input:
# $ sudo apt-get install xdotool
#
# Make sure you have updated omxplayer:
# $ sudo apt-get install omxplayer
#
# Loops a screen saver until MOUSE move, then plays film.
#
# *Remember* to set locations of desired files. See Below.
#
# Autorun on Desktop load:
# $ sudo nano ~/.config/lxsession/LXDE/autostart
# sudo ./home/pi/gitHub/exhibits/scripts/loopSSPushToPlayFilm.py
#######################################################################
import time
import subprocess
import sys
import os
#######################################################################
# Set Correct File Locations HERE:
#######################################################################
screenSaverLocation 	= '/home/pi/prepLabIntro.mp4'
filmLocation 		= '/opt/vc/src/hello_pi/hello_video/test.h264'
bgLocation		= '/home/pi/blackBG.jpg'
#######################################################################
screenSaver = None
# mouse x,y
mouse = os.popen("xdotool getmouselocation")
mouse = str(mouse.read())
oMouse = None

def playScreenSaver():
	global screenSaver
	screenSaver = subprocess.Popen(
		['omxplayer', '--loop', '--blank', '--no-osd', screenSaverLocation], 
		stdin=subprocess.PIPE, 
		stdout=subprocess.PIPE, 
		stderr=subprocess.STDOUT,
		shell=False
	)

# MAIN
# Fullscreen, HidePointer
subprocess.Popen(['feh', '-FH', bgLocation], shell=False) 
# non-blocking
playScreenSaver()

while True:	
	try:
		oMouse = mouse
		time.sleep(0.2)
		mouse = os.popen("xdotool getmouselocation")
		mouse = str(mouse.read())

		if oMouse != mouse:
			print('Killing Screen Saver.')
			# Interact with process: Send data to stdin, returns tubple (stdoutdata, stderrdata)
			screenSaver.communicate('q')
			print('Loading Film...')
			# OLD CALL... May need params to get audio working over HDMI for Screen.
			#call(["omxplayer", "-o", "hdmi", "/home/pi/main.mp4"])
			film = subprocess.Popen(
				['omxplayer', filmLocation], 
				stdin=subprocess.PIPE, 
				stdout=subprocess.PIPE, 
				stderr=subprocess.STDOUT,
				shell=False
			)
			film.wait()
			print("Film is OVER - Restarting ScreenSaver")
			# reset mouse position
			mouse = os.popen("xdotool getmouselocation")
			mouse = str(mouse.read())
			playScreenSaver()
		else:
			time.sleep(.1)
	# End program cleanly with keyboard
	except KeyboardInterrupt:
		print "  Quit"
		# Exit py script
		sys.exit()

