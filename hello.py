#!/usr/bin/env python3
from datetime import datetime
from flask import Flask, render_template
from flask_moment import Moment, moment


app = Flask(__name__)
moment = Moment(app)


@app.route("/")
def index():
    return render_template("index.html", current_time=datetime.utcnow())


# dynamic routes
@app.route("/user<name>")
def user(name):
    return render_template("user.html", name=name)


# custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
