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