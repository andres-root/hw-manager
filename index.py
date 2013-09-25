from flask import Flask
import serial

app = Flask(__name__)


@app.route('/<x>')
def hello(x):
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ret = ser.write(x)
    if(ret):
        return 'Exito %s' % x
    return 'NOO %s' % x

if __name__ == "__main__":
    app.run(host='0.0.0.0')
