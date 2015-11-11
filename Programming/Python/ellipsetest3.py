# -*- coding: utf-8 -*-
"""
Created on Sun Nov 08 13:16:07 2015

@author: Woody
"""

##gets data from serial with multiple trys and error handling
##recieving a different set of data back (now only length 14 without 
#end line puctuation, not sure what happened...)

print("Start")

import serial
import time
import random
#import matplotlib.pyplot as plt

#from pylab import *

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import matplotlib.patches as patch

print("Loaded Libraries")

ser = serial.Serial(
    port='COM4',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

def getdata(iD,MiD,mode):
    status=0
    values=[0,0,0]
    time.sleep(delay)
    #ser.flush()
    ser.readline() #reads in a line and discards it, incase previous calls are still pending
    #ser.write(("a" +iD +mode +"?--------")[0:12].encode('ascii'))
    for x in range(0,5):#attemt connection 5 times
       # print(x)
        status=2
        ser.write(("a" +iD +MiD +mode +"?--------")[0:12].encode('ascii'))
        time.sleep(delay)
        datastr=str(ser.readline())
       #print(str(len(datastr)))
        if len(datastr)==14 and datastr[1:3]==MiD:
            status=1
            try:    
                values=[float(datastr[3:6]),float(datastr[6:9]),float(datastr[9:12])]
            except ValueError:
                status=3
            #values=[float(datastr[5:8])/10,float(datastr[8:11])/10,float(datastr[11:14])/10]
            break
            
    #print(str(status))
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
    
    
	
#print(ser.portstr + '\n')	
	
delay=0.1   #current delay in arduino is 0.05, this shoul be larger to allow the arduino to respond


volts1=[]
amps1=[]
data1=[1]*30
voltagedata=[0]*30




 


xrange = [-1, 3]
yrange = [-1, 3]
fig1=plt.figure(frameon=False)
#ax1=fig1.add_subplot(1,1,1)

#mng = plt.get_current_fig_manager()
#mng.window.showMaximized() #used to maxiwise figure, better to just press f for full

ax1 = fig1.add_axes([0, 0, 1, 1])
ax2 = fig1.add_axes([0, 0, 1, 1])

ax1.set_xlim(*xrange)
ax1.set_ylim(*yrange)

ax2.set_xlim(*xrange)
ax2.set_ylim(*yrange)

t0=time.time()
t1=time.time()

def updateplot3(i):
    #global t0
    global t1
    #print(t0-time.time())
    #t0=time.time()
    ax1.clear()
    ax1.axis('off')
    time.sleep(i%2*delay)#adds in variable delay to simulate an unpredictable getdata function
    time.sleep(max(0,0.2+(t1-time.time())))#keeps a costant delay whenever possible to keep update time constant 
    t1=time.time()
    ax2.add_patch(patch.Rectangle(xy=(1,1),height=1.5,width=3,color='r',angle=i/1.0))
    ax1.add_patch(patch.Ellipse(xy=((i/3.0)%5, 1.5), width=1.5, height=1.0, angle=0))

ani = animation.FuncAnimation(fig1,updateplot3,interval=0)#true interval set by update function

plt.show()




print("End")		
	
