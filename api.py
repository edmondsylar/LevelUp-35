from flask import Flask, request, jsonify
app = Flask(__name__)

users = []

@app.route('/')
def index():
	return 'Functioning'


# The Add user endpoint
@app.route('/api/add-user', methods =['POST'])
def add_user():
	user = {
		'name':request.json['name'],
		'email':request.json['email'],
		'psw':request.json['psw']
	}
	users.append(user)
	return jsonify({'User Created':users})

# The Viewing user End point
@app.route('/api/get-users', methods =['GET'])
def getter():
	return jsonify({'values': users})


# The deleting End point.
@app.route('/api/delete-user/<string:gone>', methods = ['DELETE'])
def remover(gone):
	for user in users:
		if user['name'] == gone:
			users.remove(user)

	return jsonify({'User deleted':users})


if __name__=='__main__':
	app.run(debug=True, port=8999)