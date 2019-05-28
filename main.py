import serial
import pyaudio
import wave
import time

arduino = serial.Serial(port='/dev/cu.HC-06-DevB', baudrate=9600, timeout=.1)

#global variables
G_prevaccelX = 0
G_prevaccelY = 0
G_prevaccelZ = 0

delay = .005

def play_sound(track):
	# define stream chunk
	chunk = 1024

	# open a wav format music
	f = wave.open("./sounds/"+track, "rb")
	# instantiate PyAudio
	p = pyaudio.PyAudio()
	# open stream
	stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
					channels=f.getnchannels(),
					rate=f.getframerate(),
					output=True)
	# read data
	data = f.readframes(chunk)

	# play stream
	while data:
		stream.write(data)
		data = f.readframes(chunk)

	# stop stream
	stream.stop_stream()
	stream.close()

	# close PyAudio
	p.terminate()

def tada_eval(tf1, tf3, tf5):
	#12k for y accel, 32k for x rotation
	condition1 = False
	condition2 = False

	for val1, val2 in zip(tf1, tf3):
		if val1 > 12000:
			condition1 = True
		if val2 > 30000:
			condition2 = True
		if condition1 and condition2:
			tf1 = []
			tf3 = []
			tf5 = []
			play_sound("tada.wav")
			return True	
	return False	

def read_start():
	print("starting M2M processor...")
	tf0 = []
	tf1 = []
	tf2 = []
	tf3 = []
	tf4 = []
	tf5 = []

	while True:
		new_line = arduino.readline()[:-2]
		if new_line:
			try: 
				data = [int(i) for i in new_line.decode("utf-8").split(',')]
			except:
				continue
			
			if len(data) == 6:	
				tf0.append(data[0])
				tf1.append(data[1])
				tf2.append(data[2])
				tf3.append(data[3])
				tf4.append(data[4])
				tf5.append(data[5])
				if len(tf0) < 100:
					continue
				tf0 = tf0[1:]
				tf1 = tf1[1:]
				tf2 = tf2[1:]
				tf3 = tf3[1:]
				tf4 = tf4[1:]
				tf5 = tf5[1:]
				if tada_eval(tf1, tf3, tf5):
					print("TADA")
					tf0 = []
					tf1 = []
					tf2 = []
					tf3 = []
					tf4 = []
					tf5 = []
					time.sleep(1)

			# if len(data)==6:
			# 	data = [int(i) for i in data]
			# 	print(data)


		
		
if __name__ == '__main__':
    read_start()

            # ...
            # xjerk_new =  (G_xaccel - G_prevaccelX)/delay
            # yjerk_new =  (G_yaccel - G_prevaccelY)/delay
            # zjerk_new =  (G_zaccel - G_prevaccelZ)/delay
            # #calculate jerk as currentdata - prevline / 5 ms
            # #data - prevLine

            # xaccel_new = (xjerk_new + xjerk)/2 * delay
            # yaccel_new = (yjerk_new + yjerk)/2 * delay
            # zaccel_new = (zjerk_new + zjerk)/2 * delay
            # xjerk = xjerk_new
            # yjerk = yjerk_new
            # zjerk = zjerk_new

            # xvelocity_new = (xaccel_new + xaccel)/2 * delay
            # yvelocity_new = (yaccel_new + yaccel)/2 * delay
            # zvelocity_new = (zaccel_new + zaccel)/2 * delay
            # xaccel = xaccel_new
            # yaccel = yaccel_new
            # zaccel = zaccel_new

            # xpos = (xvelocity_new + xvelocity)/2 * delay
            # ypos = (yvelocity_new + yvelocity)/2 * delay
            # zpos = (zvelocity_new + zvelocity)/2 * delay
            # xvelocity = xvelocity_new
            # yvelocity = yvelocity_new
            # zvelocity = zvelocity_new
