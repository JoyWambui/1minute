from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from .forms import RegistrationForm,LoginForm
from . import authentication
from ..models import User
from .. import db
from ..email import welcome_mail_message


@authentication.route("/registration",methods=["GET","POST"])
def register():
    """View registration page function and its data. Registers and creates a new user and saves to the db."""
    
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        new_user = User(username = registration_form.username.data,email = registration_form.user_email.data,password = registration_form.user_password.data)
        db.session.add(new_user)
        db.session.commit()
        welcome_mail_message("Welcome to 1Minute Pitch","email/welcome_email",new_user.email,new_user=new_user)
        return redirect(url_for("authentication.login"))
    title="New Account"
    return render_template('auth/registration.html',registration_form = registration_form,title=title)

@authentication.route("/login",methods=["GET","POST"])
def login():
    """View login page function and its data. Logs in an existing user."""

    login_form = LoginForm()
    if login_form.validate_on_submit():
        existing_user = User.query.filter_by(email = login_form.login_email.data).first()
        if existing_user is not None and existing_user.password_verification(login_form.login_password.data):
            login_user(existing_user,login_form.remember_me.data)
            return redirect(request.args.get("next") or url_for("main.index"))

        flash("Invalid username or Password")

    title = "Watchlist Login"
    return render_template("auth/login.html",login_form = login_form,title=title)

@authentication.route('/logout')
@login_required
def logout():
    """View function that logs out a user."""
    logout_user()
    return redirect(url_for("login"))
