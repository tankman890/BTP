#!/usr/bin/env python

import time

import check_id

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

while True:
	id, text = reader.read()
	if check_id.check(id):
		print("Access Granted!")
	else:
		print("Access Denied!")
	time.sleep(3)
	
GPIO.cleanup()
