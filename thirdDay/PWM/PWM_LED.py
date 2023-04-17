#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

led = 18

GPIO.setup(18, GPIO.OUT)

# PWM인스턴스 p를 만들고 GPIO 18번을 PWM 핀으로 설정, 주파수 = 50Hz
p = GPIO.PWM(18, 50)

# PWM시작, 듀티비 = 0
p.start(0)


try:
	while True:
		for dc in range(0, 101, 5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)
		for dc in range(100, -1, -5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.1)
			
except KeyBoardInterrupt:
	pass
	
p.stop()

GPIO.cleanup()
