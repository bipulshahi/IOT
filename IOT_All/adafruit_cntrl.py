from Adafruit_IO import MQTTClient

Adafruit_IO_Key = "aio_GtbZ69U8oKOEo3zYQyRSwYcZykvG"
Adafruit_IO_Username = "bipul257"

def on_connection_success(mqttc):
    print('Connected.Listening changes....')
    mqttc.subscribe('device')

def disconnect(mqttc):
    print('Disconnected from Adafruit IO')
    sys.exit(1)
    
def on_message_recieve(mqttc,feed_id,status):
    if feed_id == 'device':
        if status == 'ON':
            print('LED ON')
        elif status == 'OFF':
            print('LED OFF')
    
mqttc = MQTTClient(Adafruit_IO_Username,Adafruit_IO_Key)

mqttc.on_connect = on_connection_success
mqttc.on_disconnect = disconnect
mqttc.on_message = on_message_recieve

mqttc.connect()
mqttc.loop_blocking()
