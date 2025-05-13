from flask import Flask, request, g, redirect, url_for, render_template, flash, session
import deci_maker as dm

app = Flask(__name__)

app.config.update(dict(SECRET_KEY='development key'))

@app.route('/', methods=["GET"])
def home():
    d = dm.Decisions()
    session["ops"] = d.decis
    return render_template("home.html")

@app.route("/form", methods=["GET"])
def form():
    func = request.form.get("func")
    session["type"] = func
    return render_template("form.html")

@app.route("/add", methods=["POST"])
def add():
    d = session["ops"]
    item = request.form.get("input")
    d.append(item)
    session["ops"] = d
    return render_template('form.html', d=d)
