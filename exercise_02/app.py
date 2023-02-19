from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/calculate")
def calculate():
    number = request.args["number"]

    if number == "":
        return render_template('calculate.html', odd_or_even="No number provided!")
    
    try:
        number = int(number)
        if number % 2 == 0:
            numberstring = f"{number} is even"
        else:
            numberstring = f"{number} is odd"
    except ValueError:
        numberstring = f"{number} is not an integer!"
    return render_template('calculate.html', odd_or_even=numberstring)