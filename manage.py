from app import create_app, db
from flask_script import Manager,Server
from app.models import User,Booking
from  flask_migrate import Migrate, MigrateCommand
# Creating app instance
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Pitch = Pitch,Comment = Comment )

if __name__ == '__main__':
    manager.run()




# from app import create_app, db
# from flask_login import UserMixin,
# from datetime import datetime


# class User(UserMixin,db.Model):
#     __table__ = 'users'
#     id = db.Column(db.Integer,primary_key = True)
#     username = db.Column(db.String(255),index =True)
#     email = db.Column(db.String(255),unique = True,index =True)
#     bookings = db.relationship('Booking',backref = 'user', lazy = 'dynamic')

#     @property
#     def password(self):
#         raise AttributeError('You cannot read the password attribute')

#     @password.setter
#     def password(self, password):
#         self.pass_secure = generate_password_hash(password)

#     @login_manager.user_loader
#     def load_user(user_id):
#         return User.query.get(int(user_id))

#     def verify_password(self, password):
#         return check_password_hash(self.pass_secure, password)

#     def save_user(self):
#         db.session.add(self)
#         db.session.commit()


#     def __repr__(self):
#         return f'User {self.username} '



# class Booking(db.Model):
#     __tablename__ = 'bookings'
#     id = db.Column(db.Integer,primary_key = True)
#     title =  db.Column(db.String(255))
#     session = db.Column(db.String(255))
#     category = db.Column(db.String(255))

#     def save_booking(self):
#         db.session.add(self)
#         db.session.commit()




