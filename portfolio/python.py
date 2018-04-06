from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')          
def hello_world():
  return 'Welcome to my Portfolio page'
@app.route('/projects')
def projectsPage():
	return render_template('projects.html')
@app.route('/about')
def aboutPage():
    return render_template('about.html')


app.run(debug=True)
