##gets data from serial with multiple trys and error handling
##


import serial
import time

def getdata(iD,mode):
    status=0
    values=[0,0,0]
    time.sleep(delay)
    #ser.flush()
    ser.readline() #reads in a line and discards it, incase previous calls are still pending
    #ser.write(("a" +iD +mode +"?--------")[0:12].encode('ascii'))
    for x in range(0,5):
       # print(x)
        status=2
        ser.write(("a" +iD +mode +"?--------")[0:12].encode('ascii'))
        time.sleep(delay)
        datastr=str(ser.readline())
        if len(datastr)==19 and datastr[3:5]==iD:
            status=1
            try:    
                values=[float(datastr[5:8])/10,float(datastr[8:11])/10,float(datastr[11:14])/10]
            except ValueError:
                status=3
            #values=[float(datastr[5:8])/10,float(datastr[8:11])/10,float(datastr[11:14])/10]
            break
            
    #print(str(status))
    
    return values
   

ser = serial.Serial(
    port='COM4',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
	
print(ser.portstr + '\n')	
	
rv="aAAV?--------"
ra="aAAI?--------"
rp="aAAP?--------"
r1="aAAB1?-------"
r2="aAAB2?-------"
r3="aAAB3?-------"
#codes required to request different information


delay=0.1   #current delay in arduino is 0.05



for x in range(0,30): #test loop to see how many requests can occur before it breaks
            

    volts1=getdata("AA","V")
    
#    print("bike Volts = "         \
#          +str(volts1[0]) +" "     \
#          +str(volts1[1]) +" "      \
#          +str(volts1[2]))
    amps1=getdata("AA","I")
    
    print("bike Amps = "         \
        +str(amps1[0]) +" "     \
        +str(amps1[1]) +" "      \
        +str(amps1[2])) 


#time.sleep(10)
for x in range(0,3): #test loop to see how many requests can occur before it breaks
            

    volts1=getdata("AA","V")
    
    print("bike Volts = "         \
          +str(volts1[0]) +" "     \
          +str(volts1[1]) +" "      \
          +str(volts1[2]))       

    ser.write(ra.encode('ascii'))		
    time.sleep(delay)

    tempstr=str(ser.readline())

    amps1=[float(tempstr[5:8])/10,float(tempstr[8:11])/10,float(tempstr[11:14])/10]
     
    print("bike Amps  = "        \
          +str(amps1[0]) +" "     \
          +str(amps1[1]) +" "      \
          +str(amps1[2]))  

    ser.write(rp.encode('ascii'))		
    time.sleep(delay)

    tempstr=str(ser.readline())

    watts1=[float(tempstr[5:8]),float(tempstr[8:11]),float(tempstr[11:14])]
     

    print("bike Watts = "        \
          +str(watts1[0]) +" "    \
          +str(watts1[1]) +" "     \
          +str(watts1[2]))


    ser.write(r1.encode('ascii'))		
    time.sleep(delay)

    tempstr=str(ser.readline())

    bike1=[float(tempstr[5:8]),float(tempstr[8:11]),float(tempstr[11:14])]
     

    print("bike 1 = "            \
          +str(bike1[0]) +" "     \
          +str(bike1[1]) +" "      \
          +str(bike1[2]))


    ser.write(r2.encode('ascii'))		
    time.sleep(delay)

    tempstr=str(ser.readline())
    bike2=[float(tempstr[5:8])/10,float(tempstr[8:11])/10,float(tempstr[11:14])]
     

    print("bike 2 = "            \
          +str(bike2[0]) +" "     \
          +str(bike2[1]) +" "      \
          +str(bike2[2]))

    ser.write(r3.encode('ascii'))		
    time.sleep(delay)

    tempstr=str(ser.readline())
    bike3=[float(tempstr[5:8])/10,float(tempstr[8:11])/10,float(tempstr[11:14])]
     

    print("bike 3 = "            \
          +str(bike3[0]) +" "     \
          +str(bike3[1]) +" "      \
          +str(bike3[2]))


print("End")		
	
