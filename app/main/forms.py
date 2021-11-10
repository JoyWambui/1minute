from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import Required

class PitchForm(FlaskForm):

    name = StringField('Input Name',validators=[Required()])
    pitch = TextAreaField('Write your Pitch: ')
    submit = SubmitField('Submit Pitch')
    
class CommentForm(FlaskForm):

    author = StringField('Input Name',validators=[Required()])
    pitch = TextAreaField('Add a Comment: ')
    submit = SubmitField('Submit Comment')

    