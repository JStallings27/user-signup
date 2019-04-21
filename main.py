from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template("homepage.html")



def is_acceptable():
    is_acceptable = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!?@#$%&*-+_.,'


def validate_password():
    
    password = request.form['pass_word']
    verify_password = request.form['verify']

    password_error = ''
    verify_error = ''

    if not is_acceptable(password):
        password_error = "Must contain numbers, letters and any of the available characters !?@#$%&*-+_.,'"
    else:
        password = password
        if len(password) < 3 or len(password) > 20:
            password_error = 'Password must be between 3 - 20 characters'         


    if verify_password != password:
        verify_error = 'Does not match password'

    if not password_error and not verify_error:
        return render_template('/welcome')
    else:
        return render_template('homepage.format',password_error=password_error, 
        verify_error=verify_error, password=password, 
        verify_password=verify_error)

@app.route('/welcome')
def welcome():
    return render_template('welcome_page')



app.run()