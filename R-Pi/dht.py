import sys
import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(11,17)
print 'Temp: {0:0.2f}C Temp: {1:0.2f}F Humidity: {2:0.2f}%'.format(temperature,(9/5*temperature)+32,humidity)
