from flask import Flask, request
import string

app = Flask(__name__)
app.config['DEBUG'] = True


signup_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>User Signup</h1>
    <body>
        <form method='POST'>
            <label for=username/>Username</label>
            <input type="text" name="user" id="username" value='{user}' />
            <p class="error">{user_error}</p>

  
            <label for=password/>Password</label>
            <input type="password" name="pass_word" id="password" value='{pass_word}' />
            <p class="error">{pass_word_error}</p>

            <label for=verify_password/>Verify Password</label>
            <input type="password" name="verify" id="verify_password" value='{verify}'/>
            <p class="error">{verify_error}</p>

            <label for=email>Email (optional)</label>
            <input type="text" name="email_address" id="email" value='{email_address}'/>
            <p class="error">{email_address_error}</p>
            
            <input type="submit" value="Submit Query">
        </form>
    </body>
"""

@app.route("/")
def display_signup_form():
    return signup_form.format(user='', user_error='', pass_word='',pass_word_error='',
    verify='', verify_error='', email_address='', email_address_error='' )

def acceptable(entry):
    is_acceptable = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
    's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
    'P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','?',
    '@','#','$','%','&','*','-','+','_','.']
    
    try:
        for x in entry:
            if x in is_acceptable:
                return True
    except ValueError:
        return False

@app.route("/", methods=['POST'])
def validation():
    user = request.form['user']
    user_error=''
    email_address = request.form['email_address']
    email_address_error=''


    if len(user) < 3 or len(user) > 20:
        user_error = 'Username must be 3 - 20 characters'
    else:
        user = user

    if not acceptable(user):
        user_error = 'Must only contain letters, numbers, and the available symbols(!?@#$%&*-+_.)'
    else:
        user = user

    pass_word = request.form['pass_word']
    verify = request.form['verify']
    pass_word_error = ''
    verify_error = ''

    
    if len(pass_word) < 3 or len(pass_word) > 20:
        pass_word_error = 'Password must be 3 - 20 characters'
        pass_word = ''
        verify = ''
    else:
        pass_word = pass_word

    if not acceptable(pass_word):
        pass_word_error = 'Must only contain letters, numbers, and the available symbols(!?@#$%&*-+_.)'
        pass_word = ''
        verify = ''
    else:
        pass_word = pass_word

    if len(verify) < 3 or len(verify) > 20:
        verify_error = 'Password must be 3 - 20 characters'
        pass_word = ''
        verify = ''
    else:
        verify = verify
    
    if not acceptable(verify):
        verify_error = 'Must only contain letters, numbers, and the available symbols(!?@#$%&*-+_.)'
        pass_word = ''
        verify = ''
    else:
        verify = verify

    if pass_word != verify:
        pass_word_error = 'Both passwords must match'
        verify = 'Both passwords must match'
        pass_word = ''
        verify = ''
    else:
        pass_word = pass_word
        verify = verify

    if not user_error and not pass_word_error and not verify_error and not email_address_error:
        return "Success"
    else:
        return signup_form.format(user=user, user_error=user_error, pass_word_error=pass_word_error, verify_error=verify_error, pass_word=pass_word,
         verify=verify, email_address=email_address, email_address_error=email_address_error)


@app.route("/welcome", methods=['POST'])
def welcome():
    return '<h1>Welcome</h1>'


app.run()