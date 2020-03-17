from flask import Flask, request, jsonify
app = Flask(__name__)

users = []

@app.route('/')
def index():
	return 'Functioning'

@app.route('/api/add-user', methods =['POST'])
def add_user():
	user = {
		'name':request.json['name'],
		'email':request.json['email'],
		'psw':request.json['psw']
	}
	users.append(user)
	return jsonify({'msg':'User created'})

@app.route('/api/get-users', methods =['GET'])
def getter():
	return jsonify({'values': users})

@app.route('/api/delete-user/<string:gone>', methods = ['DELETE'])
def remover(gone):
	leave = [x for x in users if x['name']== gone]
	users.remove(leave)
	return jsonify({'msg':'User deleted'})


if __name__=='__main__':
	app.run(debug=True, port=8999)