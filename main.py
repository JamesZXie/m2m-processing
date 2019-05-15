import serial

arduino = serial.Serial(port='/dev/cu.usbmodem143401', baudrate=9600, timeout=.1)
prevaccelX = 0
prevaccelY = 0

while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		dataAsString = data.decode("utf-8").split(',')[1:]
		xaccel = dataAsString[0]
		yaccel = dataAsString[1]
		#...
		xjerk =  (xaccel - prevaccelX)/.005
		#calculate jerk as currentdata - prevline / 5 ms 
		#data - prevLine 
		prevaccelX = xaccel

