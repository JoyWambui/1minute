from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Comment, User,Category,Pitch
from flask_login import login_required,current_user
from .forms import PitchForm,CommentForm
import markdown2

@main.route("/")
def index():
    """View root page function that returns the index page and its data"""
    pitches = Pitch.get_all_pitches()
    title="1Minute App"
    return render_template("index.html",title=title,pitches=pitches)

@main.route('/user/<username>')
def my_profile(username):
    "Show user profile."
    user = User.query.filter_by(username = username).first()
    user_pitches= Pitch.get_user_pitches(user.id)

    if user is None:
        abort(404)
    title="Profile Page"
    return render_template("profile/user_profile.html", user=user,title=title,user_pitches=user_pitches)

@main.route("/categories")
def categories():
    """View function that returns the categories page andshows the available categories"""
    categories = Category.get_categories()
    title="Pitch Categories"
    return render_template("categories.html",categories=categories, title=title)

@main.route('/categories/pitch/new/<name>', methods = ['GET','POST'])
@login_required
def new_pitch(name):

    pitch_form = PitchForm()
    category = Category

    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        pitch = pitch_form.pitch.data
        new_pitch = Pitch(user_pitch=pitch,user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = "New Pitch"
    return render_template('new_pitch.html',title = title, pitch_form=pitch_form, category=category)

@main.route("/pitch/<int:id>")
def single_pitch(id):
    pitch=Pitch.query.get(id)
    comments = Comment.get_pitch_comments(pitch.id)
    if pitch is None:
        abort(404)
    format_pitch = markdown2.markdown(pitch.user_pitch,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('pitch.html',pitch=pitch,format_pitch=format_pitch,comments=comments)

@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):

    comment_form= CommentForm()
    pitch = Pitch.query.get(id)

    if comment_form.validate_on_submit():
        author = comment_form.author.data
        pitch_comment = comment_form.pitch.data
        new_comment = Comment(author=author,comment=pitch_comment,user=current_user,pitch_id=pitch.id)
        new_comment.save_comment()
        return redirect(url_for('.single_pitch',id=pitch.id))

    title = "New Comment"
    return render_template('new_comment.html',title = title, comment_form=comment_form)
