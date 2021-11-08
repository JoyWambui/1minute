from . import db

class User(db.Model):
    """Class that defines a User Model and helps us create new users."""
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'
    

    