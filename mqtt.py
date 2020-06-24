import time
import paho.mqtt.client as mqtt



def on_connect(client, userdata, flags, rc):
		print ("Connected with Code :" +str(rc))
		#Subscribe Topic
		client.subscribe("Test/#")

def on_message(client, userdata, msg):
		print ( str(msg.payload))

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message




client.username_pw_set("wfnjbrix","oBiV4f0lMdQv")
client.connect("m15.cloudmqtt.com", 10541, 60)

#client.loop_forever()
client.loop_start()
time.sleep(1)
while True:
	client.publish("Tutorial","Getting started with MQTT")
	print("Message Sent")
	time.sleep(15)
client.loop_stop()
client.disconnect
