from flask_wtf import FlaskForm
from flask_babel import _, lazy_gettext as _babel
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField(_babel('Username'), validators=[DataRequired()])
    password = PasswordField(_babel('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_babel('Remember me'))
    submit = SubmitField(_babel('Sign in'))

class RegistrationForm(FlaskForm):
    username = StringField(_babel('Username'), validators=[DataRequired()])
    email = StringField(_babel('Email'), validators=[DataRequired(), Email()])
    password = PasswordField(_babel('Password'), validators=[DataRequired()])
    confirm = PasswordField(_babel('Confirm password'), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_babel('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError(_babel('Such username is already registered'))

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError(_babel('Such email is already used'))

class EditProfileForm(FlaskForm):
    username = StringField(_babel('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_babel('About me'), validators=[Length(min = 0, max = 140)])
    submit = SubmitField(_babel('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username = self.username.data).first()
            if user is not None:
                raise ValidationError(_babel('This username already exists'))

class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    post = TextAreaField(_babel('Say something'), validators=[DataRequired(), Length(min = 1, max = 140)])
    submit = SubmitField()

class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_babel('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_babel('Request password reset'))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_babel('Password'), validators=[DataRequired()])
    confirm = PasswordField(_babel('Confirm password'), 
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_babel('Set new password'))