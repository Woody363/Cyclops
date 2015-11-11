# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:39:22 2015

@author: Woody
"""

#from pylab import *


#t = arange(0.0, 2.0, 0.01)
#s = sin(2*pi*t)
#plot(t,s)

#-xlabel('time (s)')
#ylabel('voltage (mV)')
#title('About as simple as it gets, folks')
#grid(True)
#savefig("test.png")
#show()


#import matplotlib.pyplot as plt
#plt.plot([1,2,3,2,5,6,0,3])
#plt.show()


##2d plot
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#
#fig = plt.figure()
#
#def f(x, y):
#    return np.sin(x) + np.cos(y)
#
#x = np.linspace(0, 2 * np.pi, 120)
#y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
#
#im = plt.imshow(f(x, y), cmap=plt.get_cmap('jet'))
#
#def updatefig(*args):
#    global x,y
#    x += np.pi / 15.
#    y += np.pi / 20.
#    im.set_array(f(x,y))
#    return im,
#
#ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
#plt.show()


#"""
#A simple example of an animated plot
#"""
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#
#fig, ax = plt.subplots()
#
#x = np.arange(0, 2*np.pi, 0.01)        # x-array
#line, = ax.plot(x, np.sin(x))
#
#def animate(i):
#    line.set_ydata(np.sin(x+i/10.0))  # update the data
#    return line,
#
##Init only required for blitting to give a clean slate.
#def init():
#    line.set_ydata(np.ma.array(x, mask=True))
#    return line,
#
#ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,
#    interval=500, blit=True)
#plt.show()

#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#
#def update_line(num, data, line):
#    line.set_data(data[...,:num])
#    return line,
#
#fig1 = plt.figure()
#
#data = np.random.rand(2, 25)
#l, = plt.plot([], [], 'r-')
#plt.xlim(0, 1)
#plt.ylim(0, 1)
#plt.xlabel('x')
#plt.title('test')
#line_ani = animation.FuncAnimation(fig1, update_line, 25, fargs=(data, l),
#    interval=50, blit=True)
##line_ani.save('lines.mp4')
#
#fig2 = plt.figure()
#
#x = np.arange(-9, 10)
#y = np.arange(-9, 10).reshape(-1, 1)
#base = np.hypot(x, y)
#ims = []
#for add in np.arange(15):
#    ims.append((plt.pcolor(x, y, base + add, norm=plt.Normalize(0, 30)),))
#
#im_ani = animation.ArtistAnimation(fig2, ims, interval=50, repeat_delay=3000,
#    blit=True)
##im_ani.save('im.mp4', metadata={'artist':'Guido'})
#
#plt.show()

#
#import time
#from pylab import *
#import random
#
#ion() # turn interactive mode on
#
## initial data
#x = arange(-8, 8, 0.1);
#y1 = sin(x)
#y2 = cos(x)
#
## initial plot
#line1, line2, = plot(x, y1, 'r', x, y2, 'b')
#line1.axes.set_xlim(-10, 10)
#line1.axes.set_ylim(-2, 2)
#line1.set_label("line1")
#line2.set_label("line2")
#legend()
#grid()
#draw()
#
## update line 1
#for i in xrange(50):
#    time.sleep(0.1)
#
#    # update data
#    y1 = sin(x + float(i) / 10)
#
#    # update plot
#    line1.set_ydata(y1)
#    draw()
#
## update line 2
#for i in xrange(50):
#    time.sleep(0.1)
#
#    # update data
#    y2 = cos(x + float(i) / 10)
#
#    # update plot
#    line2.set_ydata(y2)
#    draw()
#


#import serial#need drawnow installed, not very versatile
#import matplotlib.pyplot as plt
#from drawnow import *
#import random
#
#values = []
#
#plt.ion()
#cnt=0
#
#
#def plotValues():
#    plt.title('Serial value from Arduino')
#    plt.grid(True)
#    plt.ylabel('Values')
#    plt.plot(values, 'rx-', label='values')
#    plt.legend(loc='upper right')
#
##pre-load dummy data
#for i in range(0,26):
#    values.append(0)
#    
#    
#while True:
#    
#    valueRead = int(random.random()*1000)
#
#    #check if valid value can be casted
#    try:
#        valueInInt = int(valueRead)
#        print(valueInInt)
#        if valueInInt <= 1024:
#            if valueInInt >= 0:
#                values.append(valueInInt)
#                values.pop(0)
#                drawnow(plotValues)
#            else:
#                print "Invalid! negative number"
#        else:
#            print "Invalid! too large"
#    except ValueError:
#        print "Invalid! cannot cast"    