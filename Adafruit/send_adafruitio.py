from Adafruit_IO import RequestError, Client, Feed
 
ADAFRUIT_IO_KEY      = 'aio_ckBE74gyEs9OeA3MIjmMzVFLJhE1'       
ADAFRUIT_IO_USERNAME = 'Bipul07'

aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)

try:
     test = aio.feeds('test')
     #test2 = aio.feeds('test_H')
except RequestError:
     test_feed = Feed(name='test')
     test_feed = aio.create_feed(test_feed)

aio.send_data(test.key,45)
aio.send_data(test.key,55)
#aio.send_data(test2.key,65)
