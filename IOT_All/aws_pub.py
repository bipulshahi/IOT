import time
import paho.mqtt.client as client
import ssl
import random

IoT_protocol = "x-amzn-mqtt-ca"
aws_end_point = "amwmnb948lrc8-ats.iot.ap-south-1.amazonaws.com"

ca = "./AmazonRootCA1.pem"
cert = "./69311293f0-certificate.pem.crt"
private = "./69311293f0-private.pem.key"

ssl_context = ssl.create_default_context()
ssl_context.set_alpn_protocols([IoT_protocol])
ssl_context.load_verify_locations(cafile=ca)
ssl_context.load_cert_chain(certfile=cert , keyfile=private)

mqttc = client.Client()
mqttc.tls_set_context(context = ssl_context)

mqttc.connect(aws_end_point,port=443)
mqttc.loop_start()

for i in range(5):
    t = random.randint(20,45)
    print("Message Publishing")
    mqttc.publish("mytopic/iot" , f"Temperature:{t}")
    time.sleep(2)
