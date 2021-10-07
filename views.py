from flask import Blueprint, render_template

views = Blueprint(__name__,"views")

@views.route("/")
def main():
    return render_template("index.html")

@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/profile")
def profile():
    return render_template("profile.html")

