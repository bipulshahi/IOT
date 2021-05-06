import random
import time
from flask import Flask,jsonify
import requests

app = Flask(__name__)

@app.route('/update_value',methods=['GET'])
def update_value():
        t = random.randint(30,70)
        h = random.randint(30,70)
    
        if t > 45:
            m = "Temperature is above Threshold"
        else:
            m = "Temperature is under control"
        
        call = requests.get(f'https://api.thingspeak.com/update?api_key=57JYXAWTXH13QKJT&field1={t}&field2={h}')

        if call.status_code == 200:
            n = "Sensor value Published"
        else:
            n = "Connection Error"

            
        notification = ("Temperature",t,"Humidity",h,m,n)
        return jsonify(notification)

        time.sleep(15)
'''            
        notification = {"Temperature & Humidity":f"Temperature {t} Humidity {h}",
                        "Message" : m,
                        "Update_status":n}
'''
    
        


app.run()
