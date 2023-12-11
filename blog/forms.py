from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField



class LoginForm(FlaskForm):
    name = StringField('name', validators=[validators.DataRequired()])
    password = PasswordField("password", validators=[validators.DataRequired()])