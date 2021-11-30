from flask import Flask, render_template, session, request, redirect, url_for
from math import sqrt, pi

import config

app = Flask(__name__)
app.secret_key = "os.urandom(24)"
app.secret_key = config.secret


@app.route("/")
def root():
    a = 1 + 5
    return render_template("base.html.j2", a=a)


@app.route("/abc/", methods=["GET"])
def abc():
    jmeno = request.args.get("jmeno")
    heslo = request.args.get("heslo")
    if jmeno:
        session["susenka"] = jmeno
    odmocnina = sqrt(2)
    return render_template("abc.html.j2", odmocnina=odmocnina, pi=pi)


@app.route("/abc/", methods=["POST"])
def abc_post():
    jmeno = request.form.get("jmeno")
    heslo = request.form.get("heslo")
    if jmeno:
        session["susenka"] = jmeno
    if jmeno == 'marek' and heslo == 'lokomotiva':
        session['user'] = jmeno
    odmocnina = sqrt(2)
    return redirect(url_for("abc"))


@app.route("/logout/")
def logout():
    session.pop("user", None)
    return redirect(url_for('abc'))
