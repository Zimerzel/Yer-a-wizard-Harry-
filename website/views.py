from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route("/")
def main():
    return render_template("home.html")

@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/shop")
def shop():
    return render_template("shop.html")

@views.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    return render_template("profile.html")

