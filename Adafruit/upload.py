# import standard python modules.
import time

# import adafruit dht library.
import Adafruit_DHT

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

import serial

# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'YOUR_AIO_KEY'

# Set to your Adafruit IO username.
ADAFRUIT_IO_USERNAME = 'YOUR_AIO_USERNAME'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

ser = serial.Serial('COM7',9600)
time.sleep(2)

# Set up Adafruit IO Feeds.
temperature_feed = aio.feeds('temperature')
humidity_feed = aio.feeds('humidity')

for i in range(50):
     a = ser.readline()
     b = a.decode()
     c = b.rstrip()
     d = c.split(" ")
     t = float(d[0])
     h = float(d[1])
     
     temperature = '%.2f'%(t)
     humidity = '%.2f'%(h)
     aio.send(temperature_feed.key, str(t))
     aio.send(humidity_feed.key, str(h))
     

