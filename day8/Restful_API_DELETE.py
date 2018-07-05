from flask import Flask, jsonify, session, redirect, url_for, render_template, request

app = Flask (__name__)

user_details ={}
user_comments = []


@app.route('/', methods = ["GET"])
def home_page():
	return jsonify ({"Home page": "Welcome to Homepage"})

@app.route('/register', methods=['POST'])
def register ():
		first_name = request.get_json("first_name")
		last_name = request.get_json("last_name")
		email = request.get_json("email")
		username = request.get_json("username")
		password = request.get_json("password")

		user_details.update({"first_name":first_name, "last_name":last_name, "email":email,"password":password})
		return jsonify ({"message": "You have been successfully registered"})
		print (user_details)

	
@app.route ('/login', methods = ["POST"])
def login():
	username = request.get_json("username")
	password = request.get_json("password")
	for username in user_details:
		if password == user_details[username]["password"]: 
			session ["logged_in"] = True
			return jsonify ({"message ":"You have successfully logged in"})
		else:
			return jsonify ({"message ":"Incorrect password"})
	else:
		return jsonify ({"message ":"You are not Registered. Register to Login"})


@app.route('/new_post', methods=['POST'])
def new_post(): 
	comment=request.get_json("New post")
	user_comments.append(request.get_json())
	return jsonify({"message": "create new post"})


@app.route("/view_comments",methods =['GET'])
def view_comments():
    for each in user_comments:
        user_comments.append({user_comments.index(each):each})
    return jsonify(user_comments)
    
@app.route('/account', methods=['GET'])
def account():
	return jsonify ({"user_details": user_details})


@app.route('/remove/<int:commentID>', methods = ['DELETE'])
def remove():
	del user_comments[commentID]
	return jsonify({"user_comments": "You have deleted a comment"})


if __name__=='__main__':
		app.run (debug = True, port = 5054)
