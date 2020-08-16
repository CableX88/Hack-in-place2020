from flask import render_template
from app import app

@app.route('/', methods=['POST','GET'])
@app.route('/login', methods=['POST','GET'])
def login():
    pass

@app.route('/create-account', methods=['POST', 'GET'])
def create_account():
	pass

@app.route('/index', methods=['POST', 'GET'])
def index():
	pass

@app.route('/my-profile', methods=['POST', 'GET'])
def my_profile():
	pass

@app.route('/academic', methods=['POST', 'GET'])
def academic():
	pass

@app.route('/social', methods=['POST', 'GET'])
def social():
	pass

@app.route('/wellness', methods=['POST', 'GET'])
def wellness():
	pass

@app.route('/connection', methods=['GET'])
def connection():
	pass

@app.route('/clubs')
def clubs():
	pass
