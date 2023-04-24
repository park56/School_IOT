#-*-coding:utf-8-*-

import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#센서에 연결한 Trig와 Echo 핀의 번호 설정
TRIG = 16
ECHO = 20
buzzer = 21
print("Distance measurement in progress")

#Trig와 Echo 핀의 출력/입력 설정
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 100)
pwm.start(10)
# fre = [262, 294, 330, 349, 392, 440, 493, 523]
myFre = {10: 262, 20: 294, 30: 330, 40: 349, 50: 392, 60: 440, 70: 493, 80: 523}
speed = 0.5

#Trig핀의 신호를 0으로 출력
GPIO.output(TRIG, False)
print("Waiting for sensor to settle")
time.sleep(2)

flag = 0

try:
	while True:
		# Triger 핀에 펄스신호를 만들기 위해 1 출력
		GPIO.output(TRIG, True)
		time.sleep(0.00001) # 10μs 딜레이
		GPIO.output(TRIG, False)
		
		# start time
		while GPIO.input(ECHO)==0:
			start = time.time()
		while GPIO.input(ECHO)==1:
			stop= time.time() # Echo 핀 하강 시간
			
		check_time = stop - start
		distance = check_time * 34300 / 2
		print("Distance : %.1f cm" % distance)
		
		if distance > 90 or distance < 10:
			pwm.ChangeFrequency(0.1)
		else:
			elsenum = math.floor(distance/10) * 10
			pwm.ChangeFrequency(myFre.get(elsenum))
		time.sleep(0.4) # 0.4초 간격으로 센서 측정
		
except KeyboardInterrrupt:
	print("Measurement stopped by User")
	GPIO.cleanup()
