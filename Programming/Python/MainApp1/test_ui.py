# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Testing.ui'
#
# Created: Tue Nov 10 15:03:05 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.closeButton = QtGui.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(650, 490, 75, 23))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.testportsButton = QtGui.QPushButton(self.centralwidget)
        self.testportsButton.setGeometry(QtCore.QRect(40, 40, 75, 23))
        self.testportsButton.setObjectName(_fromUtf8("testportsButton"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(490, 390, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.SerialList = QtGui.QComboBox(self.centralwidget)
        self.SerialList.setGeometry(QtCore.QRect(140, 40, 69, 22))
        self.SerialList.setEditable(True)
        self.SerialList.setMaxVisibleItems(20)
        self.SerialList.setObjectName(_fromUtf8("SerialList"))
        self.SerialList.addItem(_fromUtf8(""))
        self.SerialList.addItem(_fromUtf8(""))
        self.testComms = QtGui.QPushButton(self.centralwidget)
        self.testComms.setGeometry(QtCore.QRect(40, 70, 75, 23))
        self.testComms.setObjectName(_fromUtf8("testComms"))
        self.CommsList = QtGui.QComboBox(self.centralwidget)
        self.CommsList.setGeometry(QtCore.QRect(140, 70, 69, 22))
        self.CommsList.setEditable(True)
        self.CommsList.setDuplicatesEnabled(True)
        self.CommsList.setObjectName(_fromUtf8("CommsList"))
        self.CommsList.addItem(_fromUtf8(""))
        self.CommsList.addItem(_fromUtf8(""))
        self.CommsResult = QtGui.QLabel(self.centralwidget)
        self.CommsResult.setGeometry(QtCore.QRect(40, 100, 171, 16))
        self.CommsResult.setText(_fromUtf8(""))
        self.CommsResult.setObjectName(_fromUtf8("CommsResult"))
        self.VTestResult = QtGui.QLabel(self.centralwidget)
        self.VTestResult.setGeometry(QtCore.QRect(40, 120, 46, 51))
        self.VTestResult.setText(_fromUtf8(""))
        self.VTestResult.setObjectName(_fromUtf8("VTestResult"))
        self.Launch0 = QtGui.QPushButton(self.centralwidget)
        self.Launch0.setGeometry(QtCore.QRect(650, 40, 75, 23))
        self.Launch0.setObjectName(_fromUtf8("Launch0"))
        self.BSel1a = QtGui.QComboBox(self.centralwidget)
        self.BSel1a.setGeometry(QtCore.QRect(400, 70, 69, 22))
        self.BSel1a.setDuplicatesEnabled(True)
        self.BSel1a.setObjectName(_fromUtf8("BSel1a"))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel1a.addItem(_fromUtf8(""))
        self.BSel2a = QtGui.QComboBox(self.centralwidget)
        self.BSel2a.setGeometry(QtCore.QRect(480, 70, 69, 22))
        self.BSel2a.setDuplicatesEnabled(True)
        self.BSel2a.setObjectName(_fromUtf8("BSel2a"))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel2a.addItem(_fromUtf8(""))
        self.BSel3a = QtGui.QComboBox(self.centralwidget)
        self.BSel3a.setGeometry(QtCore.QRect(560, 70, 69, 22))
        self.BSel3a.setDuplicatesEnabled(True)
        self.BSel3a.setObjectName(_fromUtf8("BSel3a"))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.BSel3a.addItem(_fromUtf8(""))
        self.FBike1 = QtGui.QSlider(self.centralwidget)
        self.FBike1.setGeometry(QtCore.QRect(80, 360, 19, 160))
        self.FBike1.setMaximum(35)
        self.FBike1.setOrientation(QtCore.Qt.Vertical)
        self.FBike1.setObjectName(_fromUtf8("FBike1"))
        self.FBike2 = QtGui.QSlider(self.centralwidget)
        self.FBike2.setGeometry(QtCore.QRect(150, 360, 19, 160))
        self.FBike2.setMaximum(35)
        self.FBike2.setOrientation(QtCore.Qt.Vertical)
        self.FBike2.setObjectName(_fromUtf8("FBike2"))
        self.FBike3 = QtGui.QSlider(self.centralwidget)
        self.FBike3.setGeometry(QtCore.QRect(220, 360, 19, 160))
        self.FBike3.setMaximum(35)
        self.FBike3.setSingleStep(1)
        self.FBike3.setOrientation(QtCore.Qt.Vertical)
        self.FBike3.setObjectName(_fromUtf8("FBike3"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 320, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.Launch1 = QtGui.QPushButton(self.centralwidget)
        self.Launch1.setGeometry(QtCore.QRect(650, 70, 75, 23))
        self.Launch1.setObjectName(_fromUtf8("Launch1"))
        self.Launch2 = QtGui.QPushButton(self.centralwidget)
        self.Launch2.setGeometry(QtCore.QRect(650, 100, 75, 23))
        self.Launch2.setObjectName(_fromUtf8("Launch2"))
        self.Launch3 = QtGui.QPushButton(self.centralwidget)
        self.Launch3.setGeometry(QtCore.QRect(650, 130, 75, 23))
        self.Launch3.setObjectName(_fromUtf8("Launch3"))
        self.UpdateNames = QtGui.QPushButton(self.centralwidget)
        self.UpdateNames.setGeometry(QtCore.QRect(310, 70, 81, 23))
        self.UpdateNames.setObjectName(_fromUtf8("UpdateNames"))
        self.BSel1b = QtGui.QComboBox(self.centralwidget)
        self.BSel1b.setGeometry(QtCore.QRect(400, 100, 69, 22))
        self.BSel1b.setDuplicatesEnabled(True)
        self.BSel1b.setObjectName(_fromUtf8("BSel1b"))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel1b.addItem(_fromUtf8(""))
        self.BSel2b = QtGui.QComboBox(self.centralwidget)
        self.BSel2b.setGeometry(QtCore.QRect(480, 100, 69, 22))
        self.BSel2b.setDuplicatesEnabled(True)
        self.BSel2b.setObjectName(_fromUtf8("BSel2b"))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        self.BSel2b.addItem(_fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.closeButton.setText(_translate("MainWindow", "Close", None))
        self.testportsButton.setText(_translate("MainWindow", "Check Ports", None))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton", None))
        self.SerialList.setItemText(0, _translate("MainWindow", "None", None))
        self.SerialList.setItemText(1, _translate("MainWindow", "None2", None))
        self.testComms.setText(_translate("MainWindow", "Test Comms", None))
        self.CommsList.setItemText(0, _translate("MainWindow", "AA", None))
        self.CommsList.setItemText(1, _translate("MainWindow", "BB", None))
        self.Launch0.setText(_translate("MainWindow", "Launch!", None))
        self.BSel1a.setItemText(0, _translate("MainWindow", "1", None))
        self.BSel1a.setItemText(1, _translate("MainWindow", "2", None))
        self.BSel1a.setItemText(2, _translate("MainWindow", "3", None))
        self.BSel1a.setItemText(3, _translate("MainWindow", "1", None))
        self.BSel1a.setItemText(4, _translate("MainWindow", "2", None))
        self.BSel1a.setItemText(5, _translate("MainWindow", "3", None))
        self.BSel1a.setItemText(6, _translate("MainWindow", "1", None))
        self.BSel1a.setItemText(7, _translate("MainWindow", "2", None))
        self.BSel1a.setItemText(8, _translate("MainWindow", "3", None))
        self.BSel1a.setItemText(9, _translate("MainWindow", "1", None))
        self.BSel1a.setItemText(10, _translate("MainWindow", "2", None))
        self.BSel1a.setItemText(11, _translate("MainWindow", "3", None))
        self.BSel1a.setItemText(12, _translate("MainWindow", "1", None))
        self.BSel1a.setItemText(13, _translate("MainWindow", "2", None))
        self.BSel1a.setItemText(14, _translate("MainWindow", "3", None))
        self.BSel1a.setItemText(15, _translate("MainWindow", "None", None))
        self.BSel2a.setItemText(0, _translate("MainWindow", "1", None))
        self.BSel2a.setItemText(1, _translate("MainWindow", "2", None))
        self.BSel2a.setItemText(2, _translate("MainWindow", "3", None))
        self.BSel2a.setItemText(3, _translate("MainWindow", "1", None))
        self.BSel2a.setItemText(4, _translate("MainWindow", "2", None))
        self.BSel2a.setItemText(5, _translate("MainWindow", "3", None))
        self.BSel2a.setItemText(6, _translate("MainWindow", "1", None))
        self.BSel2a.setItemText(7, _translate("MainWindow", "2", None))
        self.BSel2a.setItemText(8, _translate("MainWindow", "3", None))
        self.BSel2a.setItemText(9, _translate("MainWindow", "1", None))
        self.BSel2a.setItemText(10, _translate("MainWindow", "2", None))
        self.BSel2a.setItemText(11, _translate("MainWindow", "3", None))
        self.BSel2a.setItemText(12, _translate("MainWindow", "1", None))
        self.BSel2a.setItemText(13, _translate("MainWindow", "2", None))
        self.BSel2a.setItemText(14, _translate("MainWindow", "3", None))
        self.BSel2a.setItemText(15, _translate("MainWindow", "None", None))
        self.BSel3a.setItemText(0, _translate("MainWindow", "1", None))
        self.BSel3a.setItemText(1, _translate("MainWindow", "2", None))
        self.BSel3a.setItemText(2, _translate("MainWindow", "3", None))
        self.BSel3a.setItemText(3, _translate("MainWindow", "1", None))
        self.BSel3a.setItemText(4, _translate("MainWindow", "2", None))
        self.BSel3a.setItemText(5, _translate("MainWindow", "3", None))
        self.BSel3a.setItemText(6, _translate("MainWindow", "1", None))
        self.BSel3a.setItemText(7, _translate("MainWindow", "2", None))
        self.BSel3a.setItemText(8, _translate("MainWindow", "3", None))
        self.BSel3a.setItemText(9, _translate("MainWindow", "1", None))
        self.BSel3a.setItemText(10, _translate("MainWindow", "2", None))
        self.BSel3a.setItemText(11, _translate("MainWindow", "3", None))
        self.BSel3a.setItemText(12, _translate("MainWindow", "1", None))
        self.BSel3a.setItemText(13, _translate("MainWindow", "2", None))
        self.BSel3a.setItemText(14, _translate("MainWindow", "3", None))
        self.BSel3a.setItemText(15, _translate("MainWindow", "None", None))
        self.label.setText(_translate("MainWindow", "Fake Bike Controls:", None))
        self.Launch1.setText(_translate("MainWindow", "Launch!", None))
        self.Launch2.setText(_translate("MainWindow", "Launch!", None))
        self.Launch3.setText(_translate("MainWindow", "Launch!", None))
        self.UpdateNames.setText(_translate("MainWindow", "Update Names", None))
        self.BSel1b.setItemText(0, _translate("MainWindow", "1", None))
        self.BSel1b.setItemText(1, _translate("MainWindow", "2", None))
        self.BSel1b.setItemText(2, _translate("MainWindow", "3", None))
        self.BSel1b.setItemText(3, _translate("MainWindow", "1", None))
        self.BSel1b.setItemText(4, _translate("MainWindow", "2", None))
        self.BSel1b.setItemText(5, _translate("MainWindow", "3", None))
        self.BSel1b.setItemText(6, _translate("MainWindow", "1", None))
        self.BSel1b.setItemText(7, _translate("MainWindow", "2", None))
        self.BSel1b.setItemText(8, _translate("MainWindow", "3", None))
        self.BSel1b.setItemText(9, _translate("MainWindow", "1", None))
        self.BSel1b.setItemText(10, _translate("MainWindow", "2", None))
        self.BSel1b.setItemText(11, _translate("MainWindow", "3", None))
        self.BSel1b.setItemText(12, _translate("MainWindow", "1", None))
        self.BSel1b.setItemText(13, _translate("MainWindow", "2", None))
        self.BSel1b.setItemText(14, _translate("MainWindow", "3", None))
        self.BSel1b.setItemText(15, _translate("MainWindow", "None", None))
        self.BSel2b.setItemText(0, _translate("MainWindow", "1", None))
        self.BSel2b.setItemText(1, _translate("MainWindow", "2", None))
        self.BSel2b.setItemText(2, _translate("MainWindow", "3", None))
        self.BSel2b.setItemText(3, _translate("MainWindow", "1", None))
        self.BSel2b.setItemText(4, _translate("MainWindow", "2", None))
        self.BSel2b.setItemText(5, _translate("MainWindow", "3", None))
        self.BSel2b.setItemText(6, _translate("MainWindow", "1", None))
        self.BSel2b.setItemText(7, _translate("MainWindow", "2", None))
        self.BSel2b.setItemText(8, _translate("MainWindow", "3", None))
        self.BSel2b.setItemText(9, _translate("MainWindow", "1", None))
        self.BSel2b.setItemText(10, _translate("MainWindow", "2", None))
        self.BSel2b.setItemText(11, _translate("MainWindow", "3", None))
        self.BSel2b.setItemText(12, _translate("MainWindow", "1", None))
        self.BSel2b.setItemText(13, _translate("MainWindow", "2", None))
        self.BSel2b.setItemText(14, _translate("MainWindow", "3", None))
        self.BSel2b.setItemText(15, _translate("MainWindow", "None", None))

