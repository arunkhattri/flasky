"""Flask Web Development, 2nd Ed, Miguel Grinberg."""
# /usr/bin/env python3
from datetime import datetime
from flask import Flask, render_template, session, flash, redirect, url_for
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config[
    "SECRET_KEY"
] = "I guess I can go anywhere I want. If only I knew where to go"
moment = Moment(app)


class NameForm(FlaskForm):
    """defines the list of fields in the form."""

    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def index():
    """Register handler for the application's root URL."""
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")
        session["name"] = form.name.data
        return redirect(url_for("index"))
    return render_template(
        "index.html",
        current_time=datetime.utcnow(),
        form=form,
        name=session.get("name"),
    )


# dynamic routes
@app.route("/user<name>")
def user(name):
    """Return dynamic user page."""
    return render_template("user.html", name=name)


# custom error pages
@app.errorhandler(404)
def page_not_found(e):
    """Return error 404 page."""
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    """Return internal server error page."""
    return render_template("500.html"), 500
