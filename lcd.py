from RPi import GPIO
from RPLCD.gpio import CharLCD

lcd = CharLCD(pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 36],
              numbering_mode=GPIO.BOARD,
              cols=16, rows=2, dotsize=8,
              charmap='A02',
              auto_linebreaks=True)




def write(msg):
	lcd.write_string(msg)

def clean():
	lcd.clear()
