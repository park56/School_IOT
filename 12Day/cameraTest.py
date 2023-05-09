import picamera
import time
from datetime import datetime 

camera = picamera.PiCamera()
camera.resolution = (1024, 768)

date = datetime.now()
imageDate = date.strftime("%Y_%m_%d_%H_%M_%S")

fileName = "/home/park/study/12Day/gallery/{}.jpg".format(imageDate)

camera.capture(fileName)
