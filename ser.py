import serial
import time

ser = serial.Serial('COM7',9600)
time.sleep(5)

data = []
for i in range(50):
     a = ser.readline()
     b = a.decode()
     c = b.rstrip()
     d = float(c)
     print(d)
     data.append(d)
     time.sleep(1)
     
ser.close()
