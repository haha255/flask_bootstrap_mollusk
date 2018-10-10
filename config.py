import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))  # 取当前文件所在路径


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or '1qazxsw23edcvfr4!@@#'  # 取环境变量的密码或者自己规定的密码
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 设置数据库自动提交
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 设置为不追踪修改
    REMEMBER_COOKIE_DURATION = timedelta(minutes=30)  # 设置30分钟内不用重新登录。

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'mollusk.sqlite')
    DEBUG = False  # 设置程序启动是否允许debug


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'mollusk_test.sqlite')
    DEBUG = True  # 设置程序启动是否允许debug

config = {
    'development': ProductionConfig,
    'test': TestConfig,
    'default': ProductionConfig,
}
