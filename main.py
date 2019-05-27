import serial
import pyaudio
import wave

arduino = serial.Serial(port='/dev/cu.HC-06-DevB', baudrate=9600, timeout=.1)
G_prevaccelX = 0
G_prevaccelY = 0
G_prevaccelZ = 0
xpos = 0
ypos = 0
zpos = 0
xaccel = 0
yaccel = 0
zaccel = 0
xvelocity = 0
yvelocity = 0
zvelocity = 0
xjerk = 0
yjerk = 0
zjerk = 0

delay = .005


def play_sound(track):
	# define stream chunk
	chunk = 1024

	# open a wav format music
	f = wave.open(track, "rb")
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
		arduino_data = arduino.readline()[:-2]
		stream.write(data)
		data = f.readframes(chunk)

	# stop stream
	stream.stop_stream()
	stream.close()

	# close PyAudio
	p.terminate()


while True:
    # the last bit gets rid of the new-line chars
    data = arduino.readline()[:-2]
    if data:

        dataAsString = data.decode("utf-8").split(',')
        # print(dataAsString)
        if (len(dataAsString) == 6):
            G_xaccel = int(dataAsString[0]) * 9.8 / 16000
            G_yaccel = int(dataAsString[1]) * 9.8 / 16000
            G_zaccel = int(dataAsString[2]) * 9.8 / 16000

            if(abs(G_zaccel) > 12):
                play_sound("fist_pump.wav")

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
