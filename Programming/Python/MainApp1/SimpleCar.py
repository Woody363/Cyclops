# -*- coding: utf-8 -*-
"""
Created on Mon Nov 09 23:54:38 2015

@author: Woody
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.image as img
import matplotlib.cbook as cbook
import os


import matplotlib.patches as patch
from getdata import *



import time 
    
        
def SimpleCar(inputBikes,mainForm):    
    
    delay=0.1   #current delay in arduino is 0.05, this should be larger to allow the arduino to respond
    
    floc=os.path.dirname(os.path.abspath(__file__))    
    
    bkg_file = cbook.get_sample_data(str(floc+'/Logo.png'))
    bkg_image = plt.imread(bkg_file)    
    
    
    
    xrange = [0, 100]
    yrange = [0, 100*3/4]
    figcar=plt.figure(frameon=False)
    
    
    
    bkg = figcar.add_axes([0, 0, 1, 1])
    car = figcar.add_axes([0, 0, 1, 1])
    
    bkg.set_xlim(*xrange)
    bkg.set_ylim(*yrange)
    bkg.axis('off')    
    #im=figcar.imshow(bkg_image)    
    
    car.add_patch(patch.Ellipse(xy=(xrange[1]/4.0,yrange[1]/2.0),height=20,width=20,color="black")) 
    car.add_patch(patch.Ellipse(xy=(3*xrange[1]/4.0,yrange[1]/2.0),height=20,width=20,color="black"))
    #bkg.figimage(im, 0, 10)    
    
    car.set_xlim(*xrange)
    car.set_ylim(*yrange)
    car.axis('off')
    
    
    d={'tc':0,'cw':0,'cl':0,'cx':0,'cy':0,'ca':0}#defines a dictionary that is accessable between functions
    
    d['tc']=time.time()
    
    d['cw']=8
    d['cl']=11
    
    d['cx']=50-d['cw']/2 ##set initial position of the car
    d['cy']=50-d['cl']/2
    d['ca']=0
    
    def kc(x,y):
        
        if (x-xrange[1]/4.0)*(x-xrange[1]/4.0)+(y-yrange[1]/2.0)*(y-yrange[1]/2.0) < 15.0*15.0/4.0:   
            return 1.0/100.0
        if (x-3*xrange[1]/4.0)*(x-3*xrange[1]/4.0)+(y-yrange[1]/2.0)*(y-yrange[1]/2.0) < 15.0*15.0/4.0:   
            return 1.0/100.0
        
        return  1/20.0   
    
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
                      
            ca=np.deg2rad(d['ca'])  #define local variables for use in equations            
            cx=d['cy']
            cy=d['cx']
            
            ax=d['cx']-d['cl']/2*np.sin(np.deg2rad(d['ca']))
            ay=d['cy']+d['cl']/2*np.cos(np.deg2rad(d['ca']))
            bx=d['cx']+d['cw']*np.cos(np.deg2rad(d['ca']))-d['cl']/2*np.sin(np.deg2rad(d['ca']))
            by=d['cy']+d['cw']*np.sin(np.deg2rad(d['ca']))+d['cl']/2*np.cos(np.deg2rad(d['ca']))
            
            ax=ax-np.sin(np.deg2rad(d['ca']))*values[0]*kc(ax,ay)
            ay=ay+np.cos(np.deg2rad(d['ca']))*values[0]*kc(ax,ay)
            bx=bx-np.sin(np.deg2rad(d['ca']))*values[1]*kc(bx,by)
            by=by+np.cos(np.deg2rad(d['ca']))*values[1]*kc(bx,by)
            
            
            d['ca']=np.rad2deg(np.arctan((ay-by)/(ax-bx)))         
            d['cx']=max(xrange[0],min(xrange[1],(ax+bx)/2))-d['cw']/2*np.cos(ca)+d['cl']/2*np.sin(ca)
            d['cy']=max(yrange[0],min(yrange[1],(ay+by)/2))-d['cw']/2*np.sin(ca)-d['cl']/2*np.cos(ca)
            
            if (ax-bx)>0:
                d['ca']=d['ca']+180 #to account for the limited 180 angle that arccos can give
            
            #d['ca']=d['ca']+np.rad2deg(np.arcsin(kc/d['cw']*60*(values[0]-values[1])))
           # d['cx']=d['cx']-(values[0]+values[1])/2.0*np.sin(d['ca'])*kc
            #d['cy']=d['cy']+(values[0]+values[1])/2.0*np.cos(d['ca'])*kc
            
            #print(np.rad2deg(ca)) 
            #print(d['ca'])            
            
            time.sleep(max(0,0.2+(d['tc']-time.time())))#keeps a costant delay whenever possible to keep update time constant 
            d['tc']=time.time()
            car.add_patch(patch.Ellipse(xy=(xrange[1]/4.0,yrange[1]/2.0),height=15,width=15,color="black")) 
            car.add_patch(patch.Ellipse(xy=(3*xrange[1]/4.0,yrange[1]/2.0),height=15,width=15,color="black"))
    
            car.add_patch(patch.Rectangle(xy=(d['cx'],d['cy']),height=d['cl'],width=d['cw'],color='b',angle=d['ca']))
            car.add_patch(patch.Ellipse(xy=(ax,ay),width=2,height=4,color='r',angle=d['ca']))
            car.add_patch(patch.Ellipse(xy=(bx,by),width=2,height=4,color='r',angle=d['ca']))
    
    ani = animation.FuncAnimation(figcar,updateplot,interval=0)#true interval set by update function
    
    plt.show()

