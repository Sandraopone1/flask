# from flask import Flask, render_template, redirect, session, request
# import random
# app = Flask(__name__)

# app.secret_key = 'ThisIsSecret'


# @app.route('/')
# def index():
# 	if "number" not in session:
# 		session["number"] = random.randint(1, 101)
# 	return render_template("index.html")
	
# @app.route('/process', methods=['POST'])
# def process():	
	
# 	guessNumber = int(request.form['guessNum'])

# 	if guessNumber > session['number']:
# 	    session["result"] = "Too high!"

# 	elif guessNumber < session['number']:
# 		session["result"]= "Too low!"
		
# 	elif guessNumber == session['number']:
# 		sessionsession["result"] = 'You guessed correct!' 
		
# 	return redirect('/')		
	


# #     if "count" not in session:
# #         session["count"] = 0
# #     session["count"] += 2
# #     return redirect('/')

# # @app.route('/reset')
# # def reset():
# # 	session["count"] = 0
# # 	return redirect('/')

# # @app.route('/process', methods = ['POST'])
# # def ninjas():
# # 	if "counter" not in session:
# # 		session['counter'] = 0

# # 	session['counter'] += 2
# # 	return redirect('/')

# app.run(debug=True)


from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)

app.secret_key = "S12Zr47j\3yX R~X@H!jmM]Lwf/,?KTW%"

@app.route("/")
def index():
	if "number" not in session:
		session["number"] = random.randint(1, 101)
	return render_template("index.html")

@app.route("/process", methods=["POST"])
def Process():
	if request.form['action'] == 'farm':
 
	elif request.form['action'] == 'cave':
  
	print session["number"]
	if int(request.form["guess"]) == session["number"]:
		session["result"] = "Correct"
	elif int(request.form["guess"]) > session["number"]:
		session["result"] = "high"
	else:
		session["result"] = "low"
	return redirect("/")

@app.route("/replay")
def play_Again():
	session.pop("number")
	session.pop("result")
	return redirect("/")

app.run(debug=True)