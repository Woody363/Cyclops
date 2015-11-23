# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 18:25:18 2015

@author: Woody
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import matplotlib.patches as patch

import time


def plottest1():
    delay=0.1   #current delay in arduino is 0.05, this should be larger to allow the arduino to respond

    
    
     
    
    
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
    global t1
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

