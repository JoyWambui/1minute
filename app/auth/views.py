from . import authentication
from flask import render_template,redirect,url_for
from ..models import User
from .forms import RegistrationForm
from .. import db


@authentication.route("/registration",methods=["GET","POST"])
def register():
    """View registration page function and its data. Registers and creates a new user and saves to the db."""
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        new_user = User(email = registration_form.email.data, username = registration_form.username.data,password = registration_form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('authentication.login'))
    return render_template('auth/registration.html',registration_form = registration_form)