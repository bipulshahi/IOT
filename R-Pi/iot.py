import sys
import RPi.GPIO as GPIO
import os
import time
import Adafruit_DHT
import urllib2

def readDHT():
    humidity,temperature=Adafruit_DHT.read_retry(11,4)   

    return(str(temperature),str(humidity))


def main():

    print 'starting...'

    URL = 'https://api.thingspeak.com/update?api_key=GX8W73AOT6NP0D54'
    print "wait...."



    while True:
        (humi,temp)=readDHT()
        finalURL = URL +"&field1=%s&field2=%s"%(humi,temp)
        print finalURL
        s=urllib2.urlopen(finalURL);
        print humi+ " " + temp + " "
        s.close
        time.sleep(60)


if __name__=='__main__':
    main()



