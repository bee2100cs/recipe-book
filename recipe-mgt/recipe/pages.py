from flask import Blueprint, render_template, url_for, redirect
from flask_login import current_user

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    # if current_user.is_authenticated:
    #     return render_template("pages/home.html")
    # else:
    #     login_url = url_for('auth.login')  # Generating the URL for the login route in auth.py
    #     return f'<a class="button" href="{login_url}">Google Login</a>'
    return render_template("pages/home.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route("/browse")
def browse():
    return render_template("pages/browse.html")

@bp.route("/add")
def add():
    return render_template("pages/add.html")
