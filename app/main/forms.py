from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, RadioField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch title', validators=[Required()])
    author = TextAreaField('Enter your comment here', validators=[Required()])
    body = StringField('Author', validators=[Required()])
    category = RadioField('Pick cateory', choices=[('wired', 'wired')], validators=[Required()])
    submit = SubmitField('submit')



class CommentForm(FlaskForm):
    title = StringField('title', validators=[Required()])
    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')

class Vote(FlaskForm):
    rating = RadioField('Rate this pitch', choices=[('upvote','upvote'), ('downvote','downvote')],validators=[Required()])


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us more about you', validators=[Required()])