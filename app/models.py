from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')  # 联系

    def __repr__(self):
        return '<Role: %r>' % self.rolename


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 外键

    @property
    def password(self):
        raise AttributeError('密码不是可读属性')

    @password.setter
    def password(self, password):  # 设置密码
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):  # 校验密码
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<user: %r>' % self.username


class Mollusk_type(db.Model):
    __tablename__ = 'dic_mollusk_type'
    id = db.Column(db.Integer, primary_key=True)
    molluskname = db.Column(db.String(32), unique=True)

    def __repr__(self):
        return '<molluskname: %r>' % self.molluskname


class Breedfarm(db.Model):  # 养殖场字典
    __tablename__ = 'breedfarm'
    id = db.Column(db.Integer, primary_key=True)
    farmname = db.Column(db.String(64), nullable=True)
    linkman = db.Column(db.String(64), nullable=True)
    farmaddr = db.Column(db.String(128), nullable=True)  # 农场地址？
    zipcode = db.Column(db.String(8), nullable=True)  # 邮政编码
    tel = db.Column(db.String(11), nullable=True)  # 手机
    email = db.Column(db.String(32), nullable=True)  # 电子邮箱

    def __repr__(self):
        return '<breedfarm: %r>' % self.farmname


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
