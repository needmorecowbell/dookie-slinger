#!/usr/bin/python3

import smtplib
from django.template import Template, Context

from django.conf import settings
import django

TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': './res/templates/email.txt'

        }

        ]

settings.configure(TEMPLATES=TEMPLATES)

django.setup()

sender_email = 'from@gmail.com' # insert user email
sender_name= 'Adam Musciano'
receivers = ['to@todomain.com'] #insert company email

header = """From: From {{sender_name}} <{{sender_email}} >
To: To {{receiver_name}} <{{receiver_email}}>
Subject: {{subject}}

"""

with open('./res/templates/email.txt', 'r') as myfile:
        body = myfile.read()
message= header+body


for receiver in receivers:
    template = Template(message)
    custom_info = {
            "sender_name":"Adam Musciano",
            "sender_email":sender_email,
            "receiver_name":receiver,
            "company":"Rain Reality",
            "job_title":"web developer",
            "name":"Adam Musciano"
            }

    #insert templated text, replacing tags with config/contact info

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com',587)
       # smtpObj.sendmail(sender, receivers, template.render(Context(custom_info )))         
        print("Full Message:\n"+ template.render(Context(custom_info)) )
        print( "Successfully sent email")
    except SMTPException:
        print( "Error: unable to send email")




