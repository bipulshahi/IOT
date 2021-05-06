import ssl
import time
import datetime
import paho.mqtt.client as client
import random

i = 0

IoT_protocol = "x-amzn-mqtt-ca"
aws_end_point = "amwmnb948lrc8-ats.iot.ap-south-1.amazonaws.com"

ca = "./AmazonRootCA1.pem"
cert = "./5120bd2888-certificate.pem.crt"
private = "./5120bd2888-private.pem.key"

ssl_context = ssl.create_default_context()
ssl_context.set_alpn_protocols([IoT_protocol])
ssl_context.load_verify_locations(cafile=ca)
ssl_context.load_cert_chain(certfile=cert , keyfile=private)

def on_connection_success(mqttc,userdata,flags,rc):
    print('Connected with response code',rc)
    mqttc.subscribe('test/a')

def on_message_recieve(mqttc,userdata,msg):
    global i
    a = msg.payload.decode()
    print(a)
    if a == 'hello':
        t = random.randint(20,40)
        h = random.randint(20,40)
        i += 1
        #timestamp = datetime.datetime.now()
        mqttc.publish('mytopic/iot','{"sno" : "'+str(i)+'" , "T": '+str(t)+' , "H": '+str(h)+'}')
        

mqttc = client.Client()

mqttc.on_connect = on_connection_success
mqttc.on_message = on_message_recieve

mqttc.tls_set_context(context = ssl_context)
mqttc.connect(aws_end_point,port=443)

mqttc.loop_start()
time.sleep(2)


