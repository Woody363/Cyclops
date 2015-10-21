##gets data from serial with multiple trys and error handling
##


import serial
import time

def getdata(iD,MiD,mode):
    status=0
    values=[0,0,0]
    time.sleep(delay)
    #ser.flush()
    ser.readline() #reads in a line and discards it, incase previous calls are still pending
    #ser.write(("a" +iD +mode +"?--------")[0:12].encode('ascii'))
    for x in range(0,5):
       # print(x)
        status=2
        ser.write(("a" +iD +MiD +mode +"?--------")[0:12].encode('ascii'))
        time.sleep(delay)
        datastr=str(ser.readline())
        if len(datastr)==19 and datastr[3:5]==MiD:
            status=1
            try:    
                values=[float(datastr[5:8]),float(datastr[8:11]),float(datastr[11:14])]
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
   

ser = serial.Serial(
    port='COM4',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
	
print(ser.portstr + '\n')	
	
delay=0.1   #current delay in arduino is 0.05



for x in range(0,5): #test loop to see how many requests can occur before it breaks
            

    volts1=getdata("AA","AV","V")
    
    print("bike Volts = "         \
          +str(volts1[0]) +" "     \
          +str(volts1[1]) +" "      \
          +str(volts1[2]))
    amps1=getdata("AA","AA","I")
    
    print("bike Amps = "         \
        +str(amps1[0]) +" "     \
        +str(amps1[1]) +" "      \
        +str(amps1[2])) 


for x in range(0,3): #test loop to see how many requests can occur before it breaks
            

    volts1=getdata("AA","AV","V")
    
    print("bike Volts = "         \
          +str(volts1[0]) +" "     \
          +str(volts1[1]) +" "      \
          +str(volts1[2]))       

print("End")		
	
