from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def landingPage():
    return render_template("submitForm.html")
@app.route('/process', methods=['POST'])
def processPage():
    print request.form['name']
    return redirect('/')
app.run(debug=True, port=5003)
