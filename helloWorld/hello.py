from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
	return render_template('index.html')

# app.run(debug=True, port=5002)
# @app.route('/user/<username>/<id>')
# def show_user_profile(username, id):
# 	print username
# 	print id
# 	return render_template("user.html")

app.run(debug=True)