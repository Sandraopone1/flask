from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index', methods=['POST'])
def processPage():
    name = request.form['name']
    places = request.form['places']
    language = request.form['language']
    textarea = request.form['textarea']
    return render_template("result.html", name = name, places = places, language = language, textarea=textarea)
    return redirect('/result')
app.run(debug=True, port=5009)


