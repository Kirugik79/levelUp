from flask import Flask
import datetime
import psycopg2
from flask_sqlalchemy import SQLAlchemy  


app = Flask (__name__)

conn = psycopg2.connect(database="mydb", user = "postgres", password = "Malakwen", host = "127.0.0.1", port = "5432")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
cursor = conn.cursor()

print ("database opened successfully")


db = SQLAlchemy (app)

class Register (db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column (db.String (100), nullable= False)
    last_name = db.Column (db.String (10), nullable= False) 
    email = db.Column (db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False) 
    password= db.Column (db.String(100), unique=True, nullable=False)
 
    def __init__(self, first_name, last_name, email,username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password

    def save(self):
     db.session.add(self)
     db.session.commit()

    def delete(self):
     db.session.delete(self)
     db.session.commit()

    @staticmethod
    def get_all_users():
        return Register.query.all()
    
    @staticmethod
    def get_one_user():
        return Register.query.get(id)

    def __repr(self):
     return '<id {}>'.format(self.id)


class Login(db.Model):
    pass


class Comments (db.Model):
    __tablename__ = "comments"
    comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime)
    
    def __init__(self, comment, date, user_id):
        self.user_id = user_id
        self.comment = comment
        self.user_id = user_id
        self.date = datetime.datetime.utcnow()


    def delete(self):
     db.session.delete(self)
     db.session.commit()


class Admin (db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column (db.String(100), unique=True, nullable=False)

    def __init__(self, admin_id, username, password):
        self.admin_id = admin_id
        self.username = username
        self.password = password


print ("Database Tables created successfully")

conn.commit()

conn.close()