import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


reader = SimpleMFRC522()

def read():
	id, text = reader.read()
	print("place card on top of the reader module to read id")
	print(f"card id: {id}")
	print(f"written id: {text}")
	#GPIO.cleanup()

	return text

def write(msg):
	try:
        	id = input("id: ")

        	print("Place your RFID card near the reade")
       		reader.write(id)
        	print(f'{id} written to RFID Card')
	finally:
        	GPIO.cleanup()

