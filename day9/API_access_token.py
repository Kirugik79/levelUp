from flask import Flask, jsonify, session, redirect, request
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp 
from functools import wraps

app = Flask (__name__)
app.config["SECRET_KEY"] = "kirugik"


user_details = {}
user_comments = []

user1 = "Robert"
pass1 = "abc123"

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


#Homepage endpoint
@app.route('/', methods = ["GET"])
def home_page():
	return jsonify ({"Home page": "Welcome to Homepage"})

#This is a user registration endpoint
@app.route('/register', methods=['POST'])
def register ():
		first_name = request.get_json()["first_name"]
		last_name = request.get_json()["last_name"]
		email = request.get_json()["email"]
		username = request.get_json()["username"]
		password = request.get_json()["password"]

		user_details.update({username:{"first_name":first_name, "last_name":last_name, "email":email,"password":password}})
		return jsonify ({"user": user_details, "message": "You have been successfully registered"})
		print (user_details)

#This is a user login endpoint
@app.route ('/login', methods = ["POST"])
def login():
	username = request.get_json()["username"]
	password = request.get_json()["password"]
	if username in user_details:
		if password == user_details[username]["password"]: 
			token = jwt.encode({"username":username,"exp":datetime.datetime.utcnow()+datetime.timedelta(minutes=10)},app.config["SECRET_KEY"])
			return jsonify({"token":token.decode("utf-8")})
		return jsonify ({"message ":"You have successfully logged in"})
	return jsonify ({"message": "You must register first"})

#This is an endpoint for new comments
@app.route('/new_post', methods=["POST"])
def new_post(): 
	comment=request.get_json()["comment"]
	user_comments.append(comment)
	return jsonify ({"message": "new comment posted"})

#This is an endpoint to view all user comments
@app.route("/view_comments",methods =['GET'])
def view_comments():
	username = request.get_json()["username"]
	if username in user_details:
			for each in user_comments:
				comments.update({user_comments.index(each):each})
			return jsonify(comments)
	else:
		return jsonify({"message": "You must register first"})

#This is an endpoint to delete comments
@app.route('/remove/<int:commentID>', methods = ["DELETE"])
def remove(commentID):
	del user_comments[commentID]
	return jsonify({"message": "You have deleted a comment"})

#This is an endpoint to fetch user details
@app.route('/account', methods=['GET'])
def account():
	username = request.get_json()["username"]
	if username in user_details:
		return (user_details)

if __name__=='__main__':
		app.run (debug = True, port = 5054)
