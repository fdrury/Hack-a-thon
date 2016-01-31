import time
import math
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
button0 = 35
button1 = 37
GPIO.setup(button0, GPIO.IN)
GPIO.setup(button1, GPIO.IN)
ledRedData = 16
ledGrnData = 18
ledClock = 36
ledWrite = 32
GPIO.setup(ledRedData, GPIO.OUT)
GPIO.setup(ledGrnData, GPIO.OUT)
GPIO.setup(ledClock, GPIO.OUT)
GPIO.setup(ledWrite, GPIO.OUT)
compassSDA = 3
compassSCL = 5

# temp values for testing
myLat = 5332.7528
myLon = -11329.9295
wayLat = 5288.0623
wayLon = -11807.6087
waySet = False
compass = 0


def readGPS():
	#read GPS beacon
	myLat = 5332.7528
	myLon = -11329.9295


def readCompass():
	#read Magnetometer
	compass = 0


def receiveGPS():
	#receive from xBee
	pass


def sendGPS():
	#send from xBee
	pass


def writeLEDs():
	#write LEDs
	if(compass%45 == math.atan(myLat/myLon)%45 and waySet):
		pass


def setWay():
	#set waypoint
	wayLon = myLon
	wayLat = myLat


def setup():
	#implement if time
	#test LEDs
	pass


def loop():
	readGPS()
	readCompass()
	receiveGPS()
	sendGPS()
	writeLEDs()
	if(GPIO.input(button0)): #fix this
		setWay()


if __name__ == "__main__":
	setup()
	while(not GPIO.input(button1)): #fix this
		loop()
	#shutdown Pi
