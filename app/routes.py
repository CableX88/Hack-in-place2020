from flask import render_template
from app import app
from flask import request, redirect, url_for

dummyusers = {"johndoe@ex.com": "password"}
current_user = 0

@app.route('/', methods=['POST','GET'])
@app.route('/login', methods=['POST','GET'])
def login():
	if request.method == 'POST':
		if request.form['signin'] == "Create an Account":
			return redirect(url_for('create_account'))
		email = request.form['email']
		password = request.form['password']
		# look up the user
		if email in dummyusers.keys():
			if password == dummyusers[email]:
				global current_user
				current_user = email
				return redirect(url_for('index'))
	return render_template('ConnectWorkLogin.html')

@app.route('/create-account', methods=['POST', 'GET'])
def create_account():
	if request.method == 'POST':
		fullname = request.form['fname']
		email = request.form['email']
		password = request.form['pwd']
		global dummyusers, current_user
		dummyusers[email] = password
		current_user = email
		return redirect(url_for('index'))
	return render_template('create-account.html')

@app.route('/index', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		if 'profile' in request.form:
			return redirect(url_for('my_profile'))
		if 'academic' in request.form:
			return redirect(url_for('academic'))
		if 'social' in request.form:
			return redirect(url_for('social'))
		if 'wellness' in request.form:
			return redirect(url_for('wellness'))
	return render_template('index.html')

@app.route('/my-profile', methods=['POST', 'GET'])
def my_profile():
	return render_template('my-profile.html')

@app.route('/academic', methods=['POST', 'GET'])
def academic():
	return render_template('academic.html')

@app.route('/social', methods=['POST', 'GET'])
def social():
	return render_template('social.html')

@app.route('/wellness', methods=['POST', 'GET'])
def wellness():
	return render_template('wellness.html')

@app.route('/connection', methods=['GET'])
def connection():
	return render_template('connection.html')

# @app.route('/clubs')
# def clubs():
# 	pass
