from flask import Flask, redirect, render_template, request, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "BrianNotOnFranzList"
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process', methods=['post'])
def submitted_info():
	if len(request.form['first_name']) and len(request.form['last_name']) < 1:
 		flash('name field cannot be empty')
	if not request.form['first_name'].isalpha() or request.form['last_name'].isalpha():
 		flash('Name can only contain letters')
    	return redirect('/')
	if len(request.form['email']) < 1 : 
		flash("email cannot be empty")
        return redirect('/')
	if not EMAIL_REGEX.match(request.form['email']): 
		flash("Invalid Email Address")  
    	return redirect('/')
    if len(request.form['email']) < 1 :
		flash("email cannot be empty")
        return redirect('/')
    if len(request.form['password']) < 8: 
    	flash('Password must be at least eight 8 characters')
        return redirect('/')
    if request.form['password'] != request.form['confirmpassword']: 
    	flash('Password and confirm password do not match')
        return redirect('/')
    else:
        flash('Thanks for filling out the form correctly')
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        return redirect('/')
app.run(debug=True)




# from flask import Flask, redirect, render_template, request, flash
# import re
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# app = Flask(__name__)
# app.secret_key = "secret"
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def processPage():
	
# 	if len(request.form['first_name']) and len(request.form['last_name']):
# 		flash('name field cannot be empty')
		
# 	if not request.form['first_name'].isalpha() or request.form['last_name'].isalpha():
# 		flash('Name can only contain letters')
		
# 	if len(request.form['email']) < 1:
# 		flash('Email cannt be empty')
		
# 	if not EMAIL_REGEX.match(request.form['email']):
# 		flash('Invalid Email')
		
# 	if len(request.form['password']) < 1:
# 		flash('Password cannot be blank')
		
# 	if len(request.form['confirmpassword']) < 1:
# 		flash('confirm Password cannot be blank')
		
# 	if request.form['password'] != request.form['confirmpassword']: 
# 		flash('Passwords do not match')
		
# 	else: 
# 		flash('success')
#     	first_name = request.form['first_name']
#     	last_name = request.form['first_name']
#     	email = request.form['email']
#     	password = request.form['password']
#     	confirmpassword = request.form['congirmpassword']
#     	return redirect('/')
	# return render_template("result.html", name = name, places = places, language = language, textarea=textarea)
	# print request.form

	    
	
app.run(debug=True)


