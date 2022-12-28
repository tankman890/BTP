import time

import check_id
import predict

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

while True:
	id, text = reader.read()
	#id = input('Scan the card: ')
	if check_id.check_local(id):
		print('Access Granted!')

		model = 'models/custom_' + id
		print('Custom comfortable temperature: ' + str(predict.predict_temp(model)))
	elif check_id.check_remote(id):
		print('Access Granted!')
		
		model = 'models/generic_model'
		print('Generic comfortable temperature: ' + str(predict.predict_temp(model)))
	else:
		print("Access Denied!")
	time.sleep(1)
	
GPIO.cleanup()
