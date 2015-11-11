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
    
        
def SimpleCar(inputBikes,mainForm):    
    
    delay=0.1   #current delay in arduino is 0.05, this should be larger to allow the arduino to respond
    
    
    
    xrange = [0, 100]
    yrange = [0, 100*3/4]
    figcar=plt.figure(frameon=False)
    
    #ax1=fig1.add_subplot(1,1,1)
    
    #mng = plt.get_current_fig_manager()
    #mng.window.showMaximized() #used to maxiwise figure, better to just press f for full
    
    bkg = figcar.add_axes([0, 0, 1, 1])
    car = figcar.add_axes([0, 0, 1, 1])
    
    bkg.set_xlim(*xrange)
    bkg.set_ylim(*yrange)
    bkg.axis('off')
    
    car.set_xlim(*xrange)
    car.set_ylim(*yrange)
    car.axis('off')
    
    
    d={'tc':0,'cw':0,'cl':0,'cx':0,'cy':0,'ca':0}#defines a dictionary that is accessable between functions
    
    d['tc']=time.time()
    
    d['cw']=10
    d['cl']=16
    
    d['cx']=50-d['cw']/2 ##set initial position of the car
    d['cy']=50-d['cl']/2
    d['ca']=-110
    
    def updateplot(i):
   
       # global tc
        #global cx
        #global cy
        #global ca
        values=CollectData(inputBikes,mainForm)
        #print(len(values))
        if len(values)==2:
            car.clear()
            car.axis('off')
            kc=1/20.0            
            ca=np.deg2rad(d['ca'])  #define local variables for use in equations            
            cx=d['cy']
            cy=d['cx']
            
            ax=d['cx']-d['cl']/2*np.sin(np.deg2rad(d['ca']))-np.sin(np.deg2rad(d['ca']))*values[0]*kc
            ay=d['cy']+d['cl']/2*np.cos(np.deg2rad(d['ca']))+np.cos(np.deg2rad(d['ca']))*values[0]*kc
            bx=d['cx']+d['cw']*np.cos(np.deg2rad(d['ca']))-d['cl']/2*np.sin(np.deg2rad(d['ca']))-np.sin(np.deg2rad(d['ca']))*values[1]*kc
            by=d['cy']+d['cw']*np.sin(np.deg2rad(d['ca']))+d['cl']/2*np.cos(np.deg2rad(d['ca']))+np.cos(np.deg2rad(d['ca']))*values[1]*kc
            
            
            d['ca']=np.rad2deg(np.arctan((ay-by)/(ax-bx)))         
            d['cx']=max(xrange[0],min(xrange[1],(ax+bx)/2))-d['cw']/2*np.cos(ca)+d['cl']/2*np.sin(ca)
            d['cy']=max(yrange[0],min(yrange[1],(ay+by)/2))-d['cw']/2*np.sin(ca)-d['cl']/2*np.cos(ca)
            
            if (ax-bx)>0:
                d['ca']=d['ca']+180 #to account for the limited 180 angle that arccos can give
            
            #d['ca']=d['ca']+np.rad2deg(np.arcsin(kc/d['cw']*60*(values[0]-values[1])))
           # d['cx']=d['cx']-(values[0]+values[1])/2.0*np.sin(d['ca'])*kc
            #d['cy']=d['cy']+(values[0]+values[1])/2.0*np.cos(d['ca'])*kc
            
            print(np.rad2deg(ca)) 
            print(d['ca'])            
            
            time.sleep(max(0,0.2+(d['tc']-time.time())))#keeps a costant delay whenever possible to keep update time constant 
            d['tc']=time.time()
        
            car.add_patch(patch.Rectangle(xy=(d['cx'],d['cy']),height=d['cl'],width=d['cw'],color='b',angle=d['ca']))
            car.add_patch(patch.Ellipse(xy=(ax,ay),width=5,height=5,color='r'))
            car.add_patch(patch.Ellipse(xy=(bx,by),width=5,height=5,color='r'))
    
    ani = animation.FuncAnimation(figcar,updateplot,interval=0)#true interval set by update function
    
    plt.show()

