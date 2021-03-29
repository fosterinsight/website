from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Name", [DataRequired("Please enter your name.")])
    email = EmailField("Email", [DataRequired("Please enter your email address."),
                                 Email("This field requires a valid email address")])
    subject = StringField("Company", [DataRequired("Please enter a subject.")])
    message = TextAreaField("Message", [DataRequired("Not including a message would be stupid")])

    submit = SubmitField("Send")
