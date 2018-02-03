#!/usr/bin/python

"""
	This is the main B3na daemon running most standard services
"""
# Copyright (c) 2010-2018 LiTtl3.1 Industries (LiTtl3.1).
# All rights reserved.
# This source code and any compilation or derivative thereof is the
# proprietary information of LiTtl3.1 Industries and is
# confidential in nature.
# Use of this source code is subject to the terms of the applicable
# LiTtl3.1 Industries license agreement.
#
# Under no circumstances is this component (or portion thereof) to be in any
# way affected or brought under the terms of any Open Source License without
# the prior express written permission of LiTtl3.1 Industries.
#
# For the purpose of this clause, the term Open Source Software/Component
# includes:
#
# (i) any software/component that requires as a condition of use, modification
#	 and/or distribution of such software/component, that such software/
#	 component:
#	 a. be disclosed or distributed in source code form;
#	 b. be licensed for the purpose of making derivative works; and/or
#	 c. can be redistributed only free of enforceable intellectual property
#		rights (e.g. patents); and/or
# (ii) any software/component that contains, is derived in any manner (in whole
#	  or in part) from, or statically or dynamically links against any
#	  software/component specified under (i).
#

# Imports
import logging
import time
import os										# used to allow execution of system level commands
import re
import sys
import socket
import schedule									# 3rd party lib used for alarm clock managment. 
import datetime									
import ConfigParser								# used to parse alfr3ddaemon.conf
from pymongo import MongoClient					# database link 
from threading import Thread
from daemon import Daemon
from random import randint						# used for random number generator

# current path from which python is executed
CURRENT_PATH = os.path.dirname(__file__)

# import my own utilities
sys.path.append(os.path.join(os.path.join(os.getcwd(),os.path.dirname(__file__)),"../"))
import utilities
# import reporting

masterSpeaker = utilities.Speaker()

# set up daemon things
os.system('sudo mkdir -p /var/run/alfr3ddaemon')
#os.system('sudo chown alfr3d:alfr3d /var/run/alfr3ddaemon')

# load up all the configs
config = ConfigParser.RawConfigParser()
config.read(os.path.join(CURRENT_PATH,'../conf/apikeys.conf'))
# get main DB credentials
db_user = config.get("B3na  DB", "user")
db_pass = config.get("B3na  DB", "password")

# gmail unread count
unread_Count = 0
unread_Count_new = 0

# time of sunset/sunrise - defaults
sunset_time = datetime.datetime.now().replace(hour=19, minute=0)
sunrise_time = datetime.datetime.now().replace(hour=6, minute=30)
bed_time = datetime.datetime.now().replace(hour=23, minute=00)

# set up logging 
logger = logging.getLogger("DaemonLog")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler = logging.FileHandler(os.path.join(CURRENT_PATH,"../log/total.log"))
handler.setFormatter(formatter)
logger.addHandler(handler)


class MyDaemon(Daemon):		
	def run(self):
		while True:
			"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
				Logging Examples:
				logger.debug("Debug message")
				logger.info("Info message")
				logger.warn("Warning message")
				logger.error("Error message")
			"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

			# OK Take a break 
			time.sleep(10)

	def checkGmail(self):
		"""
			Description:
				Checks the unread count in gMail
		"""
		logger.info("Checking email")
			
	def welcomeHome(self,time_away=None):
		"""
			Description:
				Speak a 'welcome home' greeting
		"""
		logger.info("Greeting the creator")
		
	def beSmart(self):
		"""
			Description:
				speak a quip
		"""
		logger.info("time to be a smart ass ?")

	def playTune(self):
		"""
			Description:
				pick a random song from current weather category and play it
		"""
		logger.info("playing a tune")

	def nightlight(self):
		"""
			Description:
				is anyone at home?
				it it after dark? 
				turn the lights on or off as needed. 
		"""	
		logger.info("nightlight auto-check")

def sunriseRoutine():
	"""
		Description:
			sunset routine - perform this routine 30 minutes before sunrise
			giving the users time to go see sunrise
			### TO DO - figure out scheduling
	"""		
	logger.info("Pre-sunrise routine")

def morningRoutine():
	"""
		Description:
			perform morning routine - ring alarm, speak weather, check email, etc..
	"""	
	logger.info("Time for morning routine")

def sunsetRoutine():
	"""
		Description:
			routine to perform at sunset - turn on ambient lights
	"""
	logger.info("Time for sunset routine")

def bedtimeRoutine():
	"""
		Description:
			routine to perform at bedtime - turn on ambient lights
	"""
	logger.info("Bedtime")				

def init_daemon():
	"""
		Description:
			initialize alfr3d services 
	"""
	logger.info("Initializing systems check")
	masterSpeaker.speakString("Initializing systems check")

	faults = 0
	
	return faults

if __name__ == "__main__":
	daemon = MyDaemon('/var/run/b3nadaemon/b3nadaemon.pid',stderr='/dev/null')
	#daemon = MyDaemon('/var/run/b3nadaemon/b3nadaemon.pid',stderr='/dev/stderr')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			logger.info("B3na Daemon initializing")
			faults = init_daemon()
			logger.info("B3na Daemon starting...")
			if faults != 0:
				masterSpeaker.speakString("Some faults were detected but system started successfully")
				masterSpeaker.speakString("Total number of faults is "+str(faults))
			else:
				masterSpeaker.speakString("All systems are up and operational")
			daemon.start()
		elif 'stop' == sys.argv[1]:
			logger.info("B3na Daemon stopping...")			
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)