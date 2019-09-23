from flask import *
import pyrebase
import time
import threading
import serial

config = {
    "apiKey": "AIzaSyCfvGXaZ_ltapjHIfByHOxTEMoD8UY3wGY",
    "authDomain": "smart-baby-sitter.firebaseapp.com",
    "databaseURL": "https://smart-baby-sitter.firebaseio.com",
    "projectId": "smart-baby-sitter",
    "storageBucket": "smart-baby-sitter.appspot.com",
    "messagingSenderId": "1022295587743",
    "appId": "1:1022295587743:web:a5c2e278ad7b38c9efdbaa"
};

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask(__name__)

#Thread
def background_thread() :
    # get value from arduino
    arduino = serial.Serial('COM3', 9600)
    arduino.flushInput()
    count = 0
    r = open('C:/Users/admin/Desktop/HSEC/darknet-master/darknet-master/build/darknet/x64/status/status.txt', mode='rt', encoding='utf-8')
    breathing = True

    #degree = input
    while True :
        input_s = arduino.readline()
        degree = int(input_s)
        # txt-file read
        posture = r.read()
        db.update({"posture": posture})
        db.update({"breathing": breathing})
        db.update({"degree": degree})
        r.seek(0)
        time.sleep(1)


#server
@app.route('/', methods=['GET','POST'])
def main() :
    global thread
    thread = threading.Thread(target=background_thread())
    thread.start()
    return render_template('index.html')

if __name__ == "__main__" :
    app.run(debug=True)