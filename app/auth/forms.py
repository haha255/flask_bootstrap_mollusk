from flask_wtf import FlaskForm
from ..models import User
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import Length, Email, DataRequired, Regexp, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(), Length(1, 64), Email()
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(), Length(1, 64), Email()
    ])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[\u4e00-\u9fa5_.A-Za-z]+$', 0,
                                                                                         '用户名必须由字母、数字、点或者下划线组成')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', message='2次录入的密码必须一致！')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email地址已经被占用，请更换一个新Email重试!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已被使用，请更换新用户名重试！')
