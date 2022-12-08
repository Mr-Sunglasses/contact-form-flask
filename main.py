import os
from pathlib import Path
from flask import Flask, render_template, request, flash
from dotenv import load_dotenv
from firebase import Firebase
env_path = Path('.', '.env')
load_dotenv(dotenv_path=env_path)

config = {
    "apiKey": os.getenv("apiKey"),
    "authDomain": os.getenv("authDomain"),
    "projectId" : os.getenv("projectId"),
    "storageBucket" : os.getenv("storageBucket"),
    "messagingSenderId" : os.getenv("messagingSenderId"),
    "appId" : os.getenv("appId"),
    "measurementId" : os.getenv("measurementId"),
    "databaseURL" : os.getenv("databaseURL"),
}

firebase = Firebase(config)

db = firebase.database()

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")

        data = {
            "name": name,
            "email": email
        }
        db.child("All Submissions").push(data)
        return render_template('index.html')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
