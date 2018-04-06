from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def landingPage():
    return render_template("index.html", nameOfPage = "Landing Page")
@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html", info = "Awesome")
@app.route('/dojos')
def dojo():
    return render_template("dojos.html")
app.run(debug=True, port=5002)
