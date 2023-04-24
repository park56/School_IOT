#-*-coding:utf-8-*-
import spidev
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# 딜레이 시간(센서 측정 간격)
delay = 0.5

# MCP3008 채널중 센서에 연결한 채널 설정
ldr_channel = 0

# SPI 인스턴스 spi 생성
spi = spidev.SpiDev()

# spi 통신 시작
spi.open(0,0)

# SPI통신 속도 설정
spi.max_speed_hz = 100000

# 0~7까지 8개의 채널에서 SPI 데이터를 읽어서 반환
def readadc(adcnum):
	if adcnum > 7 or adcnum < 0:
		return -1
	r = spi.xfer2([6+((adcnum&0x4)>>2),(adcnum&0x3)<<6,0])
	data = ((r[1] & 15) << 8) + r[2]
	return data
	
while True:
	# readadc 함수로 ldr_channel의 SPI데이터를 읽어 저장
	ldr_value = readadc(ldr_channel)
	print("----------------------------")
	print("LDR Value: %d"% ldr_value)
	
	if(ldr_value < 130):
		GPIO.output(18, GPIO.LOW)
	else:
		GPIO.output(18, GPIO.HIGH)
	time.sleep(delay)
