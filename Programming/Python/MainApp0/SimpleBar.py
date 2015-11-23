# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 23:54:38 2015

@author: Woody
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import matplotlib.patches as patch
from getdata import *

import time

    
        
def SimpleBar(inputBikes,mainForm):    
    
    delay=0.1   #current delay in arduino is 0.05, this should be larger to allow the arduino to respond
    
    
    
    xrange = [0, 100]
    yrange = [0, 100]
    SBar=plt.figure(frameon=False)
    #ax1=fig1.add_subplot(1,1,1)
    
    #mng = plt.get_current_fig_manager()
    #mng.window.showMaximized() #used to maxiwise figure, better to just press f for full
    
    bkg = SBar.add_axes([0, 0, 1, 1])
    bars = SBar.add_axes([0, 0, 1, 1])
    
    bkg.set_xlim(*xrange)
    bkg.set_ylim(*yrange)
    
    bars.set_xlim(*xrange)
    bars.set_ylim(*yrange)
    
    t0=time.time()
    global tb
    tb=time.time()
    
    def updateplot(i):
    #global t0
        values=CollectData(inputBikes,mainForm)
        nbars=len(values)
        bwidth=60.0/(nbars+1)
        ypos=10
        xpos=[]
        for j in range(0,nbars):
            xpos.append(5.0+(j+1.0)*90.0/(nbars+1)-bwidth/2.0)
        global tb
        #print(t0-time.time())
        #t0=time.time()
        bars.clear()
        bars.axis('off')
        #time.sleep(i%2*delay)#adds in variable delay to simulate an unpredictable getdata function
        time.sleep(max(0,0.2+(tb-time.time())))#keeps a costant delay whenever possible to keep update time constant 
        tb=time.time()
        for j in range(0,nbars):
            bars.add_patch(patch.Rectangle(xy=(xpos[j],ypos),height=values[j]*2,width=bwidth,color='r',angle=0))
        #ax2.add_patch(patch.Rectangle(xy=(1,1),height=1.5,width=3,color='r',angle=i/1.0))
        #ax1.add_patch(patch.Ellipse(xy=((i/3.0)%5, 1.5), width=1.5, height=1.0, angle=0))
        
    
    ani=animation.FuncAnimation(SBar,updateplot,interval=0)#true interval set by update function
    
    plt.show()

