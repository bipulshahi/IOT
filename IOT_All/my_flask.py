from flask import Flask

app = Flask(__name__)


@app.route('/sensor_value',methods=['GET'])
def sensor_value():
    return "Hello"

@app.route('/update_server',methods=['GET'])
def update_server():
    return "Welcome"

app.run()
