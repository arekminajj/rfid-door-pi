import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	id = input("id: ")

	print("Place your RFID card near the reade")
	reader.write(id)
	print(f'{id} written to RFID Card')
finally:
	GPIO.cleanup()
