from __future__ import print_function
import sys
import ssl
import time
import datetime
import logging, traceback
import paho.mqtt.client as mqtt


IoT_protocol_name = "x-amzn-mqtt-ca"
aws_iot_endpoint = "a1xip87ws8cwe4-ats.iot.us-east-2.amazonaws.com" # <random>.iot.<region>.amazonaws.com
url = "https://{}".format(aws_iot_endpoint)

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
mqttc.loop_start()

topic = "test/date" 

while True:
	now = "Hello Everyone...."
	print("try to publish:{}".format(now))
	mqttc.publish('mytopic/iot','How are you')
	time.sleep(3)
