from flask import Flask, render_template, request, redirect, session, flash  

app = Flask(__name__)
app.secret_key = "DojoSurvey"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if "count" not in session:
        session["count"] = 0
    session["count"] += 2
    return redirect('/')
    # return render_template('index.html')

@app.route('/reset')
def reset():
    session["count"] = 0
    return redirect('/')

app.run(debug=True)