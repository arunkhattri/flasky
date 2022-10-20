#!/usr/bin/env python3
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


# dynamic routes
@app.route("/user<name>")
def user(name):
    return "<h1>Hello, {}</h1>".format(name)
