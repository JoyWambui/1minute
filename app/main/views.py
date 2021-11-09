from flask import render_template
from . import main
#from flask_login import login_required
#@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
#@login_required
#def new_comment(id):

@main.route("/")
def index():
    """View root page function that returns the index page and its data"""
    return render_template("index.html")
