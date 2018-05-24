from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
    email = StringField('Email address', validators=[Required(), Email()])
    username = StringField('enter your name', validators=[Required()])
    password = PasswordField('your password', validators=[Required(), EqualTo('password2', message='ensure passwords match')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Sign up')


    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('Email is already taken')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('User already taken')



class LoginForm(FlaskForm):
    email = StringField('Email address', validators=[Required(), Email()])
    password = PasswordField('password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('sign in')