import re
from sqlalchemy.orm import backref, lazyload
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    """Class that defines a User Model and helps us create new users."""
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True,index=True)
    user_password = db.Column(db.String(255))
    pitches = db.relationship("Pitch",backref="user",lazy="dynamic")
    comments = db.relationship("Comment", backref="user",lazy="dynamic")
    categories = db.relationship("Category", backref="user",lazy="dynamic")

    @property
    def password(self):
        """Defines a write only class property password"""
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        """Method that takes in a password and hashes it."""
        self.user_password = generate_password_hash(password)


    def password_verification(self,password):
        """Method that checks whether a hashed password and user password that it hashes match."""
        return check_password_hash(self.user_password,password)
    
    def get_user_id(self):
        return self.id

    def __repr__(self):
        return f'User {self.username}'
    
@login_manager.user_loader
def loads_user(user_id):
    """Method that queries the datbase and gets a user with the passed id."""
    return User.query.get(int(user_id))  

class Pitch(db.Model):
    """Class that defines a Pitch Model and creates new pitches."""
    __tablename__ = "pitches"
    id = id = db.Column(db.Integer,primary_key = True)
    user_pitch = db.Column(db.String(800))
    time_posted = db.Column(db.DateTime,default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))
    comments = db.relationship("Comment",backref="pitch",lazy="dynamic")

    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_user_pitches(cls,id):
        """Returns all a user's pitches."""
        user_pitches = Pitch.query.filter_by(user_id=id).all()
        return user_pitches
    @classmethod
    def get_all_pitches(cls):
        """Returns all pitches."""
        pitches = Pitch.query.all()
        return pitches  

    
class Category(db.Model):
    """Creates category instances and defines category methods.""" 
    __tablename__="categories"
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitches = db.relationship("Pitch",backref="category",lazy="dynamic")

    def save_category(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_categories(cls):
        """Returns all categories."""
        categories = Category.query.all()
        return categories 
    
class Comment(db.Model):
    """Class that defines a Pitch Model and creates new pitches."""
    __tablename__ = "comments"
    id = id = db.Column(db.Integer,primary_key = True)
    author=db.Column(db.String(100))
    comment = db.Column(db.String)
    time_posted = db.Column(db.DateTime,default=datetime.now)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_pitch_comments(cls,id):
        """Returns all a pitch's comments."""
        pitch_comments = Comment.query.filter_by(pitch_id=id).all()
        return pitch_comments
    


    