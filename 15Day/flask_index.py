from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, 0)

@app.route('/', methods=['POST', 'GET'])
def flask():
	return render_template('index.html')

@app.route('/data', methods=['POST', 'GET'])
def data():
	if  request.form.get('led') == "on":
		ledon()
	else:
		ledoff()
	
	return render_template('index.html')

def ledon():
	GPIO.output(ledPin, 1)

def ledoff():
	GPIO.output(ledPin, 0)

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = "80")
