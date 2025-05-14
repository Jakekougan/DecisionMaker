from flask import Flask, request, g, redirect, url_for, render_template, flash, session
import deci_maker as dm
import random as rand

app = Flask(__name__)

app.config.update(dict(SECRET_KEY='development key'))

@app.route('/', methods=["GET"])
def home():
    d = dm.Decisions()
    session["ops"] = d.decis
    return render_template("home.html")

@app.route("/form", methods=["GET"])
def form():
    func = request.args.get("func")
    session["type"] = func
    print(func)
    return render_template("form.html", func=func)

@app.route("/add", methods=["POST"])
def add():
    d = session["ops"]
    item = request.form.get("input")
    d.append(item)
    session["ops"] = d
    return render_template('form.html', d=d)

@app.route("/selRand", methods=["GET"])
def select_random():
    r = rand.choice(session['ops'])
    return render_template("sel.html", dec=r)


@app.route("/delRand", methods=["GET"])
def remove_random():
    d = session["ops"]
    r = rand.choice(session['ops'])
    indx = d.index(r)
    removed = d.pop(indx)
    flash(f"{removed} has been removed from the pool")
    return render_template("form.html", removed=removed, d=d)

