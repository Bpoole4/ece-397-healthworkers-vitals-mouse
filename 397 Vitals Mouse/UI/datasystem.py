import datetime
import os
import csv
from zipfile import ZipFile
from os.path import basename



def data_store(heartrate, oxygen):

	date = 'vitals'+str(datetime.datetime.now().date())
	time = str(datetime.datetime.now().time())

	directory = os.getcwd()
	foldername = directory + '\\vitalsmouse_userdata'

	

	if not os.path.exists(foldername):
		os.makedirs(foldername)

	filename = foldername + '\\' + date +'.csv'

	

	with open(filename,'a') as file:
		f_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
		f_writer.writerow([time, str(heartrate), str(oxygen)])

	return()



def data_get(fpath):
	returnTime = [0]
	returnHR = [0]
	returnO2 = [0]


	with open(fpath,'r') as file:
            csv_reader = csv.reader(file, delimiter=',')
            for row in csv_reader:
                time = datetime.datetime.strptime(row[0],'%H:%M:%S.%f')
                today = datetime.datetime.strptime('0:0:0.0','%H:%M:%S.%f')

                times = (time-today).total_seconds()

                returnTime.append(times)
                returnHR.append(int(row[1]))
                returnO2.append(int(row[2]))
	returnTime = returnTime[1:]
	returnHR = returnHR[1:]
	returnO2 = returnO2[1:]

	return(returnTime,returnHR,returnO2)


def data_zip(ziploc):

	directory = os.getcwd()
	foldername = directory + '\\vitalsmouse_userdata'
	filelist = os.listdir(foldername)
	print(filelist)
	files = [0]
	for name in filelist:
		date =  name.replace("vitals","")
		date = 	date.replace(".csv","")
		date = datetime.datetime.strptime(date, "%Y-%m-%d")
		date = date.date()
		a = date.replace(day = 1)

		now = datetime.datetime.now().date()
		b = now.replace(day = 1)

		print(a,b)
		
		if a == b:
			files.append(name)

	if len(files) > 1:
		files = files[1:]
	print(files)
	print(ziploc)
	zfile = ZipFile(ziploc,'w')

	for na in files:
		path = foldername + '\\' + na 
		print(path)
		zfile.write(path, basename(path))

	zfile.close()

def data_analysis():
	directory = os.getcwd()
	foldername = directory + '\\vitalsmouse_userdata'
	filelist = os.listdir(foldername)
	print(filelist)
	files = [0]
	for name in filelist:
		date =  name.replace("vitals","")
		date = 	date.replace(".csv","")
		date = datetime.datetime.strptime(date, "%Y-%m-%d")
		date = date.date()
		a = date.replace(day = 1)

		now = datetime.datetime.now().date()
		b = now.replace(day = 1)

		print(a,b)
		
		if a == b:
			print('a')

			








if __name__ == "__main__":
	#data_store(200,200)
	#date = 'vitals'+str(datetime.datetime.now().date())
	#directory = os.getcwd()
	#foldername = directory + '\\vitalsmouse_userdata'
	#filename = foldername + '\\' + date +'.csv'
	#g = data_get(filename)
	data_zip('zipfile.zip')

