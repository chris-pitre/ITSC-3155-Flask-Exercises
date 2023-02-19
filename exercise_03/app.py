from flask import Flask, render_template, request
app = Flask(__name__)

registrants = {}


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        registrants[request.form["name"]] = request.form["organization"]
    return render_template("index.html")

@app.route("/registrants", methods=["GET", "POST"])
def registrants_page():
    return render_template("registrants.html", result=registrants)