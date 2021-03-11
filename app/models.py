from app import db
from flask_login import UserMixin
from datetime import datetime
from . import login_manager



class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index =True)
    email = db.Column(db.String(255),unique = True,index =True)
    bookings = db.relationship('Booking',backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f'User {self.username} '



class Booking(db.Model):
    __tablename__ = 'bookings'
    id = db.Column(db.Integer,primary_key = True)
    # email = db.Column(db.String(255),unique = True,index =True)
    title =  db.Column(db.String(255))
    day = db.Column(db.String(255))
    session = db.Column(db.String(255))
    category = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_booking(self):
        db.session.add(self)
        db.session.commit()


    def __repr__(self):
        return f'Booking {self.day} '




