from flask_wtf import FlaskForm
from wtforms import ValidationError,StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    """Class that registers a new user."""
    user_email = StringField("Input Your Email Address",validators=[Required(),Email()])
    username = StringField('Input Preferred Username',validators = [Required()])
    user_password = PasswordField('Input New Password',validators = [Required(), EqualTo('user_password_confirm',message = 'Passwords do not match!')])
    user_password_confirm = PasswordField('Confirm New Password',validators = [Required()])
    submit_details = SubmitField('Sign Up')
    
    def email_validation(self,data_field):
        """Checks if an input email is already registered with an acoount."""
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("This email is registered to an account.")

    def username_validation(self,data_field):
        "Checks if a chosen username already exists in the application."
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("This username exists. Choose another one.")
    
class LoginForm(FlaskForm):
    """Class that logs in an existing user."""
    login_email = StringField("Input Your Email Address",validators=[Required(),Email()])
    login_password = PasswordField("Input Password",validators =[Required()])
    remember_me = BooleanField("Remember this user")
    submit = SubmitField("Log In")   