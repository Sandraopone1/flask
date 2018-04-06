from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')
@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Hello world"


# from flask import Flask, render_template, redirect, request

# app = Flask(__name__)
# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/users', methods=['POST'])
# def create_user():
#     print "Got Post Info"
#     # recall the name attributes we added to our form inputs
#     # to access the data that the user input into the fields we use request.form['name_of_input']
#     name = request.form['name']
#     email = request.form['email']
#     # print request.form
#     # return redirect('/') # redirects ba
#     return render_template('success.html')


# app.run(debug=True)



# @app.route('/success/<username>')
# def create(username):
# 	return render_template("success.html")
# app.run(debug=True)

