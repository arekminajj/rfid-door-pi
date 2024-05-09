import rfid
import requests
import time
import os
import RPi.GPIO as GPIO
from RPLCD.gpio import CharLCD

API_KEY = os.environ['API_KEY']
BASE_URL = "https://rfid-door-api-db3514e2b4df.herokuapp.com/"

lcd = CharLCD(pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36],
              numbering_mode=GPIO.BOARD,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True)


#todo add exception onkeyinterupt that clean gpio

def logEntrance(id):
    json = {
        "userId": id,
        "API_KEY": API_KEY
    }

    res = requests.post(BASE_URL+'door/create', json=json, headers={"Content-Type":"application/json"})

    if res.status_code == 200:
        print("entrance has been logged into the system")
        print(res.json())


while(True):
	#lcd.clean()
	id = rfid.read()
	time.sleep(1)

	res = requests.get(BASE_URL + 'user/' + id)
	if res.text == "Not found":
		print(f"user with given id of {id} doesnt exit")
		continue
	user = res.json()
	username = user['name']
	print("logged in as " + username)
	lcd.write_string(username)
	logEntrance(int(id))
	time.sleep(3)
	lcd.clear()

