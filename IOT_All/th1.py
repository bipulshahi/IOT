import requests
import random
import time
from flask import Flask

#GET https://api.thingspeak.com/update?api_key=57JYXAWTXH13QKJT&field1=0

app = Flask(__name__)

app.route('/sensor_value',methods=['GET'])

for i in range(5):
    t = random.randint(30,70)
    h = random.randint(30,70)
    print("Temp",t)
    print("Humi",h)
    
    if t > 45:
        print("Temperature is above Threshold")
        
    response1 = requests.get(f'https://api.thingspeak.com/update?api_key=57JYXAWTXH13QKJT&field1={t}&field2={h}')
    print(response1)
    print(response1.text)

    print("****************************************************")
    time.sleep(15)
