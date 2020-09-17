from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY      = 'aio_ckBE74gyEs9OeA3MIjmMzVFLJhE1'       
ADAFRUIT_IO_USERNAME = 'Bipul07'

def connected(client):
     print ('Connected. Listening changes...')
     client.subscribe('led')

def disconnected(client):
     print ('Disconnected from Adafruit IO!')
     sys.exit(1)

def message(client, feed_id, status):
     if feed_id == 'led':
          if status == '1':
               print("Bulb On")
          elif status == '0':
               print("Bulb OFF")

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message

client.connect()
client.loop_blocking()
