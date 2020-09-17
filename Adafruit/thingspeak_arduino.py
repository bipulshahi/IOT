import time
import serial

import urllib3

http = urllib3.PoolManager()

ser = serial.Serial('COM7',9600)
time.sleep(2)

for i in range(50):
     a = ser.readline()
     b = a.decode()
     c = b.rstrip()
     d = c.split(" ")
     t = float(d[0])
     h = float(d[1])
     
     URL = "https://api.thingspeak.com/update?api_key=57JYXAWTXH13QKJT"
     finalurl = URL + "&field1=%s&field2=%s"%(t,h)

     s = http.request('GET' , finalurl)
     print('Message Published')
     print(t,h)
     s.close()
     time.sleep(45)

ser.close()
