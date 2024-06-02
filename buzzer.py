import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

buzzer = 16

GPIO.setup(buzzer,GPIO.OUT)

def beep():
	start = time.time()
	while True:
		GPIO.output(buzzer,GPIO.HIGH)
		print (time.time()-start)
		time.sleep(0.0005)
		GPIO.output(buzzer,GPIO.LOW)
		time.sleep(0.0005)
		if time.time()-start > 2:
			break
