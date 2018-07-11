from flask import Flask, jsonify, session, redirect, request
from flask_sqlalchemy import SQLAlchemy 
import datetime 
from models import *
import jwt
from functools import wraps   


app = Flask (__name__)
app.config['SECRET_KEY']="Kirugik"

app.config["SQLALCHEMY_DATABASE_URL"] = 'postgresql://postgres:Malakwen@localhost5432/mydb' 

db = SQLAlchemy (app)



@app.route('/')
def home_page():
    return jsonify({"message": "Welcome to Homepage"})


@app.route('/register', methods=['POST'])
def register ():
		first_name = request.get_json()["first_name"]
		last_name = request.get_json()["last_name"]
		email = request.get_json()["email"]
		username = request.get_json()["username"]
		password = request.get_json()["password"]	
		try:
			conn = psycopg2.connect(database="mydb", user = "postgres", password = "Malakwen", host = "127.0.0.1", port = "5432")
			with conn.cursor () as cursor:
				postgres="INSERT INTO `users` (`first_name`, `last_name`, `email`, `username`, `password`) VALUES ('"+first_name+"', '"+last_name+"', '"+email+"', '"+username+"','"+password+"');"
				cursor.execute("CREATE TABLE IF NOT EXISTS `users`  (  id = db.Column(db.Integer, primary_key=True), first_name = db.Column (db.String (100), nullable= False), last_name = db.Column (db.String (10), nullable= False),email = db.Column (db.String(120), unique=True, nullable=False),username = db.Column(db.String(100), unique=True, nullable=False),password= db.Column (db.String(100), unique=True, nullable=False)")
				try:
					cursor.execute("SELECT * FROM users WHERE username == 'username' and password == 'password'")
            		try:
                		cursor.execute("SELECT * FROM `users` WHERE `username` = "username"")
                		if cursor.fetchone() is not None:
                    return jsonify({"Message":"User is already registered"})
                cursor.execute(postgres)
            except:
                return jsonify({"message": "Registration failed"})
        conn.commit()
    finally:
        conn.close()
    return jsonify({"message": "You have registered successfully"})

def generate_auth_token(t):
	@wraps(t)
	def decorated(*args, **kwargs):
		if request.args.get("token") == "":
			return jsonify ({"message": "Login"})
		try:
			jwt.decode(request.args.get("token"), app.config['SECRET_KEY'])
		except:
			return jsonify({"Message":"You are not logged in"})
		return t(*args,**kwargs)
	return decorated


def log_in():
	username = request.get_json()["username"]
	password = request.get_json()["password"]
    cursor.execute("SELECT FROM users WHERE username = %s;", username) 
    if cursor.fetchone()[0]:
        cursor.execute("SELECT * FROM users WHERE username = %s;", username) 
        for row in cursor.fetchall():
            if password == password:
            	token = jwt.encode({"username":username,"exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=10)},app.config["SECRET_KEY"])
            	return jsonify ({"message ":"You have successfully logged in"})
            else:
				return jsonify ({"message": "You must register first"})
	else:
		return jsonify({'message' : 'Username does not exist'})
    cursor.close()



@app.route('/new_post', methods=["POST"])
def new_post(): 
	comment=request.get_json()["comment"]
	data = jwt.decode(request.args.get('token'), app.config['SECRET_KEY'])
    username=data['username']
    try:
        with conn.cursor() as cursor:
            postgresql ="INSERT INTO `comments`(`comment`), 'date', 'user_id' VALUES(%s, %s, %s)"
            try:
                cursor.execute("SELECT * FROM users WHERE username = 'username'")
                if cursor.fetchone() is not None:
                    cursor.execute(, (comment, date, user_id))
                else:
                    return jsonify({"message" : "You are not a registered user"})
        conn.commit()
    return jsonify({'message' : "You have posted a new comment"})


@app.route("/view_comments",methods =['GET'])
def view_comments():
	cursor.execute("SELECT * FROM comments")
    rows=cursor.fetchall()
    return (rows)

@app.route('/remove/<int:commentID>', methods = ["DELETE"])
def remove(commentID):
	self.username = username
    try:
        with conn.cursor() as cursor:
            postgresql="DELETE FROM `comments` WHERE `comments`.`commentID`and `comments`.`username`= '"+username+"'"
            try:
                cur.execute("SELECT * FROM `comments` WHERE `comments`.`commentID` = `comments`.`username`")
                comment=cur.fetchone()
                if result is None:
                    return jsonify({"message" : "You cannot delete this comment"})
        connection.commit()
    return jsonify({"message" : "You have deleted a comment"})


@app.route('/account', methods=['GET'])
def account():
	cursor.execute("SELECT * FROM users")
	rows=cursor.fetchall()
	return (rows)


if __name__=='__main__':
		app.run (debug = True, port = 5054)
