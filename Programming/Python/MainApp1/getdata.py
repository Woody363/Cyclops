# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 16:48:19 2015

@author: Woody
"""

import serial
import time
import random


print("Loaded Libraries")

#setup the serial connection:


def getdata(serial_port,iD,MiD,mode):
    status=0
    delay=0.1
    values=[-1,-1,-1]
    #time.sleep(delay)
    
    if iD=="fake":
        return [serial_port.ui.FBike1.sliderPosition(),serial_port.ui.FBike2.sliderPosition(),serial_port.ui.FBike3.sliderPosition()]
    
    
       
    
    #ser.flush()
    try:
        ser = serial.Serial(
            port=str(serial_port),\
            baudrate=115200,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout=0) 
        #ser.port=serial_port
        ser.readline() #reads in a line and discards it, incase previous calls are still pending
    except Exception as e:
        print("Warning, \"", str(e), "\" error")
        #ser.close()
        return([-1,-1,-1])
   #ser.write(("a" +iD +mode +"?--------")[0:12].encode('ascii'))
    for x in range(0,5):#attemt connection 5 times
       # print(x)
        status=2
        ser.write(str(("a" +iD +MiD +mode +"?--------")[0:12]).encode('ascii'))
        #use str above because outside the ide this is treated as a QString, which is different
        time.sleep(delay)
        datastr=str(ser.readline())
       #print(str(len(datastr)))
        if len(datastr)==14 and datastr[1:3]==MiD:
            status=1
            try:    
                values=[float(datastr[3:6]),float(datastr[6:9]),float(datastr[9:12])]
            except ValueError:
                status=3
            break
            
    
    if mode=="V" or mode=="I":
        values[0]=values[0]/10
        values[1]=values[1]/10
        values[2]=values[2]/10
    elif mode=="B1" or mode=="B2" or mode=="B3":
        values[0]=values[0]/10
        values[1]=values[1]/10
    
    return values
   

def fakegetdata(iD,MiD,mode):
    
    time.sleep(2*delay)
    return([random.random(),random.random(),random.random()])    
    
def CollectData(inputBikes,mainForm):

    inputdevices=[]
    inputb=[] #dynamically grab the bikes from the form and get their data
    for i in range(0,len(inputBikes)):
        inputb.append(inputBikes[i].currentIndex())
    inputb=filter(lambda a: a != inputBikes[i].count()-1, inputb)#remove "None option"
    for i in range(0,len(inputb)):    
        inputdevices.append(int(inputb[i]/3.0))
    #print(inputdevices)
    inputdevices=list(set(inputdevices))
    #print(inputdevices)
    
    bikedata=[0]*inputBikes[i].count()
    
    for i in range(0,len(inputdevices)):
        if inputdevices[i] < mainForm.ui.CommsList.count():
            tempdata=getdata(mainForm.ui.SerialList.currentText(),mainForm.ui.CommsList.itemText(inputdevices[i]),"SB","V")
        else: 
            tempdata=getdata(mainForm,"fake","SB","V")
        bikedata[3*inputdevices[i]]=tempdata[0]
        bikedata[3*inputdevices[i]+1]=tempdata[1]
        bikedata[3*inputdevices[i]+2]=tempdata[2]
    #getdata(myapp.ui.SerialList.currentText(),floor()) 
    outputb=[]    
    for i in range(0,len(inputb)):
        outputb.append(max(0,bikedata[inputb[i]]))
        if int(bikedata[inputb[i]])==-1:
            print("Warning, no data from input " + str(inputBikes[1].itemText(inputb[i])))
    return(outputb)