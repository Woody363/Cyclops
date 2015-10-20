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


delay=0.15  #current delay in arduino is 0.05
	
ser.write(rv.encode('ascii'))		
time.sleep(delay)		
print("bike volts =" +str(ser.readline()))

ser.write(ra.encode('ascii'))		
time.sleep(delay)		
print("bike amps =" +str(ser.readline()))

ser.write(rp.encode('ascii'))		
time.sleep(delay)		
print("bike power =" +str(ser.readline()))

ser.write(r1.encode('ascii'))		
time.sleep(delay)		
print("bike1 =" +str(ser.readline()))

ser.write(r2.encode('ascii'))		
time.sleep(delay)		
print("bike2 =" +str(ser.readline()))

ser.write(r3.encode('ascii'))		
time.sleep(delay)		
print("bike3 =" +str(ser.readline()))

print("End")		
	
