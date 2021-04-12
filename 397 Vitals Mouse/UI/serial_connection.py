#this file is used for connecting with the serial port and reading from it
#by default the lines to do this are commented out because it will cause errors if the device is not set up on your computer
import serial
import time


#ser = serial.Serial('COM7', '115200')

def getSerial():
	serialHR = 0
	serialO2 = 0	
#	b = ser.readline()	
#	string_n = b.decode()
#	string = string_n.rstrip()
	string = '0,0,0,0'

	for entry in string:
		data = string.split(",")
	data = list(map(int, data))
	if data[2] < 95:
		return(0,0)
	else:
		serialHR = data[0]
		serialO2 = data[1]
	
	return (serialHR, serialO2)



if __name__ == "__main__":
	i = 0
	while i<100:
		i += 1
		h = getSerial()
		print(h)
		time.sleep(.1)


