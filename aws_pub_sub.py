import sys
import ssl
import time
import datetime
import paho.mqtt.client as mqtt

IoT_protocol_name = "x-amzn-mqtt-ca"
aws_iot_endpoint = "a1xip87ws8cwe4-ats.iot.us-east-2.amazonaws.com"

ca = 'E:/AWS_Certificate/VeriSign-Class 3-Public-Primary-Certification-Authority-G5.pem'
cert = 'E:/AWS_Certificate/373100bd8c-certificate.pem.crt.txt'
private = 'E:/AWS_Certificate/373100bd8c-private.pem.key'

ssl_context = ssl.create_default_context()
ssl_context.set_alpn_protocols([IoT_protocol_name])
ssl_context.load_verify_locations(cafile=ca)
ssl_context.load_cert_chain(certfile=cert , keyfile=private)


def on_connect(client, userdata, flags, rc):
              print('Connected with code:' , rc)
              client.subscribe("test/a")
              
def on_message(client,userdata,msg):
              print(str(msg.payload))
              
client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.tls_set_context(context=ssl_context)
client.connect(aws_iot_endpoint, port=443)

client.loop_start()

time.sleep(2)
while True:
              client.publish("test/b","Hello Everyone")
              print('Message Published')
              #client.subscribe(topic2,"Message from AWS")
              time.sleep(3)

client.loop_start()
client.disconnect





