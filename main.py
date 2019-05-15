import serial

arduino = serial.Serial(port='/dev/cu.usbmodem143401', baudrate=9600, timeout=.1)
prevLine = ""

while True:
	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print(data.decode("utf-8").split(',')[1:])
		#calculate jerk as currentdata - prevline / 5 ms 
		#data - prevLine 
		prevLine = data

