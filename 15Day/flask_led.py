from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, 0)

@app.route('/')
def flask():
	return "hello world"

@app.route('/ledon')
def ledon():
	GPIO.output(ledPin, 1)
	return "<h1> LED ON </h1> "
	
@app.route('/ledoff')
def ledoff():
	GPIO.output(ledPin, 0)
	return "<h1> LED OFF <h1> "

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "80")
