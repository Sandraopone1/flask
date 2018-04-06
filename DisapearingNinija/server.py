from flask import Flask, render_template, request, redirect, session  

app = Flask(__name__)
app.secret_key = "secret"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
	img = "static/images/Ninjas/tmnt.png"
	return render_template('ninja.html', image = img)

@app.route('/ninja/<color>')
def color(color):
	# if color == "blue":
	# 	img = "../static/images/Ninjas/leonardo.jpg"
 #    	return render_template('ninja.html', image = img)
	# if color == "red":
	# 	img = "../static/images/Ninjas/raphael.jpg"
 #    	return render_template('ninja.html', image = img)
	# if color == "orange":
	# 	img = "../static/images/Ninjas/michelangelo.jpg"
 #    	return render_template('ninja.html', image = img)
	# if color == "puple":
	# 	img = "../static/images/Ninjas/donatello.jpg"
 #    	return render_template('ninja.html', image = img)
	# else:
 #    	image = "../static/Ninjas/notapril.jpg"
 #    	return render_template('/ninjas.html', image = image)

	if color == "blue":
   		image = "../static/images/Ninjas/leonardo.jpg"
    	return render_template('/ninjas.html', image = image)
	if color == "orange":
		image = "../static/images/Ninjas/michelangelo.jpg"
    	
        return render_template('/ninjas.html', image = image)
	if color == "red":
    	image = "../static/images/Ninjas/raphael.jpg"
        return render_template('/ninjas.html', image = image)
	if color == "purple":
    	image = "../static/images/Ninjas/donatello.jpg"
    	return render_template('/ninjas.html', image = image)
	else:
    	image = "../static/images/Ninjas/notapril.jpg"
    	return render_template('/ninjas.html', image = image)
app.run(debug=True)