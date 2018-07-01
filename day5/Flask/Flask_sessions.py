

from flask import Flask, session, redirect, url_for, render_template, request



app = Flask (__name__)
app.secret_key = "kisumu level_up"


dictionary = {}
user_info = []

post_comment = {}
comments = []


@app.route('/index')
def welcome ():
    if not session.get('logged_in'):
    	return render_template ('login.html')
    return  render_template('new_post.html')

@app.route('/home_page')
def home_page():
	return render_template('home.html')

@app.route ('/login', methods = ["GET", "POST"])
def login():
        if request.method == 'POST':
                for username in self.dictionary:
                    if user_info['username'] == request.form['username']:
                        return redirect(url_for('welcome'))
                    else:
                        return redirect(url_for('register'))
                    return render_template('login.html', error=error)
                return render_template ('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register ():
    if request.method == 'POST':
        self.dictionary ['user_id'] = len (users) + 1
        self.dictionary ['username'] = request.form.get('username')
        self.dictionary ['email'] = request.form.get('email')
        self.dictionary ['password'] = request.form.get('password')
        self.dictionary.append(user_info)

        print (self.dictionary)
        return render_template('register.html')
    return render_template('register.html')


@app.route('/new_post', methods=['GET','POST'])
def new_post():
        if request.method == 'POST':
            post_comment['post_id'] = len(posts)+1
            post_comment['create new post'] = request.form.get('create new post')

            posts.append(post_comment)

            print(comments)

            return render_template('new_post.html')

        return render_template('new_post.html')


@app.route('/logout')
def logout ():
    session.pop('logged_in', None)
    return render_template('home.html')

if __name__=='__main__':
        app.run (debug = True)
