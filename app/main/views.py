from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Category, User
from flask_login import login_required
#@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
#@login_required
#def new_comment(id):

@main.route("/")
def index():
    """View root page function that returns the index page and its data"""
    return render_template("index.html")

@main.route('/user/<username>')
def my_profile(username):
    "Show user profile."
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)
    title="Profile Page"
    return render_template("profile/user_profile.html", user=user,title=title)

@main.route("/categories")
def categories():
    """View function that returns the categories page andshows the available categories"""
    categories = Category.get_categories()
    title="Pitch Categories"
    return render_template("categories.html",categories=categories, title=title)
    