from flask import render_template
from . import auth
from .forms import LoginForm


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    return render_template('auth/logout.html')


@auth.route('/register')
def register():
    return render_template('auth/register.html')
