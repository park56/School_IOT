import time
import Adafruit_DHT
import RPi.GPIO as GPIO
import datetime

green = 16
blue = 20
led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)

sensor = Adafruit_DHT.DHT11
pin = 4

try:
	while True:
		h, t = Adafruit_DHT.read_retry(sensor, pin)
		if(h is not None) and (t is not None) :
			print("Temperature = {0:0.1f}*C Humidity = {1:0.1f}% At {}".format(t, h, datetime.datetime.now()))
			judgeJisu = (1.8*h) - (0.55*(1-(t/100.0))*(1.8*h-26)) + 32
			if judgeJisu <= 69:
				GPIO.output(green, GPIO.HIGH)
				GPIO.output(blue, GPIO.LOW)
				GPIO.output(led, GPIO.LOW)
			elif 75 >= judgeJisu >= 70:
				GPIO.output(blue, GPIO.HIGH)
				GPIO.output(led, GPIO.LOW)
				GPIO.output(green, GPIO.LOW)
			elif judgeJisu >= 76:
				GPIO.output(led, GPIO.HIGH)
				GPIO.output(green, GPIO.LOW)
				GPIO.output(blue, GPIO.LOW)
			else:
				GPIO.output(green, GPIO.LOW)
				GPIO.output(blue, GPIO.LOW)
				GPIO.output(led, GPIO.LOW)
		else:
			print("read error")
		time.sleep(0.3)
		
except KeyboardInterrupt:
	print("Terminated by KeyBoard")
	
finally:
	print("End of Program")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	 
