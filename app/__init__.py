from flask import Flask
from flask_bootstrap import Bootstrap
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


__author__ = 'LYH'
bootstrap = Bootstrap()  # 模板对象
db = SQLAlchemy()  # 数据库对象
login_manager = LoginManager()  # 认证登录对象
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    from .main import main as main_blueprint  # 主页蓝本
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint  # 登录蓝本
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    return app
