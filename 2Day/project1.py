#-*- coding:utf-8 -*-

# 라즈베리파이 GPIO 핀들 제어 모듈
import RPi.GPIO as GPIO			
# 시간 관련 모듈
import time						

# GPIO 핀 넘버
led_pin1 = 16
led_pin2 = 20
led_pin3 = 21

# 물리적인 핀 번호 (GND, VCC, 프로그래밍 핀 등 모두 포함)
# GPIO.setmode(GPIO.BOARD)

# 불필요한 warning 제거
GPIO.setwarnings(False)	
		
# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)	
	
# LED 핀의 In/Out 설정
GPIO.setup(led_pin1, GPIO.OUT)
GPIO.setup(led_pin2, GPIO.OUT)
GPIO.setup(led_pin3, GPIO.OUT)

while(True):
	# LED ON
	GPIO.output(led_pin1, 1)
	GPIO.output(led_pin2, 1)
	GPIO.output(led_pin3, 1)
	
	# 0.1초 sleep
	time.sleep(0.1)
	
	# LED OFF
	GPIO.output(led_pin1, 0)
	GPIO.output(led_pin2, 0)
	GPIO.output(led_pin3, 0)
	
	time.sleep(0.1)

# GPIO 설정 초기화
GPIO.cleanup()
	



