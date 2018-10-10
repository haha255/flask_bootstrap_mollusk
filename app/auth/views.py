from flask import render_template, request, redirect, url_for, flash
from . import auth
from .forms import LoginForm, RegisterForm
from ..models import User, db
from flask_login import login_user, logout_user, login_required


@auth.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # 根据Email，取出用户名
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('无效的用户名或者密码!')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已经安全退出登录!')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.password = form.password.data  # 自动加密的原因，要写成属性设置方式。
        db.session.add(user)  # db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/setting')
def setting():
    return render_template('auth/setting.html')
