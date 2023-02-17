from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def get_time():
    date = datetime.now()
    date = date.strftime("%A, %B %d %Y %H:%M:%S")
    return render_template('index.html', date_time=date)