# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Options(object):
    def setupUi(self, Options):
        Options.setObjectName("Options")
        Options.resize(208, 236)
        self.input_label = QtWidgets.QLabel(Options)
        self.input_label.setGeometry(QtCore.QRect(10, 10, 61, 51))
        self.input_label.setObjectName("input_label")
        self.inputBox = QtWidgets.QComboBox(Options)
        self.inputBox.setGeometry(QtCore.QRect(80, 30, 69, 22))
        self.inputBox.setEditable(True)
        self.inputBox.setObjectName("inputBox")
        self.notificationsBox = QtWidgets.QGroupBox(Options)
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

        self.retranslateUi(Options)
        self.inputBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Options)

    def retranslateUi(self, Options):
        _translate = QtCore.QCoreApplication.translate
        Options.setWindowTitle(_translate("Options", "Dialog"))
        self.input_label.setText(_translate("Options", "Input mode"))
        self.inputBox.setCurrentText(_translate("Options", "USB"))
        self.notificationsBox.setTitle(_translate("Options", "Notifications"))
        self.lineEdit.setText(_translate("Options", "110"))
        self.hr_label.setText(_translate("Options", "Heartrate threshold"))
        self.lineEdit_2.setText(_translate("Options", "95"))
        self.lineEdit_3.setText(_translate("Options", "20"))
        self.o2_label.setText(_translate("Options", "Oxygen threshold"))
        self.cooldown_label.setText(_translate("Options", "Cooldown(seconds)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Options = QtWidgets.QDialog()
    ui = Ui_Options()
    ui.setupUi(Options)
    Options.show()
    sys.exit(app.exec_())
