from flask import Flask, jsonify, session, redirect, url_for, render_template, request

app = Flask (__name__)

user_details ={}
user_comments = []


@app.route('/', methods = ["GET"])
def home_page():
	return jsonify ({"Home page": "You are not logged in"})

@app.route('/register', methods=['POST'])
def register ():
	if request.method == 'POST':
		first_name = request.get_json("first_name")
		last_name = request.get_json("last_name")
		email = request.get_json('email')
		username = request.get_json("username")
		password = request.get_json("password")

	user_details.update(request.get_json())
	return jsonify (user_details)

	
@app.route ('/login', methods = ["POST"])
def login():
	if request.method == "POST":
		username = request.get_json('username')
		password = request.get_json('password')
		if username in user_details :
			if user_details[username]["password"]:
				return jsonify ({"message ":"Login successful"})
			else:
				return jsonify ({"message ":"Wrong password"})
		else:
			return jsonify ({"message ":"You are not Registered. Register to Login"})


@app.route('/new_post', methods=['POST'])
def new_post():
	comment=request.get_json("New comment post")
	user_comments.append(request.get_json())
	return jsonify({"message": "create new post"})

@app.route('/account', methods=['GET'])
def account():
	return jsonify ({"user_details": user_details})


if __name__=='__main__':
		app.run (debug = True, port = 5055)
