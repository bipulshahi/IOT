import time
import datetime
import paho.mqtt.client as mqtt
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

#rootca=r'C:\Users\vipul\AppData\Local\Programs\Python\Python35\AWS\VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem'
#certificate=r'C:\Users\vipul\AppData\Local\Programs\Python\Python35\AWS\c64edd3b6b-certificate.pem.crt.txt'
#keyfile=r'C:\Users\vipul\AppData\Local\Programs\Python\Python35\AWS\c64edd3b6b-private.pem.key'

rootca=r'E:\AWS_Certificate\VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem'
certificate=r'E:\AWS_Certificate\373100bd8c-certificate.pem.crt.txt'
keyfile=r'E:\AWS_Certificate\373100bd8c-private.pem.key'


c=mqtt.Client()

c.tls_set(rootca,certfile=certificate,keyfile=keyfile,
          cert_reqs=ssl.CERT_REQUIRED,tls_version=ssl.PROTOCOL_TLSv1_2,
          ciphers=None)


c.connect('a1xip87ws8cwe4-ats.iot.us-east-2.amazonaws.com',8883)

def onc(c,userdata,flags,rc):
    print("sucessfully connected to Amazon with RC",rc)
    c.subscribe("mytopic/iot")

def onm(c,userdata,msg):
    m=msg.payload.decode()
    print(m)
    if m=='hello':
        c.publish('mytopic/iot','How are you')

c.on_connect=onc
c.on_message=onm
c.loop_forever()
