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

bright = 0

try:
	while True:
		p.ChangeDutyCycle(bright)
		time.sleep(0.1)
		if(GPIO.input(button) == 1):
			if(bright <= 60):
				bright += 30
			else:
				bright = 0
			
			time.sleep(1)
		
except KeyBoardInterrupt:
	pass
	
p.stop()

GPIO.cleanup()
