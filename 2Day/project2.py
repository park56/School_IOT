#-*- coding:utf-8 -*-
import RPi.GPIO as GPIO			

import time						

led_pin1 = 2
led_pin2 = 3
led_pin3 = 4
led_pin4 = 20
led_pin5 = 21

wait_time1 = 3

GPIO.setwarnings(False)	

GPIO.setmode(GPIO.BCM)	

GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(led_pin3, GPIO.OUT)
GPIO.setup(led_pin4, GPIO.OUT)
GPIO.setup(led_pin5, GPIO.OUT)

while(True):
	GPIO.output(led_pin1, 0)
	GPIO.output(led_pin5, 0)
	GPIO.output(led_pin3, 1)
	GPIO.output(led_pin4, 1)
	time.sleep(wait_time1)
	
	GPIO.output(led_pin3, 0)
	GPIO.output(led_pin4, 0)
	GPIO.output(led_pin2, 1)
	
	time.sleep(wait_time1)
	GPIO.output(led_pin2, 0)
	GPIO.output(led_pin1, 1)
	GPIO.output(led_pin5, 1)
	
	time.sleep(wait_time1)
	
GPIO.cleanup()
