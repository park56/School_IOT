import serial
import time

bleSerial = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1.0)

# 블루투스 모듈 : 8C E3
try:
	while True:
		sendData="3308\n"
		bleSerial.write(sendData.encode())
		time.sleep(1.0)

except KeyboardInterrupt:
	pass
	
bleSerial.close()
