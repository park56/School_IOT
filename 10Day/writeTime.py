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
			print(" Temperatyre: "+str(h) + "*C Humidity: " + str(t) + "% Attime: "+str(datetime.datetime.now()))
			f = open('temphumi.txt', 'a')
			f.write("Temperatyre: "+str(h) + "*C Humidity: " + str(t) + "% Attime: "+str(datetime.datetime.now()) + "\n")
			f.close()
		else:
			print("read error")
		time.sleep(0.3)
		
except KeyboardInterrupt:
	print("Terminated by KeyBoard")
	
finally:
	print("End of Program")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	 
