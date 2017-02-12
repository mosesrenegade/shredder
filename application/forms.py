from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    remember_me = BooleanField('remember_me', default=False)

class NewShell(FlaskForm):
    shell_url = StringField('shell_url', validators=[DataRequired()])
    shell_type = StringField('shell_type', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        FlaskForm.__init__(self, *args, **kwargs)
