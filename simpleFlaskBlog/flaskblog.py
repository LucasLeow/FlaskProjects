from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__) # Creating instance of Flask Class
# __name__ : special variable signifying name of module
# if script ran directly, __name__ == __main__
 
app.config['SECRET_KEY'] = "a23d811e63141cc6adffbdebfca8e82d" # To protect against modifying cookies and cross-site request forgery attacks
# import secrets : secrets.token_hex(16)

posts = [
    {
        'author' : 'lucas',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'August 6, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET', 'POST']) # methods to accept
def register():
    form = RegistrationForm() # Creating instance of Registration Form
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home')) # url_for(method_name)
    return render_template('register.html', title = 'Register', form = form) # Template have access to Registration class instance assigned to form var

@app.route("/login")
def login():
    form = LoginForm() # Creating instance of Registration Form
    return render_template('login.html', title = 'Login', form = form) # Template have access to Registration class instance assigned to form var
    


# Need to set environment variable to the file that we want to be our flask application
# set FLASK_APP = flaskblog.py in cmd prompt

if __name__ == '__main__':
    app.run(debug = True)