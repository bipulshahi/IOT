import ssl
import time
import datetime
import paho.mqtt.client as client

IoT_protocol = "x-amzn-mqtt-ca"
aws_end_point = "amwmnb948lrc8-ats.iot.ap-south-1.amazonaws.com"

ca = "./AmazonRootCA1.pem"
cert = "./69311293f0-certificate.pem.crt"
private = "./69311293f0-private.pem.key"

ssl_context = ssl.create_default_context()
ssl_context.set_alpn_protocols([IoT_protocol])
ssl_context.load_verify_locations(cafile=ca)
ssl_context.load_cert_chain(certfile=cert , keyfile=private)

def on_connection_success(mqttc,userdata,flags,rc):
    print('Connected with response code',rc)
    mqttc.subscribe('test/a')

def on_message_recieve(mqttc,userdata,msg):
    a = msg.payload
    b = a.decode()
    c = b.rstrip()
    print(str(c))

mqttc = client.Client()

mqttc.on_connect = on_connection_success
mqttc.on_message = on_message_recieve

mqttc.tls_set_context(context = ssl_context)
mqttc.connect(aws_end_point,port=443)

mqttc.loop_start()
time.sleep(2)

i = 0
while (i<5):
    mqttc.publish('test/b','Message Publishing')
    print('Publishing......')
    time.sleep(5)
    i += 1
    
mqttc.loop_start()


