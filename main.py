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
    if input == '':
        return True

def is_correct_length(input):
    if len(input) < 3 or len(input) > 20:
        return False
    
def contains_space(input):
    if ' ' in input:
        return True

def valid_email(input):
    at_count = 0
    for each_char in input:
        if each_char == '@':
            at_count = at_count + 1
    if at_count > 1:
        return False
    
    period_count = 0
    for each_char in input:
        if each_char == '.':
            period_count = period_count + 1
    if period_count > 1:
        return False

    else:
        return True

#initialize blank error messages
username_error = ''
password_error = ''
password2_error = ''
email_error = ''

#define validation form
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    #get input from form
    input_username = request.form['username']
    input_password = request.form['password']
    input_password = request.form['password2']
    input_email = request.form['email']

    #validate the username (length, no spaces, field required)
    if is_empty(input_username):
        username_error = "This field is required"
    if not is_correct_length(input_username):
        username_error = "Username must be between 3 and 20 characters"
    if contains_space(input_username):
        username_error = "Username must not contain spaces"

    #validate the password (length, no spaces, field required)
    if is_empty(input_password):
        password_error = "This field is required"
    if not is_correct_length(input_password):
        password_error = "Password must be between 3 and 20 characters"
    if contains_space(input_password):
        password_error = "Password must not contain spaces"

    #validate that password = password2 (must match password)
    if input_password != input_password2:
        password2_error = "Passwords must match"

    #validate email (length, no spaces, contains @ and .)
    if not is_correct_length(input_email):
        email_error = "Username must be between 3 and 20 characters"
    if contains_space(input_email):
        email_error = "Email must not contain spaces"
    if not valid_email(input_email):
        email_error = "Email must contain these symbols: '@' and '.'"
    
    if not username_error and not password_error and not email_error:
        return redirect('/welcome')
    else:
        return render_template('signup_form.html', username_error = username_error, password_error = password_error, password2_error = password2_error, email_error = email_error)

app.route('/welcome')
def welcome():
    return render_template('welcome.html', username = username)
   
app.run()