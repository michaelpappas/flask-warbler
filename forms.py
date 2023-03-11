from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Length


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('E-mail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])

class EditUserForm(FlaskForm):
    """ Edit a user's info form """

    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('E-mail', validators=[DataRequired()])
    image_url = StringField('(Optional) Image URL')
    header_image_url = StringField('(Optional) Image URL')
    bio = StringField('Bio', validators=[DataRequired()])
    location = StringField('Location')
    password = PasswordField('Password', validators=[Length(min=6)])

class ChangePasswordForm(FlaskForm):
    """ Edit a user's info form """

    New_password1 = PasswordField('New Password', validators=[Length(min=6)])
    New_password2 = PasswordField('Confirm New Password', validators=[Length(min=6)])
    password = PasswordField('Password', validators=[Length(min=6)])

class CSRFProtectionForm(FlaskForm):
    """ form for CSRF protection """
