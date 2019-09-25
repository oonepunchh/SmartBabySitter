from flask import Flask, render_template
import pyrebase
import threading
import firebase_admin
from firebase_admin import messaging
from firebase_admin import credentials
from breathing_chest import *
import time

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

cred = credentials.Certificate('service-account.json')
default_app = firebase_admin.initialize_app(cred)

app = Flask(__name__)

def warning() :
    topic = 'test'
    message = messaging.Message(
        data={
            'warning': 'warning'
        },
        topic=topic
    )
    response = messaging.send(message)
    return response

#Thread
def background_thread() :
    while True :
        # txt-file read
        r = open('C:/Users/Admin/Desktop/HSEC/darknet-master/build/darknet/x64/results/status.txt', mode='rt',encoding='utf-8')
        posture = r.read()
        breathing = extractEdge()

        db.update({"posture": posture})
        db.update({"breathing": breathing})

        if posture == "down":
            warning()
        elif breathing == "False":
            warning()
        else :
            continue

        time.sleep(1)
#server
@app.route('/')
def main():
    global thread
    thread = threading.Thread(target=background_thread())
    #thread.start()
    return render_template("index.html")

@app.route('/index')
def index():
    return render_template("index.html")

if __name__ == "__main__" :
    app.run(debug=True)