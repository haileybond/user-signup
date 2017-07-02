from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('signup_form.html')
    return template.render()

def is_empty(input):
    if input = ''
        return True

def is_correct_length(input):
    if len(input) is < 3 or len(input) > 20:
        return False
    
def contains_space(input):
    if ' ' in input:
        return True

def valid_email(input):
    if '@' in input:
        if '.' in input:
            return True     


#define validation form
@app.route("/signup", methods=['POST'])
def signup():
    #get input from form
    input_username = request.form['username']
    input_password = request.form['password']
    input_password = request.form['password2']
    input_email = request.form['email']

    #initialize blank error messages
    username_error = ''
    password_error = ''
    email_error = ''

    #validate the username (length, no spaces, field required)
    if is_empty(input_username):
        username_error = "This field is required"
    if is_correct_length(input_username) = False:
        username_error = "Username must be between 3 and 20 characters"
    if contains_space(input_username) = True:
        username_error = "Username must not contain spaces"

    #validate the password (length, no spaces, field required)
    if is_empty(input_password):
        password_error = "This field is required"
    if is_correct_length(input_password) = False:
        password_error = "Password must be between 3 and 20 characters"
    if contains_space(input_password) = True:
        password_error = "Password must not contain spaces"

    #validate that password = password2 (must match password)
    if input_password != input_password2:
        password_error = "Passwords must match"

    #validate email (length, no spaces, contains @ and .)
    if is_correct_length(input_email) = False:
        email_error = "Username must be between 3 and 20 characters"
    if contains_space(input_email) = True:
        email_error = "Email must not contain spaces"
    if valid_email(input_email) = False:
        email_error = "Email must contain these symbols: '@' and '.'"

    #if there are no errors:
    if not username_error and not password_error and not email_error:
        #redirect to Welcome Page
        return redirect('')
    else:
        return
        #error messages


