from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField # Classes
from wtforms.validators import DataRequired, Length, Email, EqualTo

# DataRequired : To ensure field is not empty
class RegistrationForm(FlaskForm): #Inherit from FlaskForm Class
    username = StringField('username', 
                           validators = [DataRequired(), Length(min = 2, max = 20)]) # Also used as label in HTML (display)
    # Validators used to ensure username conform to certain conditions desired by us (within 20 chars etc.)
    email = StringField('email',
                        validators = [DataRequired(), Email()])
    
    password = PasswordField('password',
                             validators = [DataRequired()])
    
    confirm_password = PasswordField('confirm password',
                                     validators = [DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')
    
    
class LoginForm(FlaskForm): #Inherit from FlaskForm Class
    
    email = StringField('email',
                        validators = [DataRequired(), Email()])
    
    password = PasswordField('password',
                             validators = [DataRequired()])
    
    remember = BooleanField('Remember Me')
    login = SubmitField('Login')
    