#Adafruit Python code for monitoring

import time
from Adafruit_IO import Client,Feed
import random

Adafruit_IO_KEY = "aio_GtbZ69U8oKOEo3zYQyRSwYcZykvG"
Adfruit_IO_Username = "bipul257"

client = Client(Adfruit_IO_Username,Adafruit_IO_KEY)

#feeds
temp_feed = client.feeds("t")

for i in range(10):
    Temp = random.randint(20,30)

    #send
    client.send(temp_feed.key,str(Temp))
    print(Temp)
    time.sleep(5)
