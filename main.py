from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

#don't need jinja? 
#add cgi escaping!

#template_dir = os.path.join(os.path.dirname(__file__), 'templates')
#jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

@app.route("/")
def index():
    return render_template('signup_form.html')

def is_empty(input):
    if not input:
        return True

def is_correct_length(input):
    if len(input) >= 3 and len(input) <= 20:
        return True
    
def contains_space(input):
    if " " in input:
        return True

def valid_email(input):
    at_count = 0
    for each_char in input:
        if each_char == '@':
            at_count = at_count + 1
    
    period_count = 0
    for each_char in input:
        if each_char == '.':
            period_count = period_count + 1

    if period_count == 1 and at_count == 1:
        return True

#initialize blank error messages

#define validation form
@app.route("/signup", methods=['POST'])
def signup():
    username_error = ''
    password_error = ''
    password2_error = ''
    email_error = ''

    #get input from form
    input_username = request.form['username']
    input_password = request.form['password']
    input_password2 = request.form['password2']
    input_email = request.form['email']

    #validate the username (length, no spaces, field required)
    if is_empty(input_username):
        username_error = "This field is required"
        input_username = ''
    elif contains_space(input_username):
        username_error = "Username must not contain spaces"
        input_username = ''
    elif not is_correct_length(input_username):
        username_error = "Username must be between 3 and 20 characters"
        input_username = ''

    #validate the password (length, no spaces, field required)
    if is_empty(input_password):
        password_error = "This field is required"
    elif contains_space(input_password):
        password_error = "Password must not contain spaces"
    elif not is_correct_length(input_password):
        password_error = "Password must be between 3 and 20 characters"
    
    #validate that password = password2 (must match password)
    if is_empty(input_password):
        password2_error = "This field is required"
    elif contains_space(input_password):
        password2_error = "Password must not contain spaces"
    elif not is_correct_length(input_password):
        password2_error = "Password must be between 3 and 20 characters"
    elif input_password != input_password2:
        password2_error = "Passwords must match"

    #validate email (length, no spaces, contains @ and .)
    if is_empty(input_email):
        email_error = ''
    else:
        if contains_space(input_email):
            email_error = "Email must not contain spaces"
            input_email = ''
        if not is_correct_length(input_email):
            email_error = "Email must be between 3 and 20 characters"
            input_email = ''
        if not valid_email(input_email):
            email_error = "Email must contain these symbols: '@' and '.'"
            input_email = ''

    if username_error or password_error or password2_error or email_error:
        return render_template('signup_form.html', username_error = username_error, password_error = password_error, password2_error = password2_error, email_error = email_error, username = input_username, email = input_email)        
    if not username_error and not password_error and not email_error:
        return welcome(input_username)

app.route('/welcome')
def welcome(username):
    return render_template('welcome.html', username = username)
   
app.run()