import math
import time
import quick2wire.i2c as i2c
import RPi.GPIO as GPIO

LEDclock = 36
LEDout = 32
LEDdataG = 18
LEDdataR = 16

GPIO.setmode(GPIO.BOARD)

GPIO.setup(LEDclock, GPIO.OUT)
GPIO.setup(LEDout, GPIO.OUT)
GPIO.setup(LEDdataG, GPIO.OUT)
GPIO.setup(LEDdataR, GPIO.OUT)

from i2clibraries import i2c_hmc5883l

hmc5883l = i2c_hmc5883l.i2c_hmc5883l(1)

hmc5883l.setContinuousMode()
hmc5883l.setDeclination(0,6)

x = str(hmc5883l)[8:13] #needs fixing, will break for some values
print(x)



GPIO.output(LEDout, False)
GPIO.output(LEDdataG, True)
GPIO.output(LEDdataR, True)
GPIO.output(LEDclock, True)
time.sleep(0.1)
GPIO.output(LEDdataG, False)
GPIO.output(LEDdataR, False)
GPIO.output(LEDclock, False)
GPIO.output(LEDout, True)
time.sleep(0.1)

GPIO.output(LEDout, False)
GPIO.output(LEDdataG, True)
GPIO.output(LEDdataR, True)
GPIO.output(LEDclock, True)
time.sleep(0.1)
GPIO.output(LEDdataG, False)
GPIO.output(LEDdataR, False)
GPIO.output(LEDclock, False)
GPIO.output(LEDout, True)
time.sleep(0.1)

GPIO.output(LEDout, False)
GPIO.output(LEDdataG, True)
GPIO.output(LEDdataR, True)
GPIO.output(LEDclock, True)
time.sleep(0.1)
GPIO.output(LEDdataG, False)
GPIO.output(LEDdataR, False)
GPIO.output(LEDclock, False)
GPIO.output(LEDout, True)
time.sleep(0.1)

GPIO.output(LEDout, False)
GPIO.output(LEDdataG, True)
GPIO.output(LEDdataR, True)
GPIO.output(LEDclock, True)
time.sleep(0.1)
GPIO.output(LEDdataG, False)
GPIO.output(LEDdataR, False)
GPIO.output(LEDclock, False)
GPIO.output(LEDout, True)
time.sleep(0.1)

GPIO.output(LEDout, False)
GPIO.output(LEDclock, True)
time.sleep(0.1)
GPIO.output(LEDclock, False)
GPIO.output(LEDout, True)
time.sleep(0.3)

GPIO.output(LEDout, False)
GPIO.output(LEDclock, True)
time.sleep(0.1)
GPIO.output(LEDclock, False)
GPIO.output(LEDout, True)
time.sleep(0.3)

GPIO.output(LEDout, False)
GPIO.output(LEDclock, True)
time.sleep(0.1)
GPIO.output(LEDclock, False)
GPIO.output(LEDout, True)
time.sleep(0.3)




while 1:
	x = float(str(hmc5883l)[8:13]) #needs fixing, will break for some values
	print(x)
	if(math.fabs(x)/6 <= 100):
		GPIO.output(LEDdataG, True)
		GPIO.output(LEDdataR, True)
	GPIO.output(LEDclock, True)
	time.sleep(0.1)
	GPIO.output(LEDdataG, False)
	GPIO.output(LEDdataR, False)
	GPIO.output(LEDclock, False)
	loopVar = math.fabs(x)/6
	while loopVar > 0:
		GPIO.output(LEDclock, True)
		time.sleep(0.1)
		GPIO.output(LEDclock, False)
		time.sleep(0.1)
		loopVar = loopVar - (100/7)
	GPIO.output(LEDout, True)
	time.sleep(0.1)
	GPIO.output(LEDout, False)
	time.sleep(0.5)
	GPIO.output(LEDclock, True)
	GPIO.output(LEDclock, False)
	GPIO.output(LEDclock, True)
	GPIO.output(LEDclock, False)
	GPIO.output(LEDclock, True)
	GPIO.output(LEDclock, False)
	GPIO.output(LEDclock, True)
	GPIO.output(LEDclock, False)
	GPIO.output(LEDclock, True)
	GPIO.output(LEDclock, False)
	GPIO.output(LEDclock, True)
	GPIO.output(LEDclock, False)
	GPIO.output(LEDclock, True)
	GPIO.output(LEDclock, False)
	GPIO.output(LEDclock, True)
	GPIO.output(LEDclock, False)
