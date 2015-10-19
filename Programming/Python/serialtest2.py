##gets data from serial in a basic way. but has no error handling.
##


import serial
import time




ser = serial.Serial(
    port='COM4',\
    baudrate=115200,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)
	
print(ser.portstr + '\n')	
 #print(str(chr(1212)))
 #ser.open()	
 #ser.write('deil')
	
rv="aAAV?--------"
ra="aAAI?--------"
rp="aAAP?--------"
r1="aAAB1?-------"
r2="aAAB2?-------"
r3="aAAB3?-------"
#codes required to request different information


delay=0.15

for x in range(0,3):
            
    ser.write(rv.encode('ascii'))		
    time.sleep(delay)

    tempstr=str(ser.readline())

    volts1=[float(tempstr[5:8])/10,float(tempstr[8:11])/10,float(tempstr[11:14])/10]
          
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
	
