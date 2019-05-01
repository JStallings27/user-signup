from flask import Flask, request, render_template, redirect
import string
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def display_signup_form():
    return render_template('sign_up.html', user='', user_error='', pass_word='',pass_word_error='',
    verify='', verify_error='', email_address='', email_address_error='' )

def acceptable(entry):
    is_acceptable = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
    's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
    'P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','?',
    '@','#','$','%','&','*','-','+','_','.']
    
    for x in entry:
        if x in is_acceptable:
            return True
        else:
            return False

def val_length(length):
    if len(length) > 2 and len(length) < 22:
        return True
    else:
        return False

def email_at_symbol(at):
    if at.count('@') == 1:
        return True
    else:
        return False

def email_dot_com(dot_com):
    if dot_com[-4:] == '.com':
        return True
    else:
        return False

@app.route("/", methods=['POST'])
def sign_validation():
    user = request.form['user']
    pass_word = request.form['pass_word']
    verify = request.form['verify']
    email_address = request.form['email_address']

    user_error=''
    pass_word_error = ''
    verify_error = ''
    email_address_error = ''
###################################################################
    
    if not acceptable(user):
        user_error = 'Must only contain letters, numbers, and the available symbols(!?@#$%&*-+_.)'
    elif not val_length(user):
        user_error = 'Username must be 3 - 21 characters'
    else:
        user = user
        user_error = ''
###################################################################
    
    if not acceptable(pass_word):
        pass_word_error = 'Must only contain letters, numbers, and the available symbols(!?@#$%&*-+_.)'
        pass_word = ''
        verify = ''
    elif not val_length(pass_word):
        pass_word_error = 'Username must be 3 - 21 characters'
        pass_word = ''
        verify = ''
    else:
        pass_word = pass_word
        pass_word_error = ''
###################################################################
    
    if not acceptable(verify):
        verify_error = 'Must only contain letters, numbers, and the available symbols(!?@#$%&*-+_.)'
        pass_word = ''
        verify = ''
    elif not val_length(verify):
        verify_error = 'Username must be 3 - 21 characters'
        pass_word = ''
        verify = ''
    elif verify != pass_word:
        pass_word_error = 'Passwords need to match'
        verify_error = 'Passwords need to match'
        pass_word = ''
        verify = ''
    else:
        verify = verify
        verify_error = ''
###################################################################
    
    if len(email_address) > 0:
        if not acceptable(email_address):
            email_address_error = 'Must only contain letters, numbers, and the available symbols(!?@#$%&*-+_.)'
        elif not val_length(email_address):
            email_address_error = 'Username must be 3 - 21 characters'
        elif not email_at_symbol(email_address):
            email_address_error = 'Must contain one @ symbol'
        elif not email_dot_com(email_address):
            email_address_error = 'Must end with .com'
        else:
            email_address = email_address
            email_address_error = ''
    else:
        email_address = ''
        email_address_error = ''

    

    if not user_error and not pass_word_error and not verify_error and not email_address_error:
        new_user = {user}
        return redirect("/welcome?new_user={0}".format(new_user))
    else:
        return render_template('sign_up.html', user=user, user_error=user_error, pass_word=pass_word, pass_word_error=pass_word_error, verify=verify, verify_error=verify_error, 
        email_address=email_address, email_address_error=email_address_error)


@app.route("/welcome")
def welcome():
    new_user = request.args.get('new_user')
    return render_template('welcome.html', new_user=user )


app.run()