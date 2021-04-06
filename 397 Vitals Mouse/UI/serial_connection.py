import serial


#ser = serial.Serial('COM7', '115200')

def getSerial():
	string = 'H10'
	serialHR = 0
	serialO2 = 0
	print(string[0])
#	b = ser.readline()
#	string_n = b.decode()
#	string = string_n.rstrip()
	if string[0] == 'H':
	
		serialHR = int(string[1:])
		
	elif string[0] == 'O':
		serialO2 = int(string[1:])

	return (serialHR, serialO2)



if __name__ == "__main__":
	h = getSerial()
	print(h)

