from flaskapp import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True)

    def __init__(self, username, password, first_name, last_name, email):

        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __repr__(self):
        return '<User: %r>' % self.username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.username)

class Search(db.Model):

    search_id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    description = db.Column(db.String(200))
    user_name = db.Column(db.String(50), db.ForeignKey('user.username'))

    def __init__(self, description, user_name):
        self.description = description
        self.user_name = user_name

    def __repr__(self):
        return '<Search: %r>' % self.search_string


# Adapted code from https://medium.com/@perwagnernielsen/getting-started-with-flask-login-can-be-a-bit-daunting-in-this-tutorial-i-will-use-d68791e9b5b5