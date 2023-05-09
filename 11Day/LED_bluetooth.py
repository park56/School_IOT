import serial
import time
import RPi.GPIO as GPIO

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)
green = 16
blue = 20
led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

GPIO.setwarnings(False) 

try:
	while True:
		data = bleSerial.readline()
		realData = data.decode().strip()
		
		if realData == "":
			continue
			 
		print(realData)
		
		if realData == "green_on":
			GPIO.output(green, GPIO.HIGH)
		elif realData == "green_off":
			GPIO.output(green, GPIO.LOW)
		elif realData == "led_on":
			GPIO.output(led, GPIO.HIGH)
		elif realData == "led_off":
			GPIO.output(led, GPIO.LOW)
		elif realData == "blue_on":
			GPIO.output(blue, GPIO.HIGH)
		elif realData == "blue_off":
			GPIO.output(blue, GPIO.LOW)
			
except KeyboardInterrupt:
	pass
	
bleSerial.close()
