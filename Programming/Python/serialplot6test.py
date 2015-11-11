##gets data from serial with multiple trys and error handling
##recieving a different set of data back (now only length 14 without 
#end line puctuation, not sure what happened...)


import serial
import time
import random
#import matplotlib.pyplot as plt

#from pylab import *

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

print("Start")

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
	
delay=0.1   #current delay in arduino is 0.05


volts1=[]
amps1=[]
data1=[1]*30
voltagedata=[0]*30

plt.plot(data1)

plt.ylabel('some numbers')


plt.show()

#for x in range(0,5): #lets make some data
#            
#    
#    volts1.append(getdata("AA","AV","V"))
#    data1[x]=volts1[x][1]
    #print(data1[x])
    
    
#import matplotlib.pyplot as plt
    #print[data1]
   
   
from matplotlib.patches import Ellipse

fig = plt.figure(1, figsize=(5,5), dpi=90)
ax = fig.add_subplot(111)

el = Ellipse(xy=(0.5, 0.5), width=5.5, height=1.2, angle=0)  

ax.add_patch(el)

ax.set_title('Filled Polygon')
xrange = [-1, 3]
yrange = [-1, 3]
ax.set_xlim(*xrange)
ax.set_xticks(range(*xrange) + [xrange[-1]])
ax.set_ylim(*yrange)
ax.set_yticks(range(*yrange) + [yrange[-1]])
ax.set_aspect(1)   
   
   

fig = plt.figure()
ax = plt.axes(xlim=(0, 25), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)


 
#e1.set_visible(False)
#plt.show()

def init():
    return plt.plot(data1,color='white')#create a blank plat as this frame seems to stick around
    plt.axis('off')
    line.set_data([], [])
     
    return line,
    

def updateplot(iterator):
    volts1.append(fakegetdata("AA","AV","I"))
    data1[iterator%30]=volts1[iterator][1]
    print(data1[iterator%30])
    #e1.set_visible(True)
    anifig=plt.plot(data1,color='black')    
    #a2 = fig.add_subplot(1,1,1)
    #anifig.add_patch(e1)
    return anifig

#ani = animation.FuncAnimation(fig, plt.plot(data1), interval=50, blit=True)#doesnt work yet
ani = animation.FuncAnimation(fig, updateplot , init_func=init, interval=50, blit=True)#doesnt work yet

plt.show()
#
#plt.plot(data1)
#plt.show()



print("End")		
	
