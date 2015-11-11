# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 00:20:15 2015

@author: Woody
"""

print("Start")
import sys
from PyQt4 import QtCore, QtGui
from SerialFind import *
from getdata import *

from test_ui import Ui_MainWindow

from plottest1 import *
from SimpleBar import *
from SimpleCar import *


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
    
def Launch0():
    plottest1()
    
    
def Launch1():
    print("Launch1")
    SimpleBar([myapp.ui.BSel1a,myapp.ui.BSel2a,myapp.ui.BSel3a],myapp)
    
    
def Launch2():
    print("Launch2")
    SimpleCar([myapp.ui.BSel1b,myapp.ui.BSel2b],myapp)
    
   
    
    
def Launch3():
    print("Launch2")
    UpdateBikeSelect()
    
def UpdateBikeNames():  
    objlist=[myapp.ui.BSel1a,myapp.ui.BSel2a,myapp.ui.BSel3a,myapp.ui.BSel1b,myapp.ui.BSel2b] 
    
    if objlist[1].count != 3*(myapp.ui.CommsList.count()+1)+1:
        for i in range(0,len(objlist)): 
            objlist[i].clear()
            for j in range(0,3*(myapp.ui.CommsList.count()+1)+1):
                objlist[i].addItem("None")
    
    devicelist=[]
    
    for i in range(0,myapp.ui.CommsList.count()):
        devicelist.append(myapp.ui.CommsList.itemText(i))
    devicelist.append("fake")
    
    for i in range(0,len(objlist)):   
       # objlist[i].clear()
        for j in range(0,len(devicelist)):
            for k in range(0,3):
                objlist[i].setItemText(3*j+k,devicelist[j]+str(k))
    


class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.testportsButton.clicked.connect(serialfind)
        self.ui.pushButton_3.clicked.connect(testfunc3)
        self.ui.testComms.clicked.connect(commstest)  
        self.ui.Launch0.clicked.connect(Launch0) 
        self.ui.Launch1.clicked.connect(Launch1) 
        self.ui.Launch2.clicked.connect(Launch2) 
        self.ui.Launch3.clicked.connect(Launch3) 
        #self.ui.BSel1a.mousePressEvent.connect(UpdateBikeSelect(self.ui.BSel1a.))
        self.ui.UpdateNames.clicked.connect(UpdateBikeNames)
        
    


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    serialfind()
    UpdateBikeNames()
    myapp.show()
    print("Main Window Open")
    #MainWindow.closeButton.setText(_translate("MainWindow", "Open", None))
    sys.exit(app.exec_())