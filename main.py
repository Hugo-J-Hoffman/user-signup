from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True     


@app.route("/edit", methods=['POST'])
def username_error():
    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['email']
    username_error=""
    password_error=""
    vpassword_error=""
    email_error=""

    if len(username)>20 or len(username)<3:
        username_error= "That is not a valid username"
    if " " in username or len(username)==0:
        username_error= "That is not a valid username"
    if len(password)>20 or len(password)<3:
        password_error= "That is not a valid password"
    if " " in password or len(password)==0:
        password_error= "That is not a valid password"
    if password != vpassword:
        password_error= "Passwords must match"
        vpassword_error= "Passwords must match"
    if len(email)>0:
        if len(email)>20 or len(email)<3:
            email_error= "That is not a valid email"
        if "@" not in email or "." not in email:
            email_error= "That is not a valid email"
    if username_error=="" and password_error=="" and vpassword_error=="" and email_error=="":
        return render_template('header-footer.html', username=username)
    return render_template('edit.html', username_error = username_error, password_error = password_error, vpassword_error = vpassword_error, email_error = email_error)

@app.route("/")
def index():
    return render_template('edit.html')

app.run()