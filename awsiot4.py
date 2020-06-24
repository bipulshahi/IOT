import time
import datetime
import paho.mqtt.client as mqtt
import ssl

IoT_protocol_name = "x-amzn-mqtt-ca"
aws_iot_endpoint = "a1xip87ws8cwe4-ats.iot.us-east-2.amazonaws.com" # <random>.iot.<region>.amazonaws.com
url = "https://{}".format(aws_iot_endpoint)

#rootca=r'C:\Users\vipul\AppData\Local\Programs\Python\Python35\AWS\VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem'
#certificate=r'C:\Users\vipul\AppData\Local\Programs\Python\Python35\AWS\c64edd3b6b-certificate.pem.crt.txt'
#keyfile=r'C:\Users\vipul\AppData\Local\Programs\Python\Python35\AWS\c64edd3b6b-private.pem.key'

ca = "E:/AWS_Certificate/VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem" 
cert = "E:/AWS_Certificate/373100bd8c-certificate.pem.crt.txt"
private = "E:/AWS_Certificate/373100bd8c-private.pem.key"

ssl_context = ssl.create_default_context()
ssl_context.set_alpn_protocols([IoT_protocol_name])
ssl_context.load_verify_locations(cafile=ca)
ssl_context.load_cert_chain(certfile=cert, keyfile=private)

mqttc = mqtt.Client()
mqttc.tls_set_context(context=ssl_context)

mqttc.connect(aws_iot_endpoint, port=443)
#mqttc.loop_start()


def onc(mqttc,userdata,flags,rc):
    print("sucessfully connected to Amazon with RC",rc)
    mqttc.subscribe("mytopic/iot")

def onm(mqttc,userdata,msg):
    m=msg.payload.decode()
    print(m)
    if m=='hello':
        mqttc.publish('mytopic/iot','Hello Google')

mqttc.on_connect=onc
mqttc.on_message=onm
mqttc.loop_forever()
