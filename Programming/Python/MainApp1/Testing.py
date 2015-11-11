# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 00:20:15 2015

@author: Woody
"""

import sys
from PyQt4 import QtCore, QtGui
from SerialFind import *
from getdata import *

from test_ui import Ui_MainWindow

from plottest1 import *


def serialfind():
    ports_list=serial_ports()
   # print(ports_list)
    myapp.ui.SerialList.clear()
    
    for i in range(0,len(ports_list)):
        #print(i)
        #print(ports_list[i])
        myapp.ui.SerialList.addItem(ports_list[i])
   
def commstest():
    #print("comms")
    
    cport=myapp.ui.SerialList.currentText()
    cdevice=myapp.ui.CommsList.currentText()
    
    data=getdata(cport,cdevice,"TS","V")
    
    if int(data[0])==-1 & int(data[1])==-1 & int(data[2])==-1:
        myapp.ui.CommsResult.setText("Communication with " + cdevice + " failed")
        myapp.ui.VTestResult.setText("")
    else: 
        myapp.ui.CommsResult.setText("Communication with " + cdevice + " succeeded")
        myapp.ui.VTestResult.setText("V1=" + str(data[0]) + "\nV2=" + str(data[1]) + "\nV3=" + str(data[0]))
    
def testfunc3():
    myapp.ui.pushButton_3.setText(myapp.ui.SerialList.currentText())
    
def Launch1():
    plottest1()

class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.testportsButton.clicked.connect(serialfind)
        self.ui.pushButton_3.clicked.connect(testfunc3)
        self.ui.testComms.clicked.connect(commstest)  
        self.ui.Launch1.clicked.connect(Launch1)  
        
    def testfunc2(self,parent):
        #self.ui.pushButton_3.setText("HI!")
        testfunc3(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    serialfind()
    myapp.show()
    print("Main Window Open")
    #MainWindow.closeButton.setText(_translate("MainWindow", "Open", None))
    sys.exit(app.exec_())