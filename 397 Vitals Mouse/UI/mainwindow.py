# The main window of the UI. Where the majority of things happen. Original file was created using pyuic5 and QTdesigner. From there, it has been heavily edited to get to the point it is at now

#To run this file you need to install python 3 or higher, and the following libraries: pyqt5, pyqtgraph, pyserial, winrt


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QDateEdit, QDialog
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from random import randint
from data_generator import singleGenerate
import csv 
import serial_connection
import winrt.windows.ui.notifications as notifications
import winrt.windows.data.xml.dom as dom
import windowsalert
import datetime
import datasystem
import os

class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 618)
    
        MainWindow.setStyleSheet('background:#e8e8e8')


        #here starts widget setup, mostly just assigning locations and various properties
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.topDisplayDivider = QtWidgets.QFrame(self.centralwidget)
        self.topDisplayDivider.setGeometry(QtCore.QRect(0, 90, 801, 16))
        self.topDisplayDivider.setFrameShape(QtWidgets.QFrame.HLine)
        self.topDisplayDivider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topDisplayDivider.setObjectName("topDisplayDivider")
        self.menuDivider = QtWidgets.QFrame(self.centralwidget)
        self.menuDivider.setGeometry(QtCore.QRect(110, 100, 16, 501))
        self.menuDivider.setFrameShape(QtWidgets.QFrame.VLine)
        self.menuDivider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.menuDivider.setObjectName("menuDivider")
        self.pushHistory = QtWidgets.QPushButton(self.centralwidget)
        self.pushHistory.setGeometry(QtCore.QRect(20, 140, 75, 23))
        self.pushHistory.setObjectName("pushHistory")
        self.pushHistory.setStyleSheet("border: 1px solid grey;")
        self.pushAnalytics = QtWidgets.QPushButton(self.centralwidget)
        self.pushAnalytics.setGeometry(QtCore.QRect(20, 210, 75, 23))
        self.pushAnalytics.setObjectName("pushAnalytics")
        self.pushExport = QtWidgets.QPushButton(self.centralwidget)
        self.pushExport.setGeometry(QtCore.QRect(20, 280, 75, 23))
        self.pushExport.setObjectName("pushExport")
        self.pushOptions = QtWidgets.QPushButton(self.centralwidget)
        self.pushOptions.setGeometry(QtCore.QRect(20, 350, 75, 23))
        self.pushOptions.setObjectName("pushOptions")

        self.pushLive = QtWidgets.QPushButton(self.centralwidget)
        self.pushLive.setGeometry(QtCore.QRect(20, 550, 75, 23))
        self.pushLive.setObjectName("pushLive")

        self.pushGraph = QtWidgets.QPushButton(self.centralwidget)
        self.pushGraph.setGeometry(QtCore.QRect(200, 550, 75, 23))
        self.pushGraph.setObjectName("pushGraph")

        self.pushGraph2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushGraph2.setGeometry(QtCore.QRect(300, 550, 75, 23))
        self.pushGraph2.setObjectName("pushGraph2")

        self.liveDisplay_1 = QtWidgets.QLabel(self.centralwidget)
        self.liveDisplay_1.setGeometry(QtCore.QRect(710, 20, 61, 61))
        self.liveDisplay_1.setObjectName("liveDisplay_1")
        self.liveDisplay_1.setStyleSheet("font: 30pt Arial MS")

        self.liveDisplay_2 = QtWidgets.QLabel(self.centralwidget)
        self.liveDisplay_2.setGeometry(QtCore.QRect(570, 20, 61, 61))
        self.liveDisplay_2.setObjectName("liveDisplay_2")
        self.liveDisplay_2.setStyleSheet("font: 30pt Arial MS")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 20, 61, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("heart.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 20, 61, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("o2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(140, 120, 631, 311))
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(210, 110, 151, 31))
        self.label_3.setObjectName("label_3")

        self.dateTimeEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(190, 490, 194, 22))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setDate(QDate.currentDate())

        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #creating graphs
        self.graphWidgetLive = PlotWidget(self.centralwidget)
        self.graphWidgetLive.setGeometry(QtCore.QRect(40, 10, 400, 70))
        self.graphWidgetLive.setObjectName("graphWidgetLive")
        self.graphWidgetLive.getPlotItem().hideAxis('bottom')
        self.graphWidgetLive.setMouseEnabled(x=False, y=False)
        self.graphWidgetLive.setYRange(0, 150, padding=0.2)
        self.graphWidgetLive.getPlotItem().hideAxis('bottom')


        self.graphWidgetMain = PlotWidget(self.centralwidget)
        self.graphWidgetMain.setGeometry(QtCore.QRect(150, 140, 600, 275))
        self.graphWidgetMain.setObjectName("graphWidgetLive")
        self.graphWidgetMain.setMouseEnabled(x=True, y=False)
        self.graphWidgetMain.setYRange(50, 150, padding=0)
        self.graphWidgetMain.getPlotItem().hideAxis('bottom')

        

        self.graphWidgetLive.setBackground('w')


        pen = pg.mkPen(color = (255, 0 ,0), width = 2)
        pen2 = pg.mkPen(color = (0, 0 ,255), width = 2)
        time = [1,2,3,4]
        heartRate = [90,87,88,85]
        oxygenLevel = [100,99,99,98]
        self.graphWidgetMain.setBackground('w')
        self.graphWidgetMain.plot(time, heartRate, pen=pen)
        self.graphWidgetMain.plot(time, oxygenLevel, pen=pen2)

        #these two values can be changed in options and are parameters for the windows notifications
        self.notifThresh = [120,95]
        self.notifCooldown = 25

        self.serialInput = False 

        
        


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #connecting buttons
        self.pushAnalytics.clicked.connect(self.show_Analysis)


        self.pushExport.clicked.connect(self.show_export)

        self.pushOptions.clicked.connect(self.show_popOptions)


        self.pushLive.setCheckable(True)
        self.pushLive.clicked.connect(self.show_graphLive)

        self.pushGraph.clicked.connect(self.fromFile)
        self.pushGraph2.clicked.connect(self.fromDate)



    def update_plot_data(self):

        #this is used to update the live graph by reading from serial or the debugging simulator

        self.timeLive = self.timeLive[1:]  # Remove the first y element.
        self.timeLive.append(self.timeLive[-1] + 1)  # Add a new value 1 higher than the last.

        if  self.serialInput == True:
            serialData = serial_connection.getSerial()
        else:
            serialData = (singleGenerate(79,3), singleGenerate(97,1))
        

         
        if serialData[0] != 0:
            self.liveHR = self.liveHR[1:] # Remove the first
            self.liveHR.append(serialData[0])
            self.liveDisplay_2.setText(str(self.liveHR[99]))


        if serialData[1] != 0:
            self.liveO2 = self.liveO2[1:] # Remove the first 
            self.liveO2.append(serialData[1])
            self.liveDisplay_1.setText(str(self.liveO2[99]))

        if not (serialData[0] == 0 & serialData[1] == 0):
            datasystem.data_store(serialData[0], serialData[1])

        a = datetime.datetime.now()
        b = self.startTime
        c = a - b
        print(c.total_seconds())
        if c.total_seconds() > self.notifCooldown:
            if self.notifThresh[0] < serialData[0]:
                windowsalert.sendNotifH()
                self.startTime = datetime.datetime.now()

            if self.notifThresh[1] > serialData[1] & serialData[1] != 0:
                windowsalert.sendNotifO()
                self.startTime = datetime.datetime.now()
            


        
        self.data_line_1.setData(self.timeLive, self.liveHR)  # Update the data.
        self.data_line_2.setData(self.timeLive, self.liveO2)  # Update the data.

        
        

    def show_export(self):
        #used to call the zipping function in datasystem.py, and the file dialog 
        options = QFileDialog.Options() | QFileDialog.DontUseNativeDialog
        fileName = QFileDialog.getSaveFileName(self,"Select an export location", "","Zip Files (*.zip)", options=options)
        datasystem.data_zip(fileName[0]+'.zip')

    def show_graphLive(self):
        #connects to the button for live, and also controls if the graph/reading is enabled

        self.timeLive = list(range(100))  # 100 time points
        self.liveHR = [0]*100
        self.liveO2 = [0]*100
        self.startTime =  datetime.datetime.now() - datetime.timedelta(seconds=self.notifCooldown)
        print(self.startTime)

        pen = pg.mkPen(color = (255, 0 ,0), width = 2)
        pen2 = pg.mkPen(color = (0, 0 ,255), width = 2)

        self.liveDisplay_2.setText('0')
        self.liveDisplay_1.setText('0')


        if self.pushLive.isChecked():
            self.data_line_1 = self.graphWidgetLive.plot(self.timeLive, self.liveHR,pen = pen)
            self.data_line_2 = self.graphWidgetLive.plot(self.timeLive, self.liveO2,pen = pen2)
            self.timer = QtCore.QTimer()
            self.timer.setInterval(250)
            self.timer.timeout.connect(self.update_plot_data)
            self.timer.start()
            self.pushLive.setText('Stop')
        else:
            self.timer.stop()
            self.graphWidgetLive.clear()
            self.pushLive.setText('Start')


    def fromDate(self):
        #used to connect the date picker to the main graph
        x = self.dateTimeEdit.date().toPyDate()
        date = 'vitals'+ str(x)
        directory = os.getcwd()
        foldername = directory + '\\vitalsmouse_userdata'
        self.importfile = foldername + '\\' + date +'.csv'

        self.show_graphMain()

    def fromFile(self):
        #used to connect the file dialog to the main graph
        options = QFileDialog.Options() | QFileDialog.DontUseNativeDialog
        fileName = QFileDialog.getOpenFileName(self,"Select a file to view", "","CSV Files (*.csv)", options=options)
        self.importfile = fileName[0]
        
        self.show_graphMain()

    def show_graphMain(self):
        #loads the data from a file and displays it on the main graph
        
        print(self.importfile)
        
        self.graphWidgetMain.clear()
        
        maindata = datasystem.data_get(self.importfile)

        mainTime = maindata[0]
        mainHR = maindata[1]
        mainO2 = maindata[2]

        pen = pg.mkPen(color = (255, 0 ,0), width = 2)
        pen2 = pg.mkPen(color = (0, 0 , 255), width = 2)
        self.graphWidgetMain.setBackground('w')
        self.graphWidgetMain.plot(mainTime, mainHR, pen=pen)
        self.graphWidgetMain.plot(mainTime, mainO2, pen=pen2)


    
    def show_popOptions(self):
        #secondary window for options
        self.Options = QDialog()
        self.Options.resize(200,250)
        
        self.input_label = QtWidgets.QLabel(self.Options)
        self.input_label.setGeometry(QtCore.QRect(10, 10, 61, 51))
        self.input_label.setObjectName("input_label")

        self.inputBox = QtWidgets.QComboBox(self.Options)
        self.inputBox.setGeometry(QtCore.QRect(80, 30, 69, 22))
        self.inputBox.setObjectName("inputBox")
        self.inputBox.addItem('Debug')
        self.inputBox.addItem('USB')

        self.notificationsBox = QtWidgets.QGroupBox(self.Options)
        self.notificationsBox.setGeometry(QtCore.QRect(0, 90, 211, 131))
        self.notificationsBox.setObjectName("notificationsBox")
        self.lineEdit = QtWidgets.QLineEdit(self.notificationsBox)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 61, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.hr_label = QtWidgets.QLabel(self.notificationsBox)
        self.hr_label.setGeometry(QtCore.QRect(6, 30, 111, 20))
        self.hr_label.setObjectName("hr_label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.notificationsBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 60, 61, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.notificationsBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 90, 61, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.o2_label = QtWidgets.QLabel(self.notificationsBox)
        self.o2_label.setGeometry(QtCore.QRect(10, 60, 111, 20))
        self.o2_label.setObjectName("o2_label")
        self.cooldown_label = QtWidgets.QLabel(self.notificationsBox)
        self.cooldown_label.setGeometry(QtCore.QRect(10, 90, 111, 20))
        self.cooldown_label.setObjectName("cooldown_label")

        self.input_label.setText("Input mode")
        self.notificationsBox.setTitle(("Notifications"))
        self.lineEdit.setText(("110"))
        self.hr_label.setText(("Heartrate threshold"))
        self.lineEdit_2.setText(("95"))
        self.lineEdit_3.setText(("20"))
        self.o2_label.setText(("Oxygen threshold"))
        self.cooldown_label.setText(("Cooldown(seconds)"))

        self.Options.setWindowTitle("Options")
        self.Options.exec_()

        h = self.inputBox.currentText()
        
        if h == 'USB':
            self.serialInput = True
        else:
            self.serialInput = False


        heartThresh = self.lineEdit.text()
        o2Thresh = self.lineEdit_2.text()
        cool = self.lineEdit_3.text()

        self.notifThresh = (int(heartThresh),int(o2Thresh))
        self.notifCooldown = int(cool)

    def show_Analysis(self):
        #secondary window for analysis
        self.Analysis = QDialog()
        self.Analysis.resize(400,400)
       
        self.dailyLine = QtWidgets.QLineEdit(self.Analysis)
        self.dailyLine.setGeometry(QtCore.QRect(210, 60, 113, 20))
        self.dailyLine.setReadOnly(True)
        self.dailyLine.setObjectName("dailyLine")
        self.yearly_label = QtWidgets.QLabel(self.Analysis)
        self.yearly_label.setGeometry(QtCore.QRect(40, 140, 101, 16))
        self.yearly_label.setObjectName("yearly_label")
        self.monthly_label = QtWidgets.QLabel(self.Analysis)
        self.monthly_label.setGeometry(QtCore.QRect(40, 100, 111, 16))
        self.monthly_label.setObjectName("monthly_label")
        self.monthlyLine = QtWidgets.QLineEdit(self.Analysis)
        self.monthlyLine.setGeometry(QtCore.QRect(210, 100, 113, 20))
        self.monthlyLine.setReadOnly(True)
        self.monthlyLine.setObjectName("monthlyLine")
        self.daily_label = QtWidgets.QLabel(self.Analysis)
        self.daily_label.setGeometry(QtCore.QRect(40, 60, 111, 16))
        self.daily_label.setObjectName("daily_label")
        self.yearlyLine = QtWidgets.QLineEdit(self.Analysis)
        self.yearlyLine.setGeometry(QtCore.QRect(210, 140, 113, 20))
        self.yearlyLine.setReadOnly(True)
        self.yearlyLine.setObjectName("yearlyLine")

        self.legend_label = QtWidgets.QLabel(self.Analysis)
        self.legend_label.setGeometry(QtCore.QRect(220, 20, 113, 20))
        self.legend_label.setObjectName("legend_label")
        self.legend_label.setText("Heartrate, Oxygen")
    

        self.graphWidgetAnalysis = PlotWidget(self.Analysis)
        self.graphWidgetAnalysis.setGeometry(QtCore.QRect(50, 200, 300, 150))
        self.graphWidgetAnalysis.setObjectName("graphWidgetLive")
        self.graphWidgetAnalysis.setMouseEnabled(x=False, y=False)
        self.graphWidgetAnalysis.setYRange(50, 150, padding=0)
        self.graphWidgetAnalysis.getPlotItem().hideAxis('bottom')


        analysis_data = datasystem.data_analysis()

        pen = pg.mkPen(color = (255, 0 ,0), width = 2)
        pen2 = pg.mkPen(color = (0, 0 ,255), width = 2)
        
        heartRate = analysis_data[3][0]
        oxygenLevel = analysis_data[3][1]

        length = len(heartRate)
        time = [int(z) for z in range(length)]
        self.graphWidgetAnalysis.setBackground('w')
        self.graphWidgetAnalysis.plot(time, heartRate, pen=pen)
        self.graphWidgetAnalysis.plot(time, oxygenLevel, pen=pen2)

        self.dailyLine.setText(str(round(analysis_data[0][0], 2)) + ', ' + str(round(analysis_data[0][1],2)))
        self.monthlyLine.setText(str(round(analysis_data[1][0], 2)) + ', ' + str(round(analysis_data[1][1],2)))
        self.yearlyLine.setText(str(round(analysis_data[2][0], 2)) + ', ' + str(round(analysis_data[2][1],2)))


        self.yearly_label.setText("Yearly Average")
        self.monthly_label.setText("Monthly Average")
        self.daily_label.setText("Daily Average")
        
        self.Analysis.setWindowTitle("Analysis")
    
        self.Analysis.exec_()


        

       


    def retranslateUi(self, MainWindow):
        #this is a holdover from using pyuic5, not normally used like this
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushHistory.setText(_translate("MainWindow", "History"))
        self.pushAnalytics.setText(_translate("MainWindow", "Analytics"))
        self.pushExport.setText(_translate("MainWindow", "Export"))
        self.pushOptions.setText(_translate("MainWindow", "Options"))
        self.pushLive.setText(_translate("MainWindow","Start"))
        self.pushGraph.setText(_translate("MainWindow","From file"))
        self.pushGraph2.setText(_translate("MainWindow","From date"))
        self.liveDisplay_1.setText("##")
        self.liveDisplay_2.setText("##")
        self.groupBox.setTitle(_translate("MainWindow", "History"))


        

#unused class
class Second(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Options')
        self.setFixedSize(400,350)
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
