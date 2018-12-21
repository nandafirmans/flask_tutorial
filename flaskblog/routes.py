from flask import render_template, url_for, redirect, flash
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


@app.route("/")
@app.route("/home")
def home():
    posts = [
        {
            "author": "Agus Nuraniah",
            "title": "Blog post 1",
            "content": "lorem ipsum dolor sit amet",
            "date_posted": "April 21, 2018"
        },
        {
            "author": "Aldo Alfian",
            "title": "Blog post 2",
            "content": "lorem ipsum dolor sit amet",
            "date_posted": "June 21, 2018"
        },
        {
            "author": "Nanda Firmansyah",
            "title": "Blog post 3",
            "content": "lorem ipsum dolor sit amet",
            "date_posted": "June 02, 2018"
        },
    ]
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account {form.username.data} is succefully created!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Registration", form=form)


@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "admin" and form.password.data == "admin":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
           flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)
