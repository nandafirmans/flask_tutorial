from datetime import datetime
from flask import Flask, render_template, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app: Flask = Flask(__name__)
app.config["SECRET_KEY"] = "16165e4fab20daa5803bbf722c635b6e"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db: SQLAlchemy = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(200), nullable=False, default="default.jpg", )
    username = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email}, {self.image_file})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.date_posted})"


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

    if form.validate_on_submit() and form.username.data == "admin" and form.password.data == "admin":
        flash("You have been logged in!", "success")
        return redirect(url_for("home"))

    flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)
