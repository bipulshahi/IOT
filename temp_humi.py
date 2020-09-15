import ssl
import paho.mqtt.client as mqtt
import time
import datetime
import serial
import time

ser = serial.Serial('COM7',9600)
time.sleep(2)

Iot_protocol_name = 'x-amzn-mqtt-ca'
aws_end_point = 'amwmnb948lrc8-ats.iot.ap-south-1.amazonaws.com'

ca = 'D:/aws_certi/AwsRCA.pem'
cert = 'D:/aws_certi/f5b8f558ef-certificate.pem.crt.txt'
private = 'D:/aws_certi/f5b8f558ef-private.pem.key'

ssl_context = ssl.create_default_context()
ssl_context.set_alpn_protocols([Iot_protocol_name])
ssl_context.load_verify_locations(cafile=ca)
ssl_context.load_cert_chain(certfile=cert , keyfile=private)

client = mqtt.Client()

client.tls_set_context(context = ssl_context)
client.connect(aws_end_point, port=443)

client.loop_start()

topic = "test/a"

for i in range(50):
     a = ser.readline()
     b = a.decode()
     c = b.rstrip()
     d = c.split(" ")
     t = float(d[0])
     h = float(d[1])

     timestamp = datetime.datetime.now()
     client.publish(topic,'{"Time" : "'+str(timestamp)+'" , "T": '+str(t)+' , "H": '+str(h)+'}')
     print('Message Published')
     print(d)
     time.sleep(5)
     
ser.close()
