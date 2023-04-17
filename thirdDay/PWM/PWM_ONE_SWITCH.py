#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# PWM인스턴스 p를 만들고 GPIO 18번을 PWM 핀으로 설정, 주파수 = 50Hz
p = GPIO.PWM(18, 50)
# PWM시작, 듀티비 = 0
p.start(0)

led = 18
button = 21

flag = 0

try:
	while True:	
		print("flag = ", flag)
		
		if(GPIO.input(button) == 1):
			if(flag == 0): 
				flag = 1
				time.sleep(0.1)
			elif(flag == 1): 
				flag = 0
				time.sleep(0.1)
			
		if(flag == 1):
			for dc in range(0, 100, 5):
				p.ChangeDutyCycle(dc)
				time.sleep(0.1)
				
				if(GPIO.input(button) == 1):
					flag = 0
						
			for dc in range(100, -1, -5):
				p.ChangeDutyCycle(dc)
				time.sleep(0.1)
				
				if(GPIO.input(button) == 1):
					flag = 0
				
			time.sleep(1)
except KeyBoardInterrupt:
	pass
	
p.stop()

GPIO.cleanup()
