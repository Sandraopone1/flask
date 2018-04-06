from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key="Secret"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index', methods=['POST'])
def processPage():
	
	if len(request.form['name']) < 1:
		flash('name field cannot be empty')
		return redirect('/')
  	if len(request.form['textarea']) < 1:
		flash('Please leave a comment')
		return redirect('/')
		
	if len(request.form['textarea']) > 120:
		flash('Your comment must be less that 120 characters')	
		return redirect('/')


	name = request.form['name']
	places = request.form['places']
	language = request.form['language']
	textarea = request.form['textarea']
	return render_template("result.html", name = name, places = places, language = language, textarea=textarea)
	# return redirect('/result')
	
app.run(debug=True)


