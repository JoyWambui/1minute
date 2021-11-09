from flask_mail import Message
from flask import render_template
from . import mail

subject_prefix = "1Minute: "
sender_email ="joy.ndegwa@student.moringaschool.com"

def welcome_mail_message(subject,template,to,**kwargs):

    welcome_email = Message(subject_prefix+subject,sender=sender_email,recipients=[to])
    welcome_email.body= render_template(template + ".txt",**kwargs)
    welcome_email.html = render_template(template + ".html",**kwargs)
    mail.send(welcome_email)