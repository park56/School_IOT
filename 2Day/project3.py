#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO			
import time						

led_pin1 = 23
led_pin2 = 24
button = 21

GPIO.setwarnings(False)	

GPIO.setmode(GPIO.BCM)	

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	while GPIO.input(button) == 1:
		GPIO.output(led_pin1, 1)
		GPIO.output(led_pin1, 0)
		time.sleep(0.1)
		GPIO.output(led_pin2, 1)
		GPIO.output(led_pin2, 0)
		time.sleep(0.1)

GPIO.cleanup()
