from flask import Flask, render_template
from math import sqrt, pi

app = Flask(__name__)


@app.route("/")
def root():
    a = 1 + 5
    return render_template("base.html.j2", a=a)


@app.route("/abc")
def abc():
    odmocnina = sqrt(2)
    return render_template("abc.html.j2", odmocnina=odmocnina, pi=pi)
