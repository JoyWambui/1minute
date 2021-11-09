from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    """Class that defines a User Model and helps us create new users."""
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    user_password = db.Column(db.String(255))
    
    @property
    def password(self):
        """Defines a write only class property password"""
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        """Method that takes in a password and hashes it."""
        self.user_password = generate_password_hash(password)


    def verify_password(self,password):
        """Method that checks whether a hashed password and user password that it hashes match."""
        return check_password_hash(self.user_password,password)

    def __repr__(self):
        return f'User {self.username}'
    

    