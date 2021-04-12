#Here are a few functions pertaining to managing data. It includes file read and writing functions, as well as zipping and analysis

import datetime
import os
import csv
from zipfile import ZipFile
from os.path import basename
import statistics



def data_store(heartrate, oxygen):
	#stores HR and O2 in today's file

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
	#opens a given file name and returns the values stored
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
	#takes a file path and creates a file zips the last month's files into it
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
	#generates various statistics on data
	directory = os.getcwd()
	foldername = directory + '\\vitalsmouse_userdata'
	filelist = os.listdir(foldername)
	files = [0]

	gatsuhr = [0]
	gatsuo2 = [0]
	toshihr = [0]
	toshio2 = [0]
	print(gatsuhr)
	for name in filelist:
		date =  name.replace("vitals","")
		date = 	date.replace(".csv","")
		date = datetime.datetime.strptime(date, "%Y-%m-%d")
		date = date.date()

		now = datetime.datetime.now().date()
		


		a = date.replace(day = 1)
		b = now.replace(day = 1)

		c = a.replace(month = 1)
		d = b.replace(month = 1)
		
		if a == b:
			tempdata1 = data_get(foldername + "\\" + name)
			hr1 = statistics.mean(tempdata1[1])
			o21 = statistics.mean(tempdata1[2])

			gatsuhr.append(hr1)
			gatsuo2.append(o21)

		

		if date == now:
			tempdata2 = data_get(foldername + "\\" + name)
			hr2 = statistics.mean(tempdata2[1])
			o22 = statistics.mean(tempdata2[2])
			kyou = (hr2,o22)

		if c == d:
			tempdata3 = data_get(foldername + "\\" + name)
			hr3 = statistics.mean(tempdata3[1])
			o23 = statistics.mean(tempdata3[2])
			toshihr.append(hr3)
			toshio2.append(o23)
		
	gatsuhr = gatsuhr[1:]
	gatsuo2 = gatsuo2[1:]
	toshihr = toshihr[1:]
	toshio2 = toshio2[1:]

	gatsu = (statistics.mean(gatsuhr),statistics.mean(gatsuo2))
	toshi = (statistics.mean(toshihr),statistics.mean(toshio2))

	gatsulist = (gatsuhr,gatsuo2)

	return(kyou, gatsu, toshi, gatsulist) 


			








if __name__ == "__main__":
	import time
	start_time = time.time()
	#date = 'vitals'+str(datetime.datetime.now().date())
	#directory = os.getcwd()
	#foldername = directory + '\\vitalsmouse_userdata'
	#filename = foldername + '\\' + date +'.csv'
	#g = data_get(filename)
	#data_zip('zipfile.zip')
	x = data_analysis()
	#print(x)
	print(x[3][1])
	print("--- %s seconds ---" % (time.time() - start_time))

	number = len(x[3][1])
	y = [str(z) for z in range(number + 1)]
	print(y)



	
	
	
	

