import RPi.GPIO as GPIO
import time

buzzer = 18
button1 = 17
button2 = 27
button3 = 22
button4 = 23
button5 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False)
pwm = GPIO.PWM(buzzer, 100)
pwm.start(10)

fre = [262, 294, 330, 349, 392, 440, 493, 523]
speed = 0.5

try:
	while 1:
		if (GPIO.input(button1) == GPIO.HIGH):
			print("1")
			pwm.ChangeFrequency(fre[0])
			time.sleep(speed)
			
		elif (GPIO.input(button2) == GPIO.HIGH):
			print("2")
			pwm.ChangeFrequency(fre[2])
			time.sleep(speed)
			
		elif (GPIO.input(button3) == GPIO.HIGH):
			print("3")
			pwm.ChangeFrequency(fre[4])
			time.sleep(speed)
			
			
		elif (GPIO.input(button4) == GPIO.HIGH):
			print("4")
			pwm.ChangeFrequency(fre[6])
			time.sleep(speed)
			
		elif (GPIO.input(button5) == GPIO.HIGH):

			print("5")
			pwm.ChangeFrequency(fre[7])
			time.sleep(speed)
			
		else:
			print("0")
			pwm.ChangeFrequency(0.1)
			
except KeyboardInterrupt:
	pass
p.stop()
GPIO.cleanup();
