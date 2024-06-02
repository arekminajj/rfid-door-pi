import RPi.GPIO as GPIO

relayPin = 38

#GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relayPin, GPIO.OUT)

def high():
	GPIO.output(relayPin, GPIO.HIGH)
def low():
	GPIO.output(relayPin, GPIO.LOW)
#GPIO.cleanup()
